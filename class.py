class Player:
    def __init__(self, player_name, player_id, current_location='base'):
        self.name = player_name
        self.id = player_id
        self.current_location = current_location
    def set_player_name(self,player_name):
        sql = f"INSERT INTO detective_game(detective_name) VALUES('{player_name}');"
        cursor = connection.cursor()
        cursor.execute(sql)
        return
    def get_detective_name(self,player_id):
        detective = f"SELECT detective_name FROM detective_game WHERE id = {player_id}"
        cursor = connection.cursor()
        cursor.execute(detective)
        result = cursor.fetchone()
        return result

    def get_player_location(self,player_id):
        sql = f"SELECT player_location FROM detective_game WHERE id = {player_id}"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def update_player_location(self,player_id,location):
        sql = f"UPDATE detective_game SET player_location = '{location}' WHERE id = {player_id}"
        cursor = connection.cursor()
        cursor.execute(sql)
        countries = cursor.fetchall()
        return countries
class Game:
    def __init__(self, player, limit=5):
        # one player object for every game object
        self.player = player
        self.player_id = player_id
        # how many Ricina can be disposed before player lose the game
        self.limit = limit
        # a list of country objects, randomly generated when game object created
        self.visited_location = countries
        # the last country object in visited_location
        self.crime_location = self.visited_location[-1]
        self.solved = 0
    def random_visit_location(self,limit):
        sql = "SELECT country_name FROM hints "
        sql += "ORDER BY RAND() "
        sql += "LIMIT " + limit
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                s = str(row[0])
                visited_locations.append(s)
        return
    def get_criminal_location(self,player_id):
        sql = f"SELECT crime_location FROM detective_game WHERE id = {player_id}"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]

    def update_crime_location(self,player_id, number):
        global criminal_escaped
        global visited_locations
        countries = get_countries()
        if len(visited_locations) == number:
            criminal_escaped = True
            return
        while len(visited_locations) - 1 < number:
            ran_num = random.randrange(0, number)
            if countries[ran_num] not in visited_locations:
                cursor = connection.cursor()
                visited_locations.append(countries[ran_num])
                update_query = f"UPDATE detective_game SET crime_location = '{countries[ran_num]}' WHERE id = {player_id}"
                cursor.execute(update_query)
                break

    def check_location_exist(self,answer):
        answer_check = answer.title()
        countries = get_countries()
        if answer_check in countries:
            return answer_check
        else:
            print(
                f"\nThis country is invalid! Check the countries available in:\n\t'Option 2: Display possible countries'")
            return
    def check_if_correct(self,player_id, location):
        global correct_visited_locations
        airport = get_airport(location)
        if location == visited_locations[correct_visited_locations + 1]:
            correct_visited_locations += 1
            print(
                f"\nYou solved the case and went to the correct country!\nYou are now in {airport}, {location},\none step closer to catch ContaMega Inc. Good job!")
            return True
        else:
            update_crime_location(player_id, 10)
            print(
                f"\nYour answer is wrong. One more box of Ricina is dropped by ContaMega.\nYou are now in {airport}, {location}.")
            return False

    def check_if_win_or_lose(self,player_id):
        global criminal_escaped
        global visited_locations
        global name
        crime_location = get_criminal_location(player_id)
        if visited_locations[correct_visited_locations] == crime_location:
            print(
                f"\nYou have caught ContaMega Inc. and saved the world, the R-code\nproject worked as expected and Ricina is being controlled by our\nenviromental services.\n\nWell done, detective {name}, you solved the case as we expected.")
            return True
        elif criminal_escaped:
            print(
                f"\nContaMega Inc. has released all the Ricina into the world.\nThe world is dying and we are hopeless. Maybe in another\nlife, detective {name}...")
            return True
        else:
            return None


class Country:
    def __init__(self, country_name):
        self.name = country_name
        self.hints = hints

    def get_hint_by_country(self,country_name):
        sql = f"SELECT hint FROM hints WHERE country_name = '{country_name}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        if cursor.rowcount > 0:
            for row in result:
                s = str(row)
                decoded_string = bytes(s, 'utf-8').decode('unicode-escape')
                print(decoded_string)
        return
    def get_countries(self):
        countries = "SELECT country_name FROM hints ORDER BY country_name ASC"
        cursor = connection.cursor()
        cursor.execute(countries)
        result = cursor.fetchall()
        countries = []
        for row in result:
            countries.append(row[0])
        return countries