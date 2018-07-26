from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Team,Match,Scored

from .scoreutils import get_scores
from .twitter_functions import get_tweets

from datetime import datetime, date
from pytz import timezone

from .forms import search_team_form


def index(request):
    tz = timezone('America/New_York')
    right_now = datetime.now(tz)
    today_date = date(right_now.year, right_now.month, right_now.day)

    today_matches = Match.objects.filter(date = today_date)
    return render(request, 'index.html',{'match_query':today_matches})


def history(request):
    return render(request, 'history.html')


def contact(request):
    return render(request, 'contact.html')


def scores(request):
    score_list = get_scores()
    score_list1 = []
    if score_list != None:
        for item in score_list:
            lteam = Team.objects.get(pk = item['leftplayer'])
            rteam = Team.objects.get(pk = item['rightplayer'])

            curr_match = Match.objects.get(LeftTeam = lteam, RightTeam = rteam, date = datetime.now().date())

            scored = Scored.objects.get(match = curr_match)
            scores_dict = {
                'lteam': lteam,
                'rteam': rteam,
                'curr_match': curr_match,
                'score': scored,
                'minute': item['minute']
            }

            score_list1.append(scores_dict)
    return render(request, 'scores.html', {'score_list':score_list1 })

def twitterfeed(request):
    tweetList = get_tweets('world cup')
    #return HttpResponse(str(tweetList))
    return render(request, 'twitter.html', {'tweet_list': tweetList})

def search_team(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = search_team_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            team = form.cleaned_data['team']
            team_query = None
            try:
                team_query =  Team.objects.get(pk = str(team))
            except ObjectDoesNotExist:
                raise Http404("Team is not playing in the World Cup")

            return render(request, 'team.html', {'team_query': team_query})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = search_team_form()

    return render(request, 'team_search.html', {'form': form})
