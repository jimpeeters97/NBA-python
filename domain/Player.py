from domain import Team


class Player:

    def __init__(self, id, first_name: str, last_name: str, height_feet: int, height_inches: int, position: str,
                 team: Team, weight_pounds: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.height_feet = height_feet
        self.height_inches = height_inches
        self.position = position
        self.team = team
        self.weight_pounds = weight_pounds

