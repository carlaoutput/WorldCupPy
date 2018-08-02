import sys
import os
from datetime import date
from datetime import time
sys.path.append("/home/mauricio/Documents/python_class/python_project/WorldCupPy")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django
django.setup()

from worldcup.models import Team,Match,Scored

if __name__ == "__main__":
	if len(Team.objects.all()) != 0:
		Team.objects.all().delete()
	if len(Match.objects.all()) != 0:
		Match.objects.all().delete()

	if len(Scored.objects.all()) != 0:
		Scored.objects.all().delete()
	russia = Team(teamName = "Russia", isEliminated = True, totalGoals = 11)
	russia.save()
	arabia = Team(teamName = "Saudi Arabia", isEliminated = True, totalGoals = 2)
	arabia.save()
	egypt = Team(teamName = "Egypt", isEliminated = True, totalGoals = 2)
	egypt.save()
	uruguay = Team(teamName = "Uruguay", isEliminated = True, totalGoals = 7)
	uruguay.save()
	portugal = Team(teamName = "Portugal", isEliminated = True, totalGoals = 6)
	portugal.save()
	spain = Team(teamName = "Spain", isEliminated = True, totalGoals = 7)
	spain.save()
	morocco = Team(teamName = "Morocco", isEliminated = True, totalGoals = 2)
	morocco.save()
	iran = Team(teamName = "Iran", isEliminated = True, totalGoals = 2)
	iran.save()
	france = Team(teamName = "France", isEliminated = False, totalGoals = 14)
	france.save()
	australia = Team(teamName = "Australia", isEliminated = True, totalGoals = 2)
	australia.save()
	peru = Team(teamName = "Peru", isEliminated = True, totalGoals = 2)
	peru.save()
	denmark = Team(teamName = "Denmark", isEliminated = True, totalGoals = 3)
	denmark.save()
	argentina = Team(teamName = "Argentina", isEliminated = True, totalGoals = 6)
	argentina.save()
	iceland = Team(teamName = "Iceland", isEliminated = True, totalGoals = 2)
	iceland.save()
	croatia = Team(teamName = "Croatia", isEliminated = True, totalGoals = 14)
	croatia.save()
	nigeria = Team(teamName = "Nigeria", isEliminated = True, totalGoals = 3)
	nigeria.save()
	brazil = Team(teamName = "Brazil", isEliminated = True, totalGoals = 8)
	brazil.save()
	switzerland = Team(teamName = "Switzerland", isEliminated = True, totalGoals = 5)
	switzerland.save()
	rica = Team(teamName = "Costa Rica", isEliminated = True, totalGoals = 2)
	rica.save()
	serbia = Team(teamName = "Serbia", isEliminated = True, totalGoals = 2)
	serbia.save()
	germany = Team(teamName = "Germany", isEliminated = True, totalGoals = 2)
	germany.save()
	mexico = Team(teamName = "Mexico", isEliminated = True, totalGoals = 3)
	mexico.save()
	sweden = Team(teamName = "Sweden", isEliminated = True, totalGoals = 6)
	sweden.save()
	korea = Team(teamName = "South Korea", isEliminated = True, totalGoals = 3)
	korea.save()
	belgium = Team(teamName = "Belgium", isEliminated = True, totalGoals = 13)
	belgium.save()
	panama = Team(teamName = "Panama", isEliminated = True, totalGoals = 2)
	panama.save()
	tunisia = Team(teamName = "Tunisia", isEliminated = True, totalGoals = 5)
	tunisia.save()
	england = Team(teamName = "England", isEliminated = True, totalGoals = 10)
	england.save()
	poland = Team(teamName = "Poland", isEliminated = True, totalGoals = 2)
	poland.save()
	senegal = Team(teamName = "Senegal", isEliminated = True, totalGoals = 4)
	senegal.save()
	colombia = Team(teamName = "Colombia", isEliminated = True, totalGoals = 6)
	colombia.save()
	japan = Team(teamName = "Japan", isEliminated = True, totalGoals = 6)
	japan.save()



	match1 = Match(LeftTeam = russia ,RightTeam = arabia , date = date(2018, 6, 14), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 5, rightScore = 0)
	s.save()	

	match1 = Match(LeftTeam = egypt ,RightTeam = uruguay, date = date(2018, 6, 15), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam = morocco,RightTeam = iran, date = date(2018, 6, 15), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()	
	
	match1 = Match(LeftTeam = portugal,RightTeam = spain, date = date(2018, 6, 15), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 3, rightScore = 3)
	s.save()
	
	match1 = Match(LeftTeam =france,RightTeam = australia, date = date(2018, 6, 16), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 2, rightScore = 1)
	s.save()
	#AF

	match1 = Match(LeftTeam = argentina ,RightTeam = iceland, date = date(2018, 6, 16), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 1, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam = peru,RightTeam = denmark, date = date(2018, 6, 16), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()


	match1 = Match(LeftTeam =croatia,RightTeam = nigeria, date = date(2018, 6, 16), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 2, rightScore = 0)
	s.save()	

	match1 = Match(LeftTeam =rica,RightTeam = serbia, date = date(2018, 6, 17), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()	

	match1 = Match(LeftTeam = germany,RightTeam = mexico, date = date(2018, 6, 17), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()	

	match1 = Match(LeftTeam = brazil,RightTeam = switzerland, date = date(2018, 6, 17), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 1)
	s.save()


	match1 = Match(LeftTeam = sweden ,RightTeam = korea, date = date(2018, 6, 18), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 0)
	s.save()	

	
	match1 = Match(LeftTeam = belgium,RightTeam = panama, date = date(2018, 6, 18), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 3, rightScore = 0)
	s.save()	

	match1 = Match(LeftTeam = tunisia ,RightTeam = england, date = date(2018, 6, 18), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()	

	
	match1 = Match(LeftTeam = colombia,RightTeam = japan, date = date(2018, 6, 19), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()	
	
	match1 = Match(LeftTeam = poland,RightTeam = senegal, date = date(2018, 6, 19), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()	

	match1 = Match(LeftTeam = russia,RightTeam = egypt, date = date(2018, 6, 19), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 3, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam = portugal ,RightTeam = morocco, date = date(2018, 6,  20), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 0)
	s.save()

	match1 = Match(LeftTeam = uruguay ,RightTeam = arabia, date = date(2018, 6,  20), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 0)
	s.save()	

	match1 = Match(LeftTeam = iran ,RightTeam = spain, date = date(2018, 6,  20), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()
	

	match1 = Match(LeftTeam = denmark,RightTeam = australia, date = date(2018, 6,  21), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 1)
	s.save()


	match1 = Match(LeftTeam = france,RightTeam = peru, date = date(2018, 6,  21), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 0)
	s.save()	

	
	match1 = Match(LeftTeam = argentina,RightTeam = croatia, date = date(2018, 6,  21), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 3)
	s.save()	

	match1 = Match(LeftTeam = brazil,RightTeam = rica, date = date(2018, 6, 22), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 0)
	s.save()	

	
	match1 = Match(LeftTeam = nigeria ,RightTeam = rica, date = date(2018, 6, 22), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 0)
	s.save()	

	match1 = Match(LeftTeam = serbia,RightTeam = switzerland, date = date(2018, 6, 22), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()	
	
	match1 = Match(LeftTeam = belgium,RightTeam = tunisia, date = date(2018, 6, 23), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 5, rightScore = 2)
	s.save()	

	
	match1 = Match(LeftTeam = korea,RightTeam = mexico, date = date(2018, 6, 23), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()	

	match1 = Match(LeftTeam = germany ,RightTeam = sweden, date = date(2018, 6, 23), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 1)
	s.save()	

	match1 = Match(LeftTeam = england, RightTeam = panama, date = date(2018, 6, 24), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 6, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam = japan, RightTeam = senegal, date = date(2018, 6, 24), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 2)
	s.save()	

	
	match1 = Match(LeftTeam = poland, RightTeam = colombia, date = date(2018, 6, 24), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 0, rightScore = 3)
	s.save()

	match1 = Match(LeftTeam = uruguay, RightTeam = russia, date = date(2018, 6, 25), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 3, rightScore = 0)
	s.save()

	match1 = Match(LeftTeam = arabia, RightTeam = egypt, date = date(2018, 6, 25), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 1)
	s.save()
	
	match1 = Match(LeftTeam = spain, RightTeam = morocco, date = date(2018, 6, 25), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 2)
	s.save()	

	match1 = Match(LeftTeam = iran, RightTeam = portugal, date = date(2018, 6, 25), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam = australia, RightTeam = peru, date = date(2018, 6, 26), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = denmark, RightTeam = peru, date = date(2018, 6, 26), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 0)
	s.save()

	match1 = Match(LeftTeam = nigeria, RightTeam = argentina, date = date(2018, 6, 26), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()


	match1 = Match(LeftTeam = iceland, RightTeam = croatia , date = date(2018, 6, 26), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = korea, RightTeam =  germany, date = date(2018, 6, 27), startTime = time(18, 0, 0))
	match1.save()	
	s = Scored(match = match1, leftScore = 2, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = mexico, RightTeam = sweden, date = date(2018, 6, 27), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 3)
	s.save()

	match1 = Match(LeftTeam = serbia, RightTeam = brazil, date = date(2018, 6, 27), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 2)
	s.save()	

	match1 = Match(LeftTeam = switzerland, RightTeam = rica, date = date(2018, 6, 27), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 2)
	s.save()


	match1 = Match(LeftTeam = japan, RightTeam = poland, date = date(2018, 6, 28), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()
	
	match1 = Match(LeftTeam = senegal, RightTeam = colombia, date = date(2018, 6, 28), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()	

	match1 = Match(LeftTeam = panama, RightTeam = tunisia, date = date(2018, 6, 28), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()	

	match1 = Match(LeftTeam = england, RightTeam = belgium, date = date(2018, 6, 28), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 1)
	s.save()


	match1 = Match(LeftTeam = france ,RightTeam = argentina , date = date(2018, 6, 30), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 4, rightScore = 3)
	s.save()

	match1 = Match(LeftTeam = uruguay ,RightTeam = portugal, date = date(2018, 6, 30), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam = spain,RightTeam = russia, date = date(2018, 7, 1), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = croatia,RightTeam = denmark, date = date(2018, 7, 1), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 1)
	s.save()

	match1 = Match(LeftTeam =brazil,RightTeam = mexico, date = date(2018, 7, 2), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 0)
	s.save()

	match1 = Match(LeftTeam = belgium ,RightTeam = japan, date = date(2018, 7, 2), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 3, rightScore = 2)

	match1 = Match(LeftTeam = sweden,RightTeam = switzerland, date = date(2018, 7, 3), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 0)

	match1 = Match(LeftTeam =colombia,RightTeam = england, date = date(2018, 7, 3), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)

	match1 = Match(LeftTeam =uruguay,RightTeam = france, date = date(2018, 7, 6), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = brazil,RightTeam = belgium, date = date(2018, 7, 6), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = sweden,RightTeam = england, date = date(2018, 7, 7), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 0, rightScore = 2)
	s.save()

	match1 = Match(LeftTeam = russia ,RightTeam = croatia, date = date(2018, 7, 7), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 3)
	s.save()

	match1 = Match(LeftTeam = france,RightTeam = belgium, date = date(2018, 7, 10), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 1, rightScore = 0)
	s.save()

	match1 = Match(LeftTeam = croatia ,RightTeam = england, date = date(2018, 7, 11), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 1)
	s.save()


	match1 = Match(LeftTeam = belgium,RightTeam = england, date = date(2018, 7, 14), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 2, rightScore = 0)
	s.save()

	match1 = Match(LeftTeam = france,RightTeam = croatia, date = date(2018, 7, 15), startTime = time(18, 0, 0))
	match1.save()
	s = Scored(match = match1, leftScore = 4, rightScore = 2)
	s.save()
