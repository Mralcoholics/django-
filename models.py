from django.db import models
class Doctor(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    specialist=models.CharField(max_length=100)
    def __str__(self):
        return self.FirstName
class Patient(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    address= models.CharField(max_length=100)
    def __str__(self):
        return self.FirstName

