from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.timezone import now


MEMBERSHIP_CHOICES = [
    ("sup", "Supporter"),
    ("vol", "Volunteer"),
    ("lead", "Leader"),
]

COMM_STATUS_CHOICES = [
    ("init", "Initial"),
    ("open", "Open to new members"),
    ("closed", "Closed"),
    ("ceased", "Ceased"),
]

OTHER_ENTITY_CAT_CHOICES = [
    ("other", "Other"),
    # ("open", "Open to new members"),
]


class EntityUserManager(BaseUserManager):
    pass


class BaseEntity(models.Model):
    """Abstract class for all entities that represent a person/identity"""
    class Meta:
        abstract = True

    name = models.CharField(max_length=255)
    phone = models.CharField(blank=True, max_length=15)  # TODO: regexvalidator
    hometown = models.CharField(blank=True, max_length=255, verbose_name="Tartózkodási hely")
    avatar_photo = models.ImageField(blank=True)
    intro = models.CharField(blank=True, max_length=512)

    def __str__(self) -> str:
        return self.name or f"{self._meta.verbose_name} {self.pk}"



class User(BaseEntity, AbstractUser):
    """A rendszert használó összes természetes személy (tartalmazza a hozzáférést is)"""
    class Meta:
        verbose_name = "User"

    # email_verified = models.BooleanField(default=False)  # TODO: verification with random key

    # objects = EntityUserManager()
    
    def __str__(self) -> str:
        disp_name = self.username

        if self.first_name and self.last_name:
            disp_name = f"{self.last_name} {self.first_name}"  # TODO: int'l names
            if self.name: disp_name += f" ({self.name})"
        
        return disp_name


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
    founded = models.DateField(default=now())
    intro = models.CharField(blank=True, max_length=512)
    status = models.CharField(choices=COMM_STATUS_CHOICES, default="init", max_length=64)  # TODO

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("community", kwargs={"slug": self.slug})


class Location(BaseEntity):
    """Közösségek szempontjából lényeges földrajzi helyek (közösségi terek, tanyák, stb.)"""
    class Meta:
        verbose_name = "Location"

    category = models.CharField(choices=[], max_length=255)  # TODO
    location = None  # TODO: geodjango geometryfield?


class OtherEntity(BaseEntity):
    """Egyéb, közösségek szempontjából lényeges entitások (intézmények, portálok, vállalkozások, személyek, stb.)"""
    class Meta:
        verbose_name = "Other Entity"

    category = models.CharField(choices=OTHER_ENTITY_CAT_CHOICES, max_length=64)  # TODO


# TODO: követések: User -> [Community, User, OtherEntity]
