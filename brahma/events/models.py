import uuid
from django.conf import settings
from entities.models import User, Location
from django.db import models
from django.utils.timezone import now
from datetime import date
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class EventSession(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(_("Phone"), blank=True, max_length=15)  # TODO: regexvalidator
    location = models.ForeignKey(Location, verbose_name=("Location"), on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField()
    holder = models.ManyToManyField(User, verbose_name=_("Session holder(s)"), related_name="+", blank=True)
    cam_operator = models.ForeignKey(User, verbose_name=_("Camera operator"), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

