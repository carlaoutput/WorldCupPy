from bs4 import BeautifulSoup
import requests
import os
import sys
import re
from datetime import datetime,date,time
from pytz import timezone

''' 
    System path for ubuntu server, ubuntu laptop, and windows laptop.
    Go to the directory where the this file is located and run the pwd linux command
    to show the file path. Insert the absolute path into sys.path.append if you are
    going to run this file locally.
'''
sys.path.append("/home/mauricio/Documents/python_class/WorldCupPy")
#sys.path.append("/mnt/c/Users/meec/Documents/pythonproj/python_soccer")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WorldCupPy.settings")

import django
django.setup()

from django.core.exceptions import ObjectDoesNotExist
from worldcup.models import Team,Match,Scored

def get_scores():
    worldcupRecords = getWorldCupRecords()

    minute_list = []
    rplayer_list = []
    lplayer_list = []
    scores_list = []

    # Parse information into seperate list
    for item in worldcupRecords:
        minute_list.append(item.find("div", class_="min").text.replace(" ","").replace("'", ""))
        lplayer_list.append(item.find("div", class_="ply tright name").text.replace(" ", ""))
        rplayer_list.append(item.find("div", class_="ply name").text.replace(" ", ""))
        scores_list.append(item.find("a").text.replace(" ", ""))

    returnScoreList = []
    # for every match that is currently playing append it to returnScoreList 
    for item in get_teams_gen(minute_list):
        score_dict = {
            "rightplayer": str(rplayer_list[item]),
            "leftplayer": str(lplayer_list[item]),
            str(lplayer_list[item]): scores_list[item].split("-")[0],
            str(rplayer_list[item]): scores_list[item].split("-")[1],
            "minute": str(minute_list[item])
        }
        returnScoreList.append(score_dict)
    
    # if no game is playing return none
    if len(returnScoreList) == 0:
        return None
    else:
        return returnScoreList
##------------------------------------------------------------###
def get_teams_gen(minute_list):
    i = 0
    while i < len(minute_list):
        if minute_list[i] != 'FT' and re.compile("[0-9][0-9]+:[0-9][0-9]+").match(minute_list[i]) == None:
            yield i
        i += 1
        
##----------------------------------------------------------###
def get_today_match():
    #Get valid world cup records 
    worldcupRecords = getWorldCupRecords()

    rplayer_list = []
    lplayer_list = []
    time_list = []

    for item in worldcupRecords:
        time_list.append(item.find("div", class_="min").text.replace(" ","").replace("'",""))
        lplayer_list.append(item.find("div", class_="ply tright name").text.replace(" ", ""))
        rplayer_list.append(item.find("div", class_="ply name").text.replace(" ",""))

    return rplayer_list, lplayer_list, time_list    


def getWorldCupRecords():
    #intializing beautiful soup for parsing
    pageText = requests.get("http://www.livescores.com").text
    soup = BeautifulSoup(pageText, 'html.parser')
    # get every row in the homepage and narrow down links to those that only pertain
    # to the worldcup
    worldcupRecords = soup.find_all("div", class_="row-gray")
    worldcupRecords = [item for item in worldcupRecords if item.find("a", href=re.compile("worldcup"))]
    return worldcupRecords

def insert_today_match():
    tz = timezone("America/New_York")
    log = open("log.txt", "a")
    right_now = datetime.now(tz)
    today_date = date(right_now.year, right_now.month, right_now.day)

    rplayer, lplayer, time_list = get_today_match()
    for index in range(len(rplayer)):
        right_team = None
        left_team = None
        
        # check if team exist, if not insert into database
        try:
            right_team =  Team.objects.get(pk = rplayer[index])
            left_team = Team.objects.get(pk = lplayer[index])
        except ObjectDoesNotExist:
            if right_team == None:
                right_team = Team(pk = rplayer[index])
                logstring = "right_team '" + rplayer[index] + "' does not exist. Inserting..."
                write_to_log(datetime.now(tz), "insert_today_match", logstring, log)
                right_team.save()

            
            if left_team == None:
                left_team = Team(pk = lplayer[index])
                logstring = "left_team '" + lplayer[index] + "' does not exist. Inserting..."
                write_to_log(datetime.now(tz), "insert_today_match", logstring, log)
                left_team.save()
        
        convert_time = None
        try:
            convert_time = datetime.strptime(time_list[index], "%H:%M")
        except BaseException:
            convert_time = time(0,0)
        print(convert_time)
        start_time = time(convert_time.hour, convert_time.minute)
        insert_match = Match(RightTeam = right_team, LeftTeam = left_team, date = today_date, startTime = start_time)
        insert_match.save()

        insert_score = Scored(match = insert_match)
        insert_score.save()

    log.close()

def check_for_new_score():
    tz = timezone("America/New_York")
    log = open("log.txt", "a")
    right_now = datetime.now(tz)
    today_date = date(right_now.year, right_now.month, right_now.day)

    scores_list = get_scores()

    if scores_list == None:
        return None
    
    for item in scores_list:
        try:
            right_team = Team.objects.get(pk = item['rightplayer'])
            left_team = Team.objects.get(pk = item['leftplayer'])
        except BaseException as e:
             write_to_log(datetime.now(tz), "check_for_new_score", str(e), log)

        try:
            current_match = Match.objects.get(LeftTeam = left_team, RightTeam = right_team, date = today_date)
        except BaseException as e:
            write_to_log(datetime.now(tz), "check_for_new_score", str(e), log)

        try:
            current_match_score = Scored.objects.get(match = current_match)
        except BaseException as e:
            write_to_log(datetime.now(tz), "check_for_new_score", str(e), log)

        if current_match_score.leftScore != item[left_team.teamName]:
            current_match_score.leftScore = int(item[left_team.teamName])
            left_team.totalGoals += 1
            left_team.save()
            current_match_score.save()

        if current_match_score.rightScore != item[right_team.teamName]:
            current_match_score.rightScore = int(item[right_team.teamName])
            right_team.totalGoals += 1
            right_team.save()
            current_match_score.save()

    log.close()

def write_to_log(stddate, function, logstring, log):
      print("{0} : function: {1}: \n\t{2}" .format(stddate.strftime("[ %m-%d-%Y ] %H:%M:%S"), function , logstring),file=log)

if __name__ == "__main__":
    if sys.argv[1] == "insert":
        insert_today_match()
    else:
        check_for_new_score()
