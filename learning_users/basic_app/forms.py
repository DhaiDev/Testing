from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForms(forms.ModelForm):

    portfolio_site = forms.CharField(widget=forms.Textarea)
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

#change from
# class UserProfileInfoForms(forms.ModelForm):
#
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site','profile_pic')

# to

# class UserProfileInfoForms(forms.ModelForm):
#         portfolio_site = forms.CharField(widget=forms.Textarea)
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site','profile_pic')
