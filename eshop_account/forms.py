from django import forms
from django.contrib.auth.models import User
from django.core import validators


class User_edit(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "نام خود را وارد کنید", "class": "form-control"}),
        label=False

    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "نام خانوادگی خود را وارد کنید", "class": "form-control"}),
        label=False
    )


class Login(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "نام کاربری خود را وارد کنید"}),
        label=False,
        validators=[
            validators.MaxLengthValidator(limit_value=15, message="تعداد کاراکتر ها باید بین ۵ تا ۱۵ باشد!"),
            validators.MinLengthValidator(limit_value=5, message="تعداد کاراکتر ها باید بین ۵ تا ۱۵ باشد!")
        ],

    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "رمز خود را وارد کنید"}),
        label=False
    )


class Register(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "نام"}),
        label=False
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "نام خانوادگی"})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "نام کاربری"}),
        label=False,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "ایمیل"}),
        label=False,
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "رمز"}), label=False)

    re_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "تایید رمز"}), label=False)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_ext = ["gmail.com", "yahoo.com"]
        if email.split("@", 1)[1] not in email_ext:
            raise forms.ValidationError("ایمیل معتبر نیست")
        existence = User.objects.filter(email=email).exists()
        if existence:
            raise forms.ValidationError("این ایمیل دارای اکانت است")

        return email

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("تایید رمز یکسان وارد نشده است! ")

        return password
