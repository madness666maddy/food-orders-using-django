from django.db import models
from accounts.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    register_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    family_income = models.IntegerField()
    distance_km = models.FloatField()
    health_issue = models.BooleanField(default=False)
    parent_support = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
