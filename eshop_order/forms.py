from django import forms
from django.core import validators


class UserOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput
    )

    count = forms.IntegerField(
        widget=forms.NumberInput,
        initial=1,
        validators=[validators.MinValueValidator(0)]
    )
