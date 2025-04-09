from django.db import models
from django.db import models
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_new = models.IntegerField()

    def __str__(self):
        return self.name + " : " + self.course