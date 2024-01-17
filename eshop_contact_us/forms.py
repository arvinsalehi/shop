from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "نام و نام خانوادگی را وارد کنید", "class": "form-control"}),
        validators=[validators.MaxLengthValidator(150, "نام و نام خانوادگی باید کمتر ۱۵۰ کاراکتر باشد")],

    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "ایمیل خود را وارد کنید", "class": "form-control"}),
        validators=[validators.MaxLengthValidator(150, "ایمیل باید کمتر ۱۵۰ کاراکتر باشد")],
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "عنوان پیام خود را وارد کنید ", "class": "form-control"}),
        validators=[validators.MaxLengthValidator(150, "عنوان باید کمتر ۱۵۰ کاراکتر باشد")],
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "پبام خود را وارد کنید", "class": "form-control", "rows": "8"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_ext = ["gmail.com", "yahoo.com"]
        if email.split("@", 1)[1] not in email_ext:
            raise forms.ValidationError("ایمیل معتبر نیست")
        return email
