from django import forms

from django import forms
from .models import *
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3, ReCaptchaV2Checkbox, ReCaptchaV2Invisible

class ORCForm(forms.Form):
     web_username = forms.CharField(max_length=100, required=True, error_messages={
        'required': 'Please enter a username.'
    })

class SigninForm(forms.Form):
    web_username = forms.CharField(max_length=100, required=True, error_messages={
        'required': 'Please enter a username.'
    })
    web_password = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={
        'required': 'Please enter a password.'
    }, )
    captcha = ReCaptchaField(widget=ReCaptchaV3, error_messages={
        'required': 'Your Captcha score not passed.'
    }, )

    def clean(self):
        cleaned_data = super().clean()
        web_username = cleaned_data.get("web_username")
        web_password = cleaned_data.get("web_password")
        # if not web_username:
        #     self.add_error("web_username", "Username is required.")

        # if not web_password:
        #     self.add_error("web_password", "Password is required.")

        if len(str(web_username)) < 2:
            self.add_error("web_username", 'Minimum 5 characters required')

        if len(str(web_password)) < 2:
            self.add_error("web_password", 'Minimum 10 characters required')

        # return self.cleaned_data

class SignUpForm(forms.Form):
    web_username = forms.CharField(max_length=100, required=True)
    web_email = forms.CharField(max_length=100, required=True)
    web_password = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)
    web_repassword = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def clean(self):
        cleaned_data = super().clean()
        web_username = cleaned_data.get("web_username")
        web_email = cleaned_data.get("web_email")
        web_password = cleaned_data.get("web_password")
        web_repassword = cleaned_data.get("web_repassword")
        
        if len(str(web_username)) < 4:
            self.add_error("web_username", 'Username Minimum 4 characters required')
      
        if len(str(web_email)) < 4:
            self.add_error("web_username", 'Email Minimum 4 characters required')
      
        if len(str(web_password)) < 4:
            self.add_error("web_username", 'Password Minimum 4 characters required')

        if len(str(web_repassword)) < 4:
            self.add_error("web_password", 'Repassword Minimum 4 characters required')
            
        if str(web_repassword) != str(web_repassword):
            self.add_error("web_password", 'Repassword and Password not equal')
            
            
        
