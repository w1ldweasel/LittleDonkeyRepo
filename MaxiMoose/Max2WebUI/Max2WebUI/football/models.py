from django.db import models

class Match(models.Model):
    summary = models.TextField()
    date = models.DateTimeField('Match date')
    home_team = models.ManyToManyField('Team', related_name='away_team')
    home_goals = models.IntegerField(default=0)
    away_team = models.ManyToManyField('Team', related_name='home_team')
    away_goals = models.IntegerField(default=0)
        
        
class Team(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name