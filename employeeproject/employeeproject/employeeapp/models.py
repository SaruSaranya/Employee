from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    mobileno=models.IntegerField()
    designation=models.TextField()
    def __str__(self):
        return self.name

