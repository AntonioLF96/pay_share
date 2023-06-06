from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
        'code', 'password', 'email', 'fiscalCode', 'birthDate', 'birthPlace', 'residence', 'smartContractList',
        'extensions')
        widgets = {
            'password': forms.PasswordInput()  # rendi il campo password un campo di input di tipo password
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
