import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,AbstractUser ,User
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from .managers import UserManager
from .choices import INTEREST_CHOICES,CAUSE_CHOICES,RoleType
from django.contrib.auth import get_user_model



class BaseUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_image = models.ImageField(upload_to="volunteer_profile_images/", null=True, blank=True)
    username = models.CharField(_("Username"), max_length=200, blank=True, null=True, editable=False)
    email = models.EmailField(_("email"), max_length=200, unique=True)
    role = models.CharField(max_length=9, choices=RoleType.choices, default=RoleType.OTHER)
    create_date = models.DateTimeField(auto_now_add=True)
    interests = MultiSelectField(choices=INTEREST_CHOICES,max_length=200, null=True, blank=True)
    phone = models.IntegerField(max_length=12, unique=True , null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    # REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return f"{self.username} {self.id}"

    def save(self, *args, **kwargs):
        self.username = str(self.email).split("@")[0]
        super(BaseUser, self).save(*args, **kwargs)\

BaseUser = get_user_model()


class NGOModel(BaseUser):
    """
    Custom Corporate Model
    """
    company_name = models.CharField(_('Company Name'), max_length=100, blank=True, null=True, unique=True)
    address = models.CharField(_('Address'), max_length=255, blank=True, null=True)
    website = models.URLField(_('Website'), max_length=255, blank=True, null=True)
    bio = models.CharField(_('Description'), max_length=1000, blank=True, null=True)
    
    def __str__(self) -> str:
        return  self.username

    class Meta:
        verbose_name_plural = 'NGOs'

class VolunteerModel(BaseUser):
    """
    Custom Corporate Model
    """
    first_name = models.CharField(_('First Name'), max_length=100, blank=True, null=True, unique=True)
    last_name = models.CharField(_('Last Name'), max_length=100, blank=True, null=True, unique=True)
    age = models.IntegerField(_('Age'), max_length=255, blank=True, null=True)
    bio = models.CharField(_('Description'), max_length=1000, blank=True, null=True)
    
    def __str__(self) -> str:
        return  self.username

    class Meta:
        verbose_name_plural = 'Volunteers'
# class Volunteer(models.Model):
#     user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE, related_name='%(class)s_related')
#     volunteer_profile_image = models.ImageField(upload_to="volunteer_profile_images/", null=True, blank=True)
#     volunteer_age = models.IntegerField()
#     volunteer_contact = models.IntegerField()
#     volunteer_bio = models.TextField(max_length=1000, null=True, blank=True)
#     volunteer_interests = MultiSelectField(choices=INTEREST_CHOICES,max_length=200, null=True, blank=True)
#     volunteer_ngo_id = models.IntegerField(null=True, blank=True)

# class NGO(models.Model):
#     user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE, related_name='%(class)s_related')
#     NGO_logo = models.ImageField(upload_to="ngo_logos/", null=True, blank=True)
#     NGO_address = models.CharField(max_length=500)
#     NGO_phone = models.IntegerField()
#     NGO_website = models.URLField(max_length=200)
#     NGO_socials = models.CharField(max_length=500)
#     NGO_bio = models.TextField(max_length=1000, null=True, blank=True)
#     NGO_causes = MultiSelectField(choices=CAUSE_CHOICES,max_length=200, null=True, blank=True)
#     NGO_no_of_employees = models.IntegerField()
