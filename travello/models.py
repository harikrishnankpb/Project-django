from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    price=models.IntegerField()
    path=models.ImageField(upload_to='pics')
    soffer=models.BooleanField(default=False)