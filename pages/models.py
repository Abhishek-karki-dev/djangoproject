from django.db import models
from django.shortcuts import redirect

# Create your models here.
class Property(models.Model):
    Property_type = [
        ('A',"Apartment"),
        ('H',"House")
    ]
    title = models.CharField(max_length=200, verbose_name="Property Name")
    description = models.TextField(blank=True)
    location = models.CharField(max_length=150, blank=True)
    price = models.FloatField(default=0.0)
    area = models.FloatField(default=0.0, help_text="Enter area in sq. ft")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    proptery_type = models.CharField(max_length=1, choices = Property_type)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return redirect('home')