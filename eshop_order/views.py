import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from eshop_order.forms import UserOrderForm
from eshop_order.models import Order, OrderDetail
from eshop_products.models import Product

from django.http import HttpResponse
from zeep import Client


@login_required(login_url='/login')
def user_order(request):
    user_order_form = UserOrderForm(request.POST or None)

    if user_order_form.is_valid():
        basket = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if basket is None:
            basket = Order.objects.create(owner_id=request.user.id, is_paid=False)
        product_id = user_order_form.cleaned_data.get('product_id')
        product = Product.objects.get_by_id(product_id)
        count = user_order_form.cleaned_data.get("count")
        basket.orderdetail_set.create(product_id=product_id, count=count, price=product.price, owner_id=request.user.id)
        return redirect(f"products/{product_id}/{product.title.replace(' ', '-')}")

    return redirect("/")


@login_required(login_url='/login')
def user_basket(request):
    context = {
        "basket": None,
        "basket_detail": None,
    }
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is not None:
        context["basket"] = order
        context["basket_detail"] = order.orderdetail_set.all()
    return render(request, 'basket.html', context)


@login_required(login_url='/login')
def remove_order(request, *args, **kwargs):
    detail_id = kwargs.get("detail_id")
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            if order_detail.count > 1:
                order_detail.count -= 1
                order_detail.save()
            else:
                order_detail.delete()
        return redirect("/basket")


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/verify'  # Important: need to edit for realy server.


def send_request(request):
    open_order: Order = Order.objects.filter(is_paid=False, owner_id=request.user.id).first()
    if open_order is not None:
        total_amount = open_order.get_amount()
        result = client.service.PaymentRequest(
            MERCHANT, total_amount, description, email, mobile,
            f"{CallbackURL}/{open_order.id}")
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


def verify(request, *args, **kwargs):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order_id = kwargs.get("order_id")
            order = Order.objects.get_queryset().get(id=order_id)
            order.is_paid = True
            order.payment_date = time.time()
            order.save()
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
