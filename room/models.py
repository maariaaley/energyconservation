from django.db import models
from landlord.models import Landlord

from student.models import Student
# Model for room
class Room(models.Model):
    address = models.CharField(max_lenght=80)
    room_number = models.IntegerField()
    square_meters = models.IntegerField()
    windows = models.IntegerField()
    insulated = models.BooleanField(default=True)
    bathroom = models.BooleanField(default=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)

