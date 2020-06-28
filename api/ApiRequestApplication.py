import json
import requests
import time

from domain.Player import Player
from domain.Team import Team


def main():
    page = 1

    while page is not None:
        response = requests.get('https://www.balldontlie.io/api/v1/players?page=' + str(page) + '&per_page=100')

        data = response.json()['data']
        meta = response.json()['meta']

        meta_dump = json.dumps(meta)

        print(page)

        for e in data:
            dump = json.dumps(e)

            t = json.loads(dump)

            team_dict = t.get('team')

            team = Team(team_dict.get('id'), team_dict.get('abbreviation'), team_dict.get('city'),
                        team_dict.get('conference'), team_dict.get('division'), team_dict.get('full_name'),
                        team_dict.get('name'))

            pl = Player(t.get('id'), t.get('first_name'), t.get('last_name'), t.get('height_feet'),
                        t.get('height_inches'), t.get('position'), team, t.get('weight_pounds'))
            # print(pl.first_name)

        # we can only do 60 requests per minute, so sleep for a second after each request
        time.sleep(1)
        page = json.loads(meta_dump).get('next_page')


if __name__ == "__main__":
    main()
