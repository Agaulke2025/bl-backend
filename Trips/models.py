from django.db import models
from Users.models import User

class Trip (models.Model):
  date = models.DateField()
  location = models.CharField(max_length=50)
  groupCheckIn = models.TextField()
  forecast = models.TextField()
  avyProblems = models.TextField()
  advisory = models.TextField()
  conditions = models.TextField()
  review = models.TextField()
  observations = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
