# Generated by Django 4.1.7 on 2023-02-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=200)),
                ('e_desc', models.CharField(max_length=500, null=True)),
                ('type', models.CharField(choices=[('1', 'ONLINE'), ('2', 'OFFLINE')], default=2, max_length=10)),
                ('start_date', models.DateField(blank=True, verbose_name='startdate(mm/dd/yyyy)')),
                ('end_date', models.DateField(blank=True, verbose_name='enddate(mm/dd/yyyy)')),
                ('nature', models.CharField(choices=[('1', 'PERMANENT'), ('2', 'TEMPORARY')], default=2, max_length=10)),
                ('noofvolunteers', models.IntegerField()),
                ('ngo_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.ngomodel')),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.volunteermodel')),
            ],
        ),
    ]
