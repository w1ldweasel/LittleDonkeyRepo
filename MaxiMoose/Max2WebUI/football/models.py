from django.db import models

class Match(models.Model):
    match_id = models.IntegerField(default=0)
    league_id = models.IntegerField(default=0)
    match_date = models.DateTimeField('Match date')
    match_hometeam_id = models.IntegerField(default=0)
    match_hometeam_name = models.CharField(max_length=50, verbose_name='Team Name', help_text='Home Team Name')
    match_hometeam_score = models.IntegerField(default=0)
    match_awayteam_id = models.IntegerField(default=0)
    match_awayteam_name = models.CharField(max_length=50, verbose_name='Team Name', help_text='Away Team Name')
    match_awayteam_score = models.IntegerField(default=0)
        
        
class Team(models.Model):
    team_name = models.CharField(max_length=50, verbose_name='Team Name', help_text='Team Name')
    team_key = models.IntegerField(default=0)
    def __str__(self):
        return self.team_name