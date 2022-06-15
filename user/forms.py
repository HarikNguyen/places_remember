from django import forms
from .models import UserWithAvatar, User
from django.core.files.images import get_image_dimensions

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-type Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def clean_password2(self):
        cleanedData = self.cleaned_data
        if cleanedData['password'] != cleanedData['password2']:
            raise forms.ValidationError('Password don\'t match')
        return cleanedData['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserEditAvatarForm(forms.ModelForm):
    class Meta:
        model = UserWithAvatar
        fields = ('avatar',)