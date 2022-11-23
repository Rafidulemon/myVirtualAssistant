import json

with open('footballfix.json') as f:
    jsondata = json.load(f)




for group in jsondata['standings']:
    groupName = group['name']
    print()
    print(groupName)
    for team in group['rows']:
        teamName = team['team']['name']
        position = team['position']
        matches = team['matches']
        wins = team['wins']
        losses = team['losses']
        draws = team['draws']
        points = team['points']

        print(position, ":", teamName, matches, wins, losses, draws, "Point-", points)
