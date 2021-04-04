from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    result = models.CharField(max_length=120)
    docname = models.CharField(max_length=12)
    meds = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.fname

class User(models.Model):
    first_name = models.CharField( max_length=50)
    username = models.CharField( max_length=20)
    email = models.EmailField( max_length=120)
    password = models.CharField(max_length=50)
