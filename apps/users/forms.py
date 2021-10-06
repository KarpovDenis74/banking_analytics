from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

User = get_user_model()


class CreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email", "captcha")


class FormUsersEdit(ModelForm):
    def clean_text(self):
        if self.cleaned_data['username'] is None:
            raise forms.ValidationError(
                'Пожалуйста, заполните это поле',
                params={'value': self.cleaned_data['username']},
            )
        return self.cleaned_data['username']

    class Meta:
        model = User
        fields = ["first_name",
                  "last_name",
                  "username",
                  "email",
                  "is_email_confirmed",
                  "is_staff",
                  "role",
                  "phone",
                  "communications"

                  ]
        labels = {
            'username': 'Ваш ник в системе'
        }
        help_texts = {
            'username': 'Ваш ник в системе',
            'email': 'Здесь Ваш email'
        }
