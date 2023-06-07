from django.forms import ModelForm, TextInput, Textarea, Select, FileInput, EmailInput, PasswordInput
from .models import Category, Product
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "First name"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Last name",
            }),
            "username": TextInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Username",
                "aria-describedby": "addon-wrapping",
            }),
            "email": EmailInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "E-mail",
                "aria-describedby": "inputGroup-sizing-default",
            }),
            "password": PasswordInput(attrs={
                "class": "form-control text-bg-dark",
                "aria-label": "Password",
                "aria-describedby": "inputGroup-sizing-default",
            }),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            "title": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Категория",
            })
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image','title', 'description', 'price', 'category']
        widgets = {
            "image": FileInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "placeholder": "Изображение",
            }),
            "title": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Товар",
            }),
            "description": Textarea(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control form-control-dark",
                "type": "text",
                "placeholder": "Описание",
                "cols": "30",
                "rows": "10",
            }),
            "price": TextInput(attrs={
                "style": "margin: 20px; width: 1190px;",
                "class": "form-control",
                "placeholder": "Цена",
            }),
            'category': Select(attrs={
                "style": "margin: 20px; width: 1190px;",
                'class': 'form-control form-control-dark'
            }),
        }