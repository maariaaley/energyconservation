from django.db import models
from users.models import Landlord
# Model for room
class Room(models.Model):
    address = models.CharField(default='12345678', max_length=30)
    room_number = models.IntegerField()
    square_meters = models.IntegerField()
    windows = models.IntegerField()
    is_insulated = models.BooleanField(default=False)
    is_normal = models.BooleanField(default=False)
    has_bathroom = models.BooleanField(default=False)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)