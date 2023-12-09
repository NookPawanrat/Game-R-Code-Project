import mysql.connector
import random
import game as g


connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="crime_game",
    user="Nook",
    password="nook1996",
    autocommit=True
)


# ---------------  Player class ---------------- #
def set_player_name(player_name):
    sql = f"INSERT INTO detective_game(detective_name) VALUES('{player_name}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

def update_player_location(player_id,location):
    sql = f"UPDATE detective_game SET player_location = '{location}' WHERE id = {player_id}"
    cursor = connection.cursor()
    cursor.execute(sql)
    return

# ---------------  Game class  ---------------- #

def start_game():
    countries = []
    sql = "SELECT country_name, hint FROM hints "
    sql += "ORDER BY RAND() LIMIT 5;"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
            country = {"name": result[0], "hint": result[1]}
            countries.append(country)
    return countries

def get_available_countries():
    countries = "SELECT name, latitude_deg, longitude_deg, hints.country_name FROM airport, hints WHERE hints.iso_country = airport.iso_country GROUP BY airport.iso_country"
    cursor = connection.cursor()
    cursor.execute(countries)
    result = cursor.fetchall()
    countries = []
    for row in result:
        countries.append({"name": row[0], "lat": row[1], "long": row[2], "country": row[3]})
    return countries


def update_crime_location(country_arleadyHave):
    global criminal_escaped
    visited_locations =[]
    for i in range(0,5):
        n = int(i)
        country_name = country_arleadyHave[n]['name']
        if country_name not in visited_locations:
            visited_locations.append(country_name)
    countries = get_available_countries()
    if len(visited_locations) == 9:
        criminal_escaped = True
        return
    while len(visited_locations) < 9:
        ran_num = random.randrange(0,10)
        country_name = countries[ran_num]['country']
        if country_name not in visited_locations:
            visited_locations.append(countries[ran_num]['country'])
            new_crime_location = countries[ran_num]['country']
            return new_crime_location
