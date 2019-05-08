from django.db import models
from datetime import datetime, timedelta

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

class Touroku(models.Model):

    date = models.DateField(verbose_name='日時', blank=True, null=True)
    name = models.CharField(max_length=30)
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)
    eatout = models.BooleanField(default=True)
    drinking = models.BooleanField(default=True)
    workout = models.BooleanField(default=True)
    stretch = models.BooleanField(default=True)
    studying = models.BooleanField(default=True)
    awaketime = models.TimeField(default=default_start_time)
    asleeptime = models.TimeField(default=default_start_time)
    kenkobody = models.CharField(default=True,max_length=30)
    workcond = models.CharField(default=True,max_length=30)

    def __str__(self):
        return '<ID:'+str(self.id)+'>  名前:'+self.name
