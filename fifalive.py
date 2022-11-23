import json

with open('fifalive.json') as f:
    jsondata = json.load(f)


for game in jsondata['featuredEvents']:
    name = game['tournament']['name']
    home_team = game['homeTeam']['name']
    away_team = game['awayTeam']['name']
    home_score = game['homeScore']
    away_score = game['awayScore']
    description = game['status']['description']

    print(name)
    print(home_team, home_score, '-', away_score, away_team)
    print(description)