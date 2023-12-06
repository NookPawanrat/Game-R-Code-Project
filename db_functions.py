import mysql.connector
import random

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="crime_game",
    user="root",
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
    countries = cursor.fetchall()
    return countries



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


