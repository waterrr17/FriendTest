from django.db import models


# Create your models here.

class Player(models.Model):
    is_host = models.BooleanField()
    name = models.CharField(max_length=30)
    player_number = models.IntegerField()
    current_guess=models.IntegerField(default=0)
    score=models.IntegerField(default=0)
    question1 = models.BooleanField(default=False)
    question2 = models.BooleanField(default=False)
    question3 = models.BooleanField(default=False)
    question4 = models.BooleanField(default=False)
    question5 = models.BooleanField(default=False)
    question6 = models.BooleanField(default=False)
    question7 = models.BooleanField(default=False)
    question8 = models.BooleanField(default=False)
    question9 = models.BooleanField(default=False)
    question10 = models.BooleanField(default=False)
