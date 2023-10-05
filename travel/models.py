from django.db import models

class TravelRegion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    # You can add more fields as needed

    def __str__(self):
        return self.name
