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
        self.fields['accept_privacy_policy'].required = True

    class Meta:
        model = ExtraInfo
        fields = ('subscribe_to_news_updates', 'accept_terms_of_use_of_personal_data', 'accept_privacy_policy')
        labels = {
            'subscribe_to_news_updates': ("Je souhaite être informé-e de l'actualité de Rue89/l'Obs et de "
                                          "la parution de ses futures MOOCs"),
            'accept_terms_of_use_of_personal_data': mark_safe(
                """j'accepte les <a href="{}">conditions d'utilisation des données personnelles</a>""".format(
                    reverse_lazy('tos')
                )
            ),
            'accept_privacy_policy': mark_safe(
                """J’accepte la <a href="{}">politique de confidentialité</a> de Rue89 MOOC""".format(
                    reverse_lazy('privacy')
                )
            ),
        }
