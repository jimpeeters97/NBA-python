import requests
import json
import time

from domain.Player import Player
from domain.Team import Team


class ApiRequestFactory:
    __instance = None

    def __init__(self):
        self.players = []
        self.teams = []

        if ApiRequestFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ApiRequestFactory.__instance = self

    @staticmethod
    def get_instance():
        if ApiRequestFactory.__instance is None:
            ApiRequestFactory()
        return ApiRequestFactory.__instance

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
                    team_dict = e.get('team')

                    team = Team(team_dict.get('id'), team_dict.get('abbreviation'), team_dict.get('city'),
                                team_dict.get('conference'), team_dict.get('division'), team_dict.get('full_name'),
                                team_dict.get('name'))

                    pl = Player(e.get('id'), e.get('first_name'), e.get('last_name'), e.get('height_feet'),
                                e.get('height_inches'), e.get('position'), team, e.get('weight_pounds'))

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
                    team = Team(e.get('id'), e.get('abbreviation'), e .get('city'), e.get('conference'),
                                e.get('division'), e.get('full_name'), e.get('name'))

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
