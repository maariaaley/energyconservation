from django.db import models
# model for Landlord
class Landlord(models.Model):
    first_name = models.CharField(max_length=80, default='Maria')
    last_name = models.CharField(max_length=80, default='Aley')
    phone_number = models.IntegerField()
    email = models.EmailField(default='maria@gmail.com')

