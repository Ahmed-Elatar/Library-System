from django.db import models

# Create your models here.

class users (models.Model):
    nid = models.CharField(max_length=14 )
    name = models.CharField(max_length=20)
    email = models.EmailField()
    passcode=models.CharField(max_length=20)


    def __str__(self):
        return self.name


class opinion (models.Model):
    name = models.CharField(max_length=20)
    faculty = models.CharField(max_length=30)
    subject=models.CharField(max_length=2000)


    def __str__(self):
        return self.name

