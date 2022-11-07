import json

with open('football.json') as f:
    jsondata = json.load(f)

league = jsondata['events'][0]['tournament']['name']
home_team = jsondata['events'][0]['homeTeam']['name']
away_team = jsondata['events'][0]['awayTeam']['name']

home_score = jsondata['events'][0]['homeScore']['current']
away_score = jsondata['events'][0]['awayScore']['current']

print(home_team, home_score, '-', away_score, away_team)

# for game in jsondata['events']:
#     league = game['tournament']['name']
#     home_team = game['homeTeam']['name']
#     away_team = game['awayTeam']['name']
#     home_score = game['homeScore']['current']
#     away_score = game['awayScore']['current']
#     print(home_team, home_score, '-', away_score, away_team)