import mysql.connector
import random

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="crime_game",
    user="root",
    password="123456",
    autocommit=True
)

name = ""
visited_locations = ["Base", ]
correct_visited_locations = 0
criminal_escaped = False
id = 0


def get_countries():
    countries = "SELECT country_name FROM hints ORDER BY country_name ASC"
    cursor = connection.cursor()
    cursor.execute(countries)
    result = cursor.fetchall()
    countries = []
    for row in result:
        countries.append(row[0])
    return countries

def get_airport(country):
    sql = "select name from airport, hints "
    sql += "where airport.iso_country = hints.iso_country "
    sql += "and type = 'large_airport' "
    sql += f"and country_name = '{country}'"
    sql += "ORDER BY RAND() limit 1;"
    cursor = connection.cursor()
    cursor.execute(sql)
    airport = cursor.fetchone()
    return airport[0]


def get_detective_name(player_id):
    detective = f"SELECT detective_name FROM detective_game WHERE id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(detective)
    result = cursor.fetchone()
    return result


def get_criminal_location(player_id):
    sql = f"SELECT crime_location FROM detective_game WHERE id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]


def get_player_location(player_id):
    sql = f"SELECT player_location FROM detective_game WHERE id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def get_hint_by_country(country):
    sql = f"SELECT hint FROM hints WHERE country_name = '{country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        for row in result:
            s = str(row)
            decoded_string = bytes(s, 'utf-8').decode('unicode-escape')
            print(decoded_string)
    return


def random_visit_location(quantity):
    sql = "SELECT country_name FROM hints "
    sql += "ORDER BY RAND() "
    sql += "LIMIT " + quantity
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            s = str(row[0])
            visited_locations.append(s)
    return


def update_player_location(player_id, location):
    sql = f"UPDATE detective_game SET player_location = '{location}' WHERE id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    countries = cursor.fetchall()
    return countries


def update_crime_location(player_id, number):
    global criminal_escaped
    global visited_locations
    countries = get_countries()
    if len(visited_locations) == number:
        criminal_escaped = True
        return
    while len(visited_locations)-1 < number:
        ran_num = random.randrange(0, number)
        if countries[ran_num] not in visited_locations:
            cursor = connection.cursor()
            visited_locations.append(countries[ran_num])
            update_query = f"UPDATE detective_game SET crime_location = '{countries[ran_num]}' WHERE id = {player_id}"
            cursor.execute(update_query)
            break


def check_if_correct(player_id, location):
    global correct_visited_locations
    airport= get_airport(location)
    if location == visited_locations[correct_visited_locations+1]:
        correct_visited_locations += 1
        print(f"\nYou solved the case and went to the correct country!\nYou are now in {airport}, {location},\none step closer to catch ContaMega Inc. Good job!")
        return True
    else:
        update_crime_location(player_id, 10)
        print(f"\nYour answer is wrong. One more box of Ricina is dropped by ContaMega.\nYou are now in {airport}, {location}.")
        return False


def check_if_win_or_lose(player_id):
    global criminal_escaped
    global visited_locations
    global name
    crime_location = get_criminal_location(player_id)
    if visited_locations[correct_visited_locations] == crime_location:
        print(f"\nYou have caught ContaMega Inc. and saved the world, the R-code\nproject worked as expected and Ricina is being controlled by our\nenviromental services.\n\nWell done, detective {name}, you solved the case as we expected.")
        return True
    elif criminal_escaped:
        print(f"\nContaMega Inc. has released all the Ricina into the world.\nThe world is dying and we are hopeless. Maybe in another\nlife, detective {name}...")
        return True
    else:
        return None


def check_location_exist(answer):
    answer_check = answer.title()
    countries = get_countries()
    if answer_check in countries:
        return answer_check
    else:
        print(f"\nThis country is invalid! Check the countries available in:\n\t'Option 2: Display possible countries'")
        return


def set_player_name():
    global name
    global id
    name = input("Enter your name, detective: ")
    name = name.title()
    sql = f"INSERT INTO detective_game(detective_name) VALUES('{name}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    id = cursor.lastrowid
    return name
