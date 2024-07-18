from django import forms
from django.contrib.auth.models import User

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

