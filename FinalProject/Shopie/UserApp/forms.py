import re
from django import forms
from django.contrib.auth.models import User
from .models import ShopieUser
from re import match


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    image = forms.ImageField(required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords didn't match!")
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'username already exists, try another one!')
        phone = cleaned_data.get('phone')
        if not match(r'\b01[0-9]{9}\b', phone):
            raise forms.ValidationError('Invalid phone number')

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        ShopieUser.objects.create(
            user=user,
            phone=self.cleaned_data['phone'],
            image=self.cleaned_data.get('image')
        )
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = ShopieUser
        fields = ['image', 'phone']

    username = forms.CharField(max_length=50, required=False)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['username'].initial = self.instance.user.username
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.exclude(pk=self.instance.user.pk).filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exists, try another one!')
        return username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.match(r'\b01[0-9]{9}\b', phone):
            raise forms.ValidationError('Invalid phone number')
        return phone

    def save(self, commit=True):
        shopieuser = super().save(commit=False)
        user = shopieuser.user

        if self.cleaned_data.get('username'):
            user.username = self.cleaned_data['username']
        if self.cleaned_data.get('first_name'):
            user.first_name = self.cleaned_data['first_name']
        if self.cleaned_data.get('last_name'):
            user.last_name = self.cleaned_data['last_name']
        if self.cleaned_data.get('email'):
            user.email = self.cleaned_data['email']

        if commit:
            user.save()
            shopieuser.save()

        return shopieuser
