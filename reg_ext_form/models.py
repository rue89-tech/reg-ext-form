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
    accept_terms_of_use_of_personal_data = models.BooleanField(
        "j'accepte les conditions d'utilisation des données personnelles"
    )
