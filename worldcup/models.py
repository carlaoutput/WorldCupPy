from django.db import models

class Team(models.Model):
    teamName = models.CharField(max_length=12, primary_key=True)
    isEliminated = models.BooleanField(default=False)
    totalGoals = models.IntegerField(default = 0)

    def __str__(self):
        return self.teamName

class Match(models.Model):
    RightTeam = models.ForeignKey(Team, related_name = "rightteam", on_delete = models.CASCADE )
    LeftTeam = models.ForeignKey(Team, related_name = "leftteam", on_delete = models.CASCADE ) 
    date = models.DateField()
    startTime = models.TimeField()

    def __str__(self):
        return "[ " + str(self.date) + " ] : " + str(self.LeftTeam.teamName) + " vs. " + str(self.RightTeam.teamName)

    '''Class Meta is similar to mysql Primary Key. unique_together states that Field RightTeam and LeftTeam, date  as Primary key'''
    class Meta:
        unique_together = (("RightTeam", "LeftTeam", "date"),)


class Scored(models.Model):
    match = models.ForeignKey(Match, on_delete = models.CASCADE)
    leftScore = models.IntegerField(default = 0)
    rightScore = models.IntegerField(default = 0)

    def __str__(self):
        return  str(self.match.LeftTeam.teamName) + " : "+ str(self.leftScore) +  "-" + str(self.rightScore) + " : " + self.match.RightTeam.teamName

    class Meta:
        unique_together = (("match"),)
# Create your models here.
