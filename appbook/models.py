from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    real_name = models.TextField()
    tz = models.CharField(max_length=50)
    

class ActivityPeriod(models.Model):
    user_pk = models.ForeignKey(User, related_name='tracks', on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    
    class Meta:
            unique_together = ['user_pk','start_time']
            ordering = ['start_time']

    def __str__(self):
        return str(self.user_pk)