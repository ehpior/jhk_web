from django.db import models

# Create your models here.
class Ddate(models.Model):
    pub_date = models.DateTimeField('published')
    def __str__(self):
        return str(self.pub_date).split(' ')[0]

class Ddiary(models.Model):
    ddate = models.ForeignKey(Ddate, on_delete = models.CASCADE)
    dtitle = models.CharField(max_length = 50)
    dcontent = models.TextField()

    def __str__(self):
        return self.dtitle