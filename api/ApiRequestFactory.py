import requests
import json
import time
import logging

from domain.Player import Player
from domain.Team import Team


class ApiRequestFactory:
    __instance = None

    def __init__(self):
        self.players = []
        self.teams = []

        logging.basicConfig(level=logging.INFO)

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

            logging.info('Receiving players from API')
            while page is not None:
                response = requests.get('https://www.balldontlie.io/api/v1/players?page=' + str(page) + '&per_page=100')

                result = self.__create_players_from_response(response)

                players.append(tuple((page, result[0])))
                page = result[1]

                time.sleep(1)

            self.set_players(players)
            return players
        else:
            logging.info('Receiving players from cache')
            return self.players

    def get_players_from_page(self, page):
        if not self.players or not (pg for pg in self.players if pg[0] == page):
            players = []

            response = requests.get('https://www.balldontlie.io/api/v1/players?page=' + str(page) + '&per_page=100')

            result = self.__create_players_from_response(response)

            players.append(tuple((page, result[0])))

            next_page = result[1]

            self.players.append(players)
            return players, next_page
        else:
            return (pg for pg in self.players if pg[0] == page), (pg[0] for pg in self.players if pg[0] == (page + 1))

    def set_players(self, players):
        self.players = players

    def get_teams(self):
        if not self.teams:
            teams = []
            page = 1

            logging.info('Receiving teams from API')
            while page is not None:
                response = requests.get('https://www.balldontlie.io/api/v1/teams')

                data = response.json()['data']
                meta = response.json()['meta']

                meta_dump = json.dumps(meta)

                for e in data:
                    team = Team(e.get('id'), e.get('abbreviation'), e.get('city'), e.get('conference'),
                                e.get('division'), e.get('full_name'), e.get('name'))

                    teams.append(team)

                # we can only do 60 requests per minute, so sleep for a second after each request
                time.sleep(1)
                page = json.loads(meta_dump).get('next_page')

            self.set_teams(teams)
            return teams
        else:
            logging.info('Receiving teams from cache')
            return self.teams

    def set_teams(self, teams):
        self.teams = teams

    @staticmethod
    def __create_players_from_response(response):
        players = []

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

        page = json.loads(meta_dump).get('next_page')

        return players, page
