import uuid
from django.db import models
from accounts.models import BaseUser
from accounts.models import VolunteerModel,NGOModel
CHOICES = [
        ('1', 'ONLINE'),
        ('2', 'OFFLINE'),
        ]
Nature = [
        ('1', 'PERMANENT'),
        ('2', 'TEMPORARY'),
        ]
# Create your models here.


class events(models.Model):
    e_id = models.AutoField(primary_key=True),
    e_name = models.CharField(max_length=200)
    e_desc = models.CharField(max_length=500,null=True)
    type=models.CharField(
        max_length=10,
        choices=CHOICES,
        default=2
    )
    start_date=models.DateField("startdate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    end_date=models.DateField("enddate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    nature = models.CharField(
        max_length=10,
        choices=Nature,
        default=2
    )
    noofvolunteers = models.IntegerField()
    ngo_id = models.ForeignKey(NGOModel, null=True, default=None,on_delete=models.CASCADE)
    
class volunteer_event(models.Model):
    v_id = models.ForeignKey(VolunteerModel,on_delete=models.CASCADE)
    e_id =models.ForeignKey(events,on_delete=models.CASCADE)
    hours=models.IntegerField()


    
