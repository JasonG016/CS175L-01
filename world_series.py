#world_series
#Jason Galvao


with open("WorldSeriesWinners.txt", "r") as file:
    winners = file.read().splitlines()

while True:
    team_name = input("Enter the name of a team (or Quit to exit): ")
    if team_name == "Quit":
        print("Exiting out of World Series Directory. Goodbye!")
        break
    win_count = winners.count(team_name)
    print(f"The {team_name} won the world series {win_count} times between 1903 and 2009.")
