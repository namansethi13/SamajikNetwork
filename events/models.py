import uuid
from django.db import models
from accounts.models import NGO,Volunteer
CHOICES = [
        ('1', 'ONLINE'),
        ('2', 'OFFLINE'),
        ]

# Create your models here.
class events(models.Model):
    e_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    e_name = models.CharField(max_length=200)
    type=models.CharField(
        max_length=10,
        choices=CHOICES,
        default=2
    )
    start_date=models.DateField("startdate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    end_date=models.DateField("enddate(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)
    nature = models.CharField(max_length=200)
    noofvolunteers = models.IntegerField()
    id = models.ForeignKey(NGO,on_delete=models.CASCADE)
    
class volunteer_event():
    event_id =models.ForeignKey(events,on_delete=models.CASCADE)
    id = models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    hours=models.IntegerField()

    
