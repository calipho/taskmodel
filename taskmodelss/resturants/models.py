from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    opening_time = models.TimeField(default='08:00:00')
    closing_time = models.TimeField(default='22:00:00')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
