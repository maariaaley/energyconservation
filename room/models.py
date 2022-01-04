from django.db import models
from users.models import Landlord, Student

# Model for room
class Room(models.Model):
    address = models.CharField(default='12345678', max_length=30)
    room_number = models.IntegerField(primary_key=True)
    square_meters = models.IntegerField()
    windows = models.IntegerField(null=True)
    is_insulated = models.BooleanField(default=False, null=True)
    has_bathroom = models.BooleanField(default=False, null=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
class Consumption(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    electricity = models.IntegerField()
    gas = models.IntegerField()
    water = models.IntegerField()
