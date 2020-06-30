import tkinter as tk

from api.ApiRequestFactory import ApiRequestFactory

factory = ApiRequestFactory()


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

    players = factory.get_players()

    scroll = tk.Scrollbar(window)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(window, yscrollcommand=scroll.set)

    for pl in players:
        listbox.insert(tk.END, pl.first_name + " " + pl.last_name + ": " + pl.position)

    listbox.pack(side=tk.LEFT)

    scroll.config(command=listbox.yview)

    window.geometry("400x300")
    window.mainloop()


def show_teams():
    window = tk.Tk()

    window.title("NBA Teams")

    teams = factory.get_teams()

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
