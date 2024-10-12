from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class open_mic(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True, null=True)
    ig_link = models.CharField(max_length=100, blank=True, null=True)
    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'

    WEEKDAY_CHOICES = [
        (Monday, 'Monday'),
        (Tuesday, 'Tuesday'),
        (Wednesday, 'Wednesday'),
        (Thursday, 'Thursday'),
        (Friday, 'Friday'),
        (Saturday, 'Saturday'),
        (Sunday, 'Sunday'),

    ]
    
    weekday = models.CharField(
        max_length=10,
        choices=WEEKDAY_CHOICES,
        default=Monday,
    )

    frequency = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    notes = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name

    
