# Generated by Django 4.1.7 on 2023-02-26 10:35

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='volunteer_profile_images/')),
                ('username', models.CharField(blank=True, editable=False, max_length=200, null=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('role', models.CharField(choices=[('NGO', 'Ngo'), ('VOLUNTEER', 'Volunteer'), ('OTHER', 'Other')], default='OTHER', max_length=9)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('interests', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('animals', 'Animals'), ('arts_culture', 'Arts and Culture'), ('children', 'Children'), ('disaster_relief', 'Disaster Relief'), ('education', 'Education'), ('environment', 'Environment'), ('health', 'Health'), ('human_rights', 'Human Rights'), ('poverty', 'Poverty'), ('seniors', 'Seniors'), ('sports', 'Sports'), ('women', 'Women'), ('other', 'Other')], max_length=200, null=True)),
                ('phone', models.IntegerField(max_length=12, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NGOModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Company Name')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('bio', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'NGOs',
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Last Name')),
                ('age', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='Age')),
                ('bio', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Volunteers',
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
    ]
