from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex.: Mike'
        })
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex.: Olson'
            }
        )
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your user'
        })
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email'
        })
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password'
        }),
        error_messages={
            'required': 'The field must not be empty'
        },
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password'
            }
        ),
        error_messages={
            'required': 'The field must not be empty'
        }
    )


    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')

        # error_messages = {
        #     'username': {'required':'This field is Requerid'},
        #     'password': {'required': 'This field is Requerid'}
        # }


    #Validando campos especificos do formulário
    def clean_password(self):
        #pegando o valor do campo
        data = self.cleaned_data.get('password')

        #validando se existe a palavra especifica no password como teste
        if 'Atenção' in data:
            raise ValidationError(
                'Você não pode digita a palvra %(aleatorio)s no campo password',
                code='invalid',
                params={'aleatorio': 'Atenção'}
                )

        return data
    
    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')

        if 'Ricardo' in data:
            raise ValidationError(
                'Você não pode digitar o nome %(primeiro_nome)s',
                code='invalid',
                params={'primeiro_nome': 'Ricardo'}
            )

        return data
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                #definido o campo em que irá aparecer o error
                'password':'Password and password2 must be equal',
                'password2':'Password and password2 must be equal',
        })