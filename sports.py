import requests
import json
import pyttsx3
import pywhatkit

url_football = "https://api.sofascore.com/api/v1/sport/football/events/live"
url_cricket = "https://api.sofascore.com/api/v1/sport/cricket/events/live"
url_fix = "https://api.sofascore.com/api/v1/unique-tournament/16/season/41087/standings/total"
url_fifa = "https://api.sofascore.com/api/v1/unique-tournament/16/featured-events"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def football_live():
    try:
        payload = ""
        headers = {
            "authority": "api.sofascore.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "if-none-match": "W/^\^a9e4071357^^",
            "origin": "https://www.sofascore.com",
            "referer": "https://www.sofascore.com/",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

        response = requests.request("GET", url_football, data=payload, headers=headers)

        jsondata = json.loads(response.text)

        event = jsondata['events']
        if event == []:
            talk("Sorry Sir! There is no live match now")
            print("There is no live match now")

        else:
            talk("Showing football scores:")
            for game in jsondata['events']:
                league = game['tournament']['name']
                home_team = game['homeTeam']['name']
                away_team = game['awayTeam']['name']
                home_score = game['homeScore']['current']
                away_score = game['awayScore']['current']
                print(league, ': ', home_team, home_score, '-', away_score, away_team)
    except:
        pass

def cricket_live():
    try:
        payload = ""
        headers = {
            "authority": "api.sofascore.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "if-none-match": "W/^\^2872f28087^^",
            "origin": "https://www.sofascore.com",
            "referer": "https://www.sofascore.com/",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

        response = requests.request("GET", url_cricket, data=payload, headers=headers)

        jsondata = json.loads(response.text)
        event = jsondata['events']
        if event == []:
            talk("Sorry Sir! There is no live match now")
            print("There is no live match now")

        else:

            talk("Showing cricket scores:")

            for game in jsondata['events']:
                league = game['tournament']['name']
                home_team = game['homeTeam']['name']
                away_team = game['awayTeam']['name']
                home_score = game['homeScore']['innings']['inning1']['score']
                home_wicket = game['homeScore']['innings']['inning1']['wickets']
                home_over = game['homeScore']['innings']['inning1']['overs']
                home_in = home_team + ": " + str(home_score) + "/" + str(home_wicket) + "  " + "(" + str(home_over) + ")"

                inning = game['lastPeriod']
                print(league, ":")
                if inning == 'inning1':
                    print(home_in)
                    print(away_team)
                else:
                    print(home_in)
                    away_score = game['awayScore']['innings']['inning1']['score']
                    away_wicket = game['awayScore']['innings']['inning1']['wickets']
                    away_over = game['awayScore']['innings']['inning1']['overs']
                    away_in = away_team + ": " + str(away_score) + "/" + str(away_wicket) + "  " + "(" + str(away_over) + ")"
                    print(away_in)
    except:
        pass

def fixture():
    try:
        payload = ""
        headers = {
            "authority": "api.sofascore.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "if-none-match": "W/^\^d4dec7598d^^",
            "origin": "https://www.sofascore.com",
            "referer": "https://www.sofascore.com/",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

        response = requests.request("GET", url_fix, data=payload, headers=headers)
        jsondata = json.loads(response.text)

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
    except:
        pass

def fifaLive():
    try:
        payload = ""
        headers = {
            "authority": "api.sofascore.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "if-none-match": "W/^\^5188b3053d^^",
            "origin": "https://www.sofascore.com",
            "referer": "https://www.sofascore.com/",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

        response = requests.request("GET", url_fifa, data=payload, headers=headers)
        jsondata = json.loads(response.text)
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
            print()
    except:
        print("No match")

def score(command):
    if 'football score' in command:
        football_live()
    elif 'cricket score' in command:
        cricket_live()
    else:
        pywhatkit.search(command)



