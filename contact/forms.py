from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self):
        self.add_error(
            None,
            ValidationError(
                'Mensagem de error',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de error 2',
                code='invalid'
            )
        )
        return super().clean()
