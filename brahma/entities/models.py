import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.timezone import now
from datetime import date
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


MEMBERSHIP_CHOICES = [
    # Translators: Ezek a tagsági formák nevei
    ("sup", _("Supporter")),
    ("vol", _("Volunteer")),
    ("lead", _("Leader")),
    ("admin", _("Administrator")),
]

COMM_STATUS_CHOICES = [
    # Translators: Ezek a közösségek lehetséges státuszai
    ("init", _("Initial")),
    ("open", _("Open to new members")),
    ("closed_temp", _("Temporarily closed")),
    ("closed", _("Closed")),
    ("ceased", _("Ceased")),
]

LOCATION_CAT_CHOICES = [
    # Translators: Ezek a helyszínek kategória nevei
    ("farm", _("Farm")),
    ("commgard", _("Community garden")),
    ("commhub", _("Community hub")),
    ("park", _("Park")),
    ("venue", _("Public venue")),
]

OTHER_ENTITY_CAT_CHOICES = [
    ("org", _("Organization")),
    ("comm_ent", _("Community Enterprise")),
    ("other", _("Other")),
]


class EntityUserManager(BaseUserManager):
    pass


class BaseEntity(models.Model):
    """Abstract class for all entities that represent a person/identity"""
    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    phone = models.CharField(_("Phone"), blank=True, max_length=15)  # TODO: regexvalidator
    hometown = models.CharField(_("Location of residency"), blank=True, max_length=255)
    avatar_photo = models.ImageField(blank=True)
    intro = models.CharField(_("Introduction"), blank=True, max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name or f"{self._meta.verbose_name} {self.pk}"



class User(BaseEntity, AbstractUser):
    """A rendszert használó összes természetes személy (tartalmazza a hozzáférést is)"""
    class Meta:
        verbose_name = _("User")

    email = models.EmailField(_("email address"), blank=True, unique=True)

    def __str__(self) -> str:
        disp_name = self.username

        if self.first_name and self.last_name:
            disp_name = f"{self.last_name} {self.first_name}"  # TODO: int'l names
            if self.name: disp_name += f" ({self.name})"
        
        return disp_name

    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.pk})


class CommunityMembership(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    member =  models.ForeignKey('User', on_delete=models.CASCADE)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default="sup", max_length=64)  # TODO
    member_since = models.DateTimeField(auto_now_add=True)


class Community(BaseEntity):
    """Közösségek..."""
    class Meta:
        verbose_name = _("Community")

    slug = models.SlugField(unique=True)
    location = models.CharField(blank=True, max_length=255)  # TODO: geodjango geometryfield?
    members = models.ManyToManyField('User', through='CommunityMembership')
    founded = models.DateField(_("Date of foundation"), default=date.today)
    status = models.CharField(choices=COMM_STATUS_CHOICES, default="init", max_length=64)  # TODO

    def get_absolute_url(self):
        return reverse("community", kwargs={"slug": self.slug})
    
    def get_memberships(self):
        return CommunityMembership.objects.filter(community=self)


class CommunityEnterprise(BaseEntity):
    """Közösségi vállalkozások"""
    class Meta:
        verbose_name = _("Community Enterprise")



class Location(BaseEntity):
    """Közösségek szempontjából lényeges földrajzi helyek (közösségi terek, tanyák, stb.)"""
    class Meta:
        verbose_name = _("Location")

    category = models.CharField(_("Category"), choices=LOCATION_CAT_CHOICES, max_length=255)  # TODO
    location = None  # TODO: geodjango geometryfield?


class OtherEntity(BaseEntity):
    """Egyéb, közösségek szempontjából lényeges entitások (intézmények, portálok, vállalkozások, személyek, stb.)"""
    class Meta:
        verbose_name = _("Other Entity")

    category = models.CharField(_("Category"), choices=OTHER_ENTITY_CAT_CHOICES, max_length=64)  # TODO
    admins = models.ManyToManyField('User')


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey('User', default=User.objects.filter(is_superuser=True).first().pk, on_delete=models.DO_NOTHING)
    invitee = models.OneToOneField('User', related_name='own_invitation', blank=True, null=True, on_delete=models.DO_NOTHING)
    email = models.EmailField(unique=True)


# TODO: követések: User -> [Community, User, OtherEntity]
