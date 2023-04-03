#world_series
#Jason Galvao

with open("WorldSeriesWinners.txt", "r") as file:
    winners = file.read().splitlines()

win_counts = {}

for team in winners:
    if team in win_counts:
        win_counts[team] += 1
    else:
        win_counts[team] = 1

while True:
    team_name = input("Enter the name of a team (or Quit to exit): ")
    if team_name == "Quit":
        print("Exiting out of World Series Directory")
        break
    if team_name in win_counts:
        print(f"The {team_name} won the world series {win_counts[team_name]} times between 1903 and 2009.")
    else:
        print(f"The {team_name} did not win the world series between 1903 and 2009.")
