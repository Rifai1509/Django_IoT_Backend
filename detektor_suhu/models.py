from django.db import models

# Create your models here.
class stats(models.Model):
    suhu = models.fields.FloatField()
    humidity = models.fields.FloatField()

    def __str__(self):
        return f'Temp = {self.suhu} dan humidity = {self.humidity}'
