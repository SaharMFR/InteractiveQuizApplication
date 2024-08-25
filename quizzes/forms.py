from django import forms
from .models import QuizzesUser
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class SignupForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = QuizzesUser
#         fields = ['username', 'email']
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.password = self.cleaned_data['password1']  # Store the plain password initially
#         if commit:
#             user.save()
#         return user
