from django.db import models

class DropoutPrediction(models.Model):
    # define fields here
    name = models.CharField(max_length=100)
    # etc.
