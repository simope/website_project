from django.db import models

class Player(models.Model):
    first_visit = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=255, null=True)
    IP = models.CharField(max_length=100)
    latitude = models.FloatField()
    points = models.PositiveSmallIntegerField()
    longitude = models.FloatField()
    
    def __str__(self):
        return f"{self.IP}"

class Game(models.Model):
    result = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.result}"