from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Team(models.Model):
    team_name=models.CharField(max_length=45)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

class Super(models.Model):
    real_name=models.CharField(max_length=45)
    code_name=models.CharField(max_length=45)
    is_good=models.BooleanField(True)
    team=models.ForeignKey(Team, related_name="supers",on_delete=DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
