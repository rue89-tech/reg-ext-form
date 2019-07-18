# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from .models import ExtraInfo


class ExtraInfoForm(ModelForm):
    """
    The fields in this form are derived from the ExtraInfo model in models.py
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['accept_terms_of_use_of_personal_data'].required = True

    class Meta:
        model = ExtraInfo
        fields = ('accept_terms_of_use_of_personal_data', )
        labels = {
            'accept_terms_of_use_of_personal_data': mark_safe(
                u"""j'accepte les <a href="{}">conditions d'utilisation des données personnelles</a>""".format(
                    reverse_lazy('tos')
                )
            )
        }
