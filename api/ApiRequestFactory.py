import requests
import json
import time

from domain.Player import Player
from domain.Team import Team


class ApiRequestFactory:

    def __init__(self):
        self.players = []
        self.teams = []

    def get_players(self):
        if not self.players:
            players = []
            page = 1

            while page is not None:
                response = requests.get('https://www.balldontlie.io/api/v1/players?page=' + str(page) + '&per_page=100')

                data = response.json()['data']
                meta = response.json()['meta']

                meta_dump = json.dumps(meta)

                for e in data:
                    data_dump = json.dumps(e)

                    t = json.loads(data_dump)

                    team_dict = t.get('team')

                    team = Team(team_dict.get('id'), team_dict.get('abbreviation'), team_dict.get('city'),
                                team_dict.get('conference'), team_dict.get('division'), team_dict.get('full_name'),
                                team_dict.get('name'))

                    pl = Player(t.get('id'), t.get('first_name'), t.get('last_name'), t.get('height_feet'), t.get('height_inches'),
                                t.get('position'), team, t.get('weight_pounds'))

                    players.append(pl)

                time.sleep(1)
                page = json.loads(meta_dump).get('next_page')

            self.set_players(players)
            return players
        else:
            return self.players

    def set_players(self, players):
        self.players = players

    def get_teams(self):
        if not self.teams:
            teams = []
            page = 1

            while page is not None:
                response = requests.get('https://www.balldontlie.io/api/v1/teams')

                data = response.json()['data']
                meta = response.json()['meta']

                meta_dump = json.dumps(meta)

                for e in data:
                    dump = json.dumps(e)

                    t = json.loads(dump)

                    team = Team(t.get('id'), t.get('abbreviation'), t.get('city'),t.get('conference'), t.get('division'),
                                t.get('full_name'), t.get('name'))

                    teams.append(team)

                # we can only do 60 requests per minute, so sleep for a second after each request
                time.sleep(1)
                page = json.loads(meta_dump).get('next_page')

            self.set_teams(teams)
            return teams
        else:
            return self.teams

    def set_teams(self, teams):
        self.teams = teams
