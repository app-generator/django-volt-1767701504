# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Contact(models.Model):

    #__Contact_FIELDS__
    vorname = models.CharField(max_length=255, null=True, blank=True)
    nachname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Contact_FIELDS__END

    class Meta:
        verbose_name        = _("Contact")
        verbose_name_plural = _("Contact")


class Contactlist(models.Model):

    #__Contactlist_FIELDS__
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)

    #__Contactlist_FIELDS__END

    class Meta:
        verbose_name        = _("Contactlist")
        verbose_name_plural = _("Contactlist")



#__MODELS__END
