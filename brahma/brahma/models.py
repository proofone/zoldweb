from django.contrib.auth.models import AbstractUser
from django.db import models


MEMBERSHIP_CHOICES = [
    ("sup", "Supporter"),
    ("vol", "Volunteer"),
    ("lead", "Leader"),
]


class BaseEntity(models.Model):
    """Abstract class for all entities that represent a person/identity"""
    class Meta:
        abstract = True

    phone = models.CharField(blank=True, max_length=15)  # TODO: regexvalidator
    hometown = models.CharField(blank=True, max_length=255, verbose_name="Tartózkodási hely")
    avatar_photo = models.ImageField(blank=True)
    intro = models.CharField(blank=True, max_length=512)



class User(BaseEntity, AbstractUser):
    """A rendszert használó összes természetes személy (tartalmazza a hozzáférést is)"""
    class Meta:
        verbose_name = "User"


class CommunityMembership(models.Model):
    community = models.ForeignKey('Community', on_delete=models.CASCADE)
    member =  models.ForeignKey('User', on_delete=models.CASCADE)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=64)  # TODO
    member_since = models.DateTimeField(auto_now_add=True)


class Community(BaseEntity):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    location = models.CharField(blank=True, max_length=255)
    members = models.ManyToManyField('User', through='CommunityMembership')
    avatar_photo = models.ImageField(blank=True)
    founded = models.DateField(auto_now_add=True)
    intro = models.CharField(blank=True, max_length=512)


class Location(models.Model):
    """Közösségek szempontjából lényeges földrajzi helyek (közösségi terek, tanyák, stb.)"""
    name = models.CharField(max_length=255)
    category = models.CharField(choices=[], max_length=255)  # TODO
    avatar_photo = models.ImageField(blank=True)
    location = None  # TODO: geodjango geometryfield?


class OtherEntity(BaseEntity):
    """Egyéb, közösségek szempontjából lényeges entitások (intézmények, portálok, vállalkozások, személyek, stb.)"""
    pass


# TODO: követések: User -> [Community, User, OtherEntity]