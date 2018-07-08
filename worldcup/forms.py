from django import forms

class search_team_form(forms.Form):
    team = forms.CharField(label="Team: ", max_length = 20)