from django.db import models

INTEREST_CHOICES = (
    ('animals', 'Animals'),
    ('arts_culture', 'Arts and Culture'),
    ('children', 'Children'),
    ('disaster_relief', 'Disaster Relief'),
    ('education', 'Education'),
    ('environment', 'Environment'),
    ('health', 'Health'),
    ('human_rights', 'Human Rights'),
    ('poverty', 'Poverty'),
    ('seniors', 'Seniors'),
    ('sports', 'Sports'),
    ('women', 'Women'),
    ('other', 'Other'),
)

CAUSE_CHOICES = (
    ('animals', 'Animals'),
    ('arts_culture', 'Arts and Culture'),
    ('children', 'Children'),
    ('disaster_relief', 'Disaster Relief'),
    ('education', 'Education'),
    ('environment', 'Environment'),
    ('health', 'Health'),
    ('human_rights', 'Human Rights'),
    ('poverty', 'Poverty'),
    ('seniors', 'Seniors'),
    ('sports', 'Sports'),
    ('women', 'Women'),
    ('other', 'Other'),
)


class RoleType(models.TextChoices):
    NGO = "NGO", "Ngo"
    VOLUNTEER = "VOLUNTEER", "Volunteer"
    OTHER = "OTHER", "Other"

class ShortRoleType(models.TextChoices):
    NGO = "NGO", "Ngo"
    VOLUNTEER = "VOLUNTEER", "Volunteer"