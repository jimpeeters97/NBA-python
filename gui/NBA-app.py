import tkinter as tk

from api.ApiRequestFactory import ApiRequestFactory


def main():
    window = tk.Tk()

    window.title("NBA-python")

    players_button = tk.Button(window, text="Players", command=show_players)
    teams_button = tk.Button(window, text="Teams", command=show_teams)

    players_button.pack()
    teams_button.pack()
    window.mainloop()


def show_players():
    window = tk.Tk()

    window.title("NBA Players")

    players = ApiRequestFactory().get_players()

    for pl in players:
        first_name_lb = tk.Label(window, text=pl.first_name)
        last_name_lb = tk.Label(window, text=pl.last_name)
        position_lb = tk.Label(window, text=pl.position)

        first_name_lb.pack()
        last_name_lb.pack()
        position_lb.pack()

    window.mainloop()


def show_teams():
    window = tk.Tk()

    window.title("NBA Teams")

    teams = ApiRequestFactory().get_teams()

    for tm in teams:
        name_lb = tk.Label(window, text=tm.name)
        city_lb = tk.Label(window, text=tm.city)
        conference_lb = tk.Label(window, text=tm.conference)
        division_lb = tk.Label(window, text=tm.division)

        name_lb.pack()
        city_lb.pack()
        conference_lb.pack()
        division_lb.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
