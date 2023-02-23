import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from .managers import UserManager
from .choices import INTEREST_CHOICES,CAUSE_CHOICES


class BaseUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("Username"), max_length=200, blank=True, null=True, editable=False)
    email = models.EmailField(_("email"), max_length=200, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    is_email_verified = models.BooleanField(_("Email Verified"), default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    # REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return f"{self.username} {self.id}"

    def save(self, *args, **kwargs):
        self.username = str(self.email).split("@")[0]
        super(BaseUser, self).save(*args, **kwargs)




class Volunteer(BaseUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="volunteer_profile_images/", null=True, blank=True)
    age = models.IntegerField()
    contact = models.IntegerField()
    bio = models.TextField(max_length=1000, null=True, blank=True)
    interests = MultiSelectField(choices=INTEREST_CHOICES,max_length=200, null=True, blank=True)
    ngo_id = models.IntegerField(null=True, blank=True)

class NGO(BaseUser):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="ngo_logos/", null=True, blank=True)
    address = models.CharField(max_length=500)
    phone = models.IntegerField()
    website = models.URLField(max_length=200)
    socials = models.CharField(max_length=500)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    causes = MultiSelectField(choices=CAUSE_CHOICES,max_length=200, null=True, blank=True)
    no_of_employees = models.IntegerField()
    achievements = models.IntegerField()



