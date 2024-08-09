from django.db import models

class Player(models.Model):
    first_visit = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=255, null=True)
    IP = models.CharField(max_length=100)
    latitude = models.FloatField()
    points = models.PositiveSmallIntegerField()
    longitude = models.FloatField()

class Game(models.Model):
    played_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)