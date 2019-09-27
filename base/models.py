from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    protocol = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=18, null=True)
    phone = models.CharField(max_length=10, null=True)
    active = models.BooleanField(default=True)
    pdf = models.FileField(upload_to='pdfs')

    def __str__(self):
        return str(self.id)
