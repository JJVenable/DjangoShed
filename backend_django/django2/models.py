from django.db import models

# Create your models here.
class Truck(models.Model):
  number = models.CharField(max_length=3, default="Not assigned")
  key = models.CharField(max_length=10)
  drivers = models.CharField(max_length=50)
  notes = models.TextField(blank=True, )

  def __str__(self):
    return self.number

class Job(models.Model):
  truck = models.ManyToManyField(
    Truck, related_name='jobs', blank=True  )
  suggested_tools = models.CharField(max_length=1000)
  address = models.TextField()
  scheduled = models.TextField()
  comments = models.TextField(blank=True, ) 
  job_number = models.TextField(default="Not specified")

  def __str__(self):
    return self.job_number


class Tool(models.Model):
  truck = models.ManyToManyField(
    Truck, related_name='tools', blank=True  )
  name = models.CharField(max_length=60)
  img = models.ImageField(null=True, blank=True, upload_to="images/")
  notes = models.TextField(blank=True, )

  def __str__(self):
    return self.name 