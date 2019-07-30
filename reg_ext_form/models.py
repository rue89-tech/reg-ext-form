# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    subscribe_to_news_updates = models.BooleanField(
        "Je souhaite être informé-e de l'actualité de Rue89/l'Obs et de la parution de ses futures MOOCs",
        blank=True,
        default=False
    )
    accept_terms_of_use_of_personal_data = models.BooleanField(
        "j'accepte les conditions d'utilisation des données personnelles"
    )
    accept_privacy_policy = models.BooleanField(
        "J’accepte la politique de confidentialité de Rue89 MOOC"
    )
