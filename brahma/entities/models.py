from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.timezone import now
from datetime import date
from django.urls import reverse


MEMBERSHIP_CHOICES = [
    ("sup", "Supporter"),
    ("vol", "Volunteer"),
    ("lead", "Leader"),
    ("admin", "Administrator"),
]

COMM_STATUS_CHOICES = [
    ("init", "Initial"),
    ("open", "Open to new members"),
    ("closed_temp", "Temporarily closed"),
    ("closed", "Closed"),
    ("ceased", "Ceased"),
]

LOCATION_CAT_CHOICES = [
    ("farm", "Farm"),
    ("commgard", "Community garden"),
    ("commhub", "Community hub"),
    ("park", "Park"),
    ("venue", "Public venue"),
]

OTHER_ENTITY_CAT_CHOICES = [
    ("org", "Organization"),
    ("other", "Other"),
]


class EntityUserManager(BaseUserManager):
    pass


class BaseEntity(models.Model):
    """Abstract class for all entities that represent a person/identity"""
    class Meta:
        abstract = True

    name = models.CharField(max_length=50)
    phone = models.CharField(blank=True, max_length=15)  # TODO: regexvalidator
    hometown = models.CharField(blank=True, max_length=255, verbose_name="Tartózkodási hely")
    avatar_photo = models.ImageField(blank=True)
    intro = models.CharField(blank=True, max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name or f"{self._meta.verbose_name} {self.pk}"



class User(BaseEntity, AbstractUser):
    """A rendszert használó összes természetes személy (tartalmazza a hozzáférést is)"""
    class Meta:
        verbose_name = "User"

    # email_verified = models.BooleanField(default=False)  # TODO: verification with random key

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
        verbose_name = "Community"

    slug = models.SlugField(unique=True)
    location = models.CharField(blank=True, max_length=255)  # TODO: geodjango geometryfield?
    members = models.ManyToManyField('User', through='CommunityMembership')
    founded = models.DateField(default=date.today)
    status = models.CharField(choices=COMM_STATUS_CHOICES, default="init", max_length=64)  # TODO

    def get_absolute_url(self):
        return reverse("community", kwargs={"slug": self.slug})
    
    def get_memberships(self):
        return CommunityMembership.objects.filter(community=self)


class CommunityEnterprise(BaseEntity):
    """Közösségi vállalkozások"""
    class Meta:
        verbose_name = "Community Enterprise"



class Location(BaseEntity):
    """Közösségek szempontjából lényeges földrajzi helyek (közösségi terek, tanyák, stb.)"""
    class Meta:
        verbose_name = "Location"

    category = models.CharField(choices=LOCATION_CAT_CHOICES, max_length=255)  # TODO
    location = None  # TODO: geodjango geometryfield?


class OtherEntity(BaseEntity):
    """Egyéb, közösségek szempontjából lényeges entitások (intézmények, portálok, vállalkozások, személyek, stb.)"""
    class Meta:
        verbose_name = "Other Entity"

    category = models.CharField(choices=OTHER_ENTITY_CAT_CHOICES, max_length=64)  # TODO
    admins = models.ManyToManyField('User')


# TODO: követések: User -> [Community, User, OtherEntity]
