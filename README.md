# R-Code Project: the game project for Metropolia IT Software 2

R-Code Project is a flight-simulator puzzle game created by Binchi Zhou, Giselle Altamiranda, Pawanrat Santiyanon and Tingyu Pan, first year students from Metropolia University of Applied Sciences. This web-based game is based on the software 1 prototype.

## Story and background

The story of R-Code Project unveils in the fictional future, where the global industries are under the monopoly of a conglomerate called Conta Mega Inc. Behind the glory of the thriving Conta Mega Inc. lies a conspiracy which only a few people are aware of: Conta Mega Inc. has been secretly disposing Ricina, a toxic byproduct from Conta Mega Inc.’s affiliated factories. To hide their conducts from the public, Conta Mega Inc. has been randomly dropping a fraction of this toxic substance around the world, one country at a time. According to the ongoing investigation, five portions of Ricina have been disposed at five different locations so far. 

The player is a special agent and environment specialist. The player is asked to investigate the case, track the location of the substances, and eventually arrest Conta Mega Inc.’s toxic disposal team and press charges before Ricina pollutes every corner of the planet Earth.

## Install and Run

Before running the game, you need to download the game database "crime_game.sql" to your local computer.

* Step 1: Clone the project code to your local computer. 
* Step 2: Download Python and a database management system if it's not yet installed on your machine. We recommend using [MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.3.0&os=windows&cpu=x86_64&pkg=msi&m=xtom_tal).
* Step 3: Go to your SQL console, input your password, and execute the following command:
  * `source` the path to crime_game.sql;
* Step 4: Change the password of database connection in db_functions.py to your own password.

Now you shall be able to run route.py and go to your local server to start the game. Detailed gameplay instruction can be accessed by clicking "How to Play" button in the game webpage.

### Winning or losing the game

At the start of the game, Conta Mega Inc. has already disposed Ricina at **5** countries. Each time you input a correct country, the criminals will panic and not move to their next target. However, each time you enter a wrong country, Conta Mega Inc. will continue their plan.

There are two possible endings:

* You **WIN** the game if you catch the criminals, i.e. you visited all the countries where ContaMega Inc. dropped Ricina, before ContaMega reaches their **10th** destination.
* You **LOSE** the game if ContaMega Inc. reaches their **10th** target country.

<br>

Now it's your time to shine, detective! Enjoy the game and let us know what you think!

<br>

## Key contributors
[Binchi Zhou](https://github.com/zeclaircie)

[Giselle Altamiranda](https://github.com/Gisaltamir)

[Pawanrat Santiyanon](https://github.com/NookPawanrat)

[Tingyu Pan](https://github.com/tingyup1)


