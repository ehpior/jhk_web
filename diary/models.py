from django.db import models
import datetime

class Ddate(models.Model):
    pub_date = models.DateField('published')
    def __str__(self):
        return str(self.pub_date)

class Ddiary(models.Model):
    ddate = models.ForeignKey(Ddate, on_delete = models.CASCADE)
    dtitle = models.CharField(max_length = 50)
    dcontent = models.TextField()
    dtime = models.TimeField(default=datetime.time(hour=9))
    def __str__(self):
        return self.dtitle