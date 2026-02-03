import json

class HockeyStatsApplication:
    def __init__(self):
        self.players_data = []

    def _print_player_stats(self, player_data):
        """
        Prints a single player's statistics in the required format.
        Example: Leon Draisaitl       EDM  43 + 67 = 110
        Format:  {name:<21}{team:<3}  {goals:>2} + {assists:>2} = {points:>3}
        Name: 21 chars, left-justified
        Team: 3 chars, left-justified (starts at char 22)
        Goals: 2 chars, right-justified
        Assists: 2 chars, right-justified
        Points: 3 chars, right-justified
        '+' is the 30th char, '=' is the 35th char.
        """
        name = player_data['name']
        team = player_data['team']
        goals = player_data['goals']
        assists = player_data['assists']
        points = goals + assists
        # Format based on detailed analysis of sample output and constraints:
        # Name (chars 1-21), Team (chars 22-24)
        # Space (char 25), Goals (chars 26-27, right-justified in 2 spaces, so effectively chars 27-28 if goals are 2 digits)
        # Actually, it's: Name(21) Team(3) Space(1) Space(1) Goals(2) Space(1) '+'(1) Space(1) Assists(2) Space(1) '='(1) Space(1) Points(3)
        # This means: name(21)team(3)  goals(2) + assists(2) = points(3)
        print(f"{name:<21}{team:<3}  {goals:>2} + {assists:>2} = {points:>3}")

    def load_data(self):
        """
        Prompts for a filename, loads JSON data, and stores it.
        Prints the number of players read.
        """
        file_name = input("file name: ")
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                self.players_data = json.load(f)
            print(f"read the data of {len(self.players_data)} players")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            self.players_data = []
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{file_name}'.")
            self.players_data = []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.players_data = []


    def search_player(self):
        """
        Prompts for a player's name and prints their stats if found.
        """
        if not self.players_data:
            print("No data loaded.")
            return
        search_name = input("name: ")
        found = False
        for player in self.players_data:
            if player['name'] == search_name:
                self._print_player_stats(player)
                found = True
                break
        # If not found, the sample output shows nothing, so no "not found" message.

    def list_teams(self):
        """
        Lists all unique team abbreviations in alphabetical order.
        """
        if not self.players_data:
            print("No data loaded.")
            return
        teams = sorted(list(set(player['team'] for player in self.players_data)))
        for team in teams:
            print(team)

    def list_countries(self):
        """
        Lists all unique country abbreviations in alphabetical order.
        """
        if not self.players_data:
            print("No data loaded.")
            return
        countries = sorted(list(set(player['nationality'] for player in self.players_data)))
        for country in countries:
            print(country)

    def list_players_in_team(self):
        """
        Prompts for a team name and lists players in that team,
        ordered by points (descending).
        """
        if not self.players_data:
            print("No data loaded.")
            return
        team_name = input("team: ")
        team_players = [p for p in self.players_data if p['team'] == team_name]
        
        # Sort by points (goals + assists) descending
        sorted_players = sorted(team_players, key=lambda p: p['goals'] + p['assists'], reverse=True)
        
        for player in sorted_players:
            self._print_player_stats(player)

    def list_players_from_country(self):
        """
        Prompts for a country name and lists players from that country,
        ordered by points (descending).
        """
        if not self.players_data:
            print("No data loaded.")
            return
        country_name = input("country: ")
        country_players = [p for p in self.players_data if p['nationality'] == country_name]

        # Sort by points (goals + assists) descending
        sorted_players = sorted(country_players, key=lambda p: p['goals'] + p['assists'], reverse=True)
        
        for player in sorted_players:
            self._print_player_stats(player)

    def list_most_points(self):
        """
        Prompts for N and lists the top N players by points.
        Tie-breaker: higher number of goals.
        """
        if not self.players_data:
            print("No data loaded.")
            return
        try:
            how_many = int(input("how many: "))
            if how_many < 0:
                print("Number should be non-negative.")
                return
        except ValueError:
            print("Invalid number entered.")
            return

        # Sort by points (desc), then goals (desc)
        # Points = goals + assists
        # Primary key: points (descending), Secondary key: goals (descending)
        sorted_players = sorted(self.players_data,
                                key=lambda p: (p['goals'] + p['assists'], p['goals']),
                                reverse=True)
        
        for i in range(min(how_many, len(sorted_players))):
            self._print_player_stats(sorted_players[i])

    def list_most_goals(self):
        """
        Prompts for N and lists the top N players by goals.
        Tie-breaker: lower number of games played.
        """
        if not self.players_data:
            print("No data loaded.")
            return
        try:
            how_many = int(input("how many: "))
            if how_many < 0:
                print("Number should be non-negative.")
                return
        except ValueError:
            print("Invalid number entered.")
            return

        # Sort by goals (desc), then games played (asc)
        # Primary key: goals (descending), Secondary key: games (ascending)
        # To achieve this with a single key tuple for sorting: use (-goals, games)
        sorted_players = sorted(self.players_data,
                                key=lambda p: (-p['goals'], p['games']))
        
        for i in range(min(how_many, len(sorted_players))):
            self._print_player_stats(sorted_players[i])

    def run(self):
        """
        Main loop for the application.
        """
        self.load_data()
        if not self.players_data and not (self.players_data == [] and "File not found" in [True for handler in self.load_data.__closure__[0].cell_contents.__self__.handlers if "FileNotFoundError" in str(handler[0])]): # Check if data is empty due to actual empty file or error
             # This error check is a bit complex, simpler is just if not self.players_data after load
            if not self.players_data: # Simpler check: if loading failed or file was empty and resulted in no data
                # The problem description implies the program continues to the menu even if file load fails,
                # but operations would yield "No data loaded." or nothing.
                # For a better user experience, one might exit, but let's follow implicit behavior.
                pass


        while True:
            print() # Newline before commands menu, as in sample
            print("commands:")
            print("0 quit")
            print("1 search for player")
            print("2 teams")
            print("3 countries")
            print("4 players in team")
            print("5 players from country")
            print("6 most points")
            print("7 most goals")
            
            command = input("command: ")

            if command == '0':
                break
            elif command == '1':
                self.search_player()
            elif command == '2':
                self.list_teams()
            elif command == '3':
                self.list_countries()
            elif command == '4':
                self.list_players_in_team()
            elif command == '5':
                self.list_players_from_country()
            elif command == '6':
                self.list_most_points()
            elif command == '7':
                self.list_most_goals()
            else:
                # The sample output does not show an "unknown command" message.
                # Assuming valid inputs or that unrecognized commands should be ignored.
                pass 

if __name__ == "__main__":
    app = HockeyStatsApplication()
    app.run()
