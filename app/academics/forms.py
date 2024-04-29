from django import forms
from academics.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password", "status"]
