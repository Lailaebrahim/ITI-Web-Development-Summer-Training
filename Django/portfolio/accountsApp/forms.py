from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PortfolioUser
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = PortfolioUser.objects.create(user=user)
        return user

class PortfolioUserForm(forms.ModelForm): 
    class Meta:
        model = PortfolioUser
        fields = ['jobTitle', 'bio', 'image']
       
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    portfolio_image = forms.ImageField()
    bio = forms.CharField(max_length=300, required=False)
    jobTitle = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                self.fields['portfolio_image'].initial = self.instance.portfolio_user.image
                self.fields['bio'].initial = self.instance.portfolio_user.bio
                self.fields['jobTitle'].initial = self.instance.portfolio_user.jobTitle
            except PortfolioUser.DoesNotExist:
                pass

    def save(self, commit=True):
        user = super().save(commit=commit)
        portfolio_user, _ = PortfolioUser.objects.get_or_create(user=user)
        portfolio_user.image = self.cleaned_data['portfolio_image']
        portfolio_user.bio = self.cleaned_data['bio']
        portfolio_user.jobTitle = self.cleaned_data['jobTitle']
        if commit:
            portfolio_user.save()
        return user
    
    