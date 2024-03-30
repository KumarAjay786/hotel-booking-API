from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.hotel.name} - Room {self.number}"

# Create your models here.
