# R-Code Project: the game project for Metropolia IT Software 1

R-Code Project is a flight-simulator puzzle game prototype created by Binchi Zhou, Giselle Altamiranda, Pawanrat Santiyanon and Tingyu Pan, first year students from Metropolia University of Applied Sciences. R-Code Project is the final project of the course Software 1. 

This game program uses python as the main programming language. The project database is based on the flight_game database provided by the course lecturers. The project team redesigned and named the database as "crime_game". The Python program communicate the database through MySQL driver.

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

Now you shall be able to run the main program.

## How to play

This section will provide a step-by-step tutorial for the gameplay.

### Getting started
After running the program, a short text about the story and your mission will be displayed on the screen.
> In a world full of threats, ... 
> 
> Red code alert! We need you, agent!It's your mission to stop them and their lethal creation Ricina. Using your skills as detective, you need to move to different locations where Ricina has been dumped and discover the secret code hiding behind the clues we've found. 
> 
> Hurry up and explore the first crime scene, before it's too late for the world...

The game program will prompt you to enter your name. The name can be **any combination of letters, numbers, or special characters**. The name will be registered in your local database.

### Gameplay
As the game starts, four action options will be displayed in the console:

> 1- Explore crime scene.
> 
> 2- Display possible countries.
> 
> 3- Move to destination.
> 
> 4- Close the case.
> 
> Your selection:

**When you enter number 1**, the game will display one crime scene, i.e. the clue that points to the country where Conta Mega Inc. disposed Ricina. In the current version, the clues could be the following five types:

> * Clues that contain keywords that are written backwards;
> * Clues where certain letters are colored;
> * Clues with keywords mixed with irrelevant letters;
> * Clues where the player needs to decrypt with a table;
> * Clues in morse code.

As the detective, your mission is to figure out which country the clue is referring to, and enter your answer in *3-Move to destination*.

**When you enter number 2**, the game will print out a list of countries where Conta Mega Inc. could be committing their crime. This function will help you when you need to narrow down your options.

> Your selection: 2
> 
> The countries where we know Ricina could be release are:
> 
> Argentina
> 
> Australia
> 
> ...

**When you enter number 3**, the game will allow you to enter the country name. The input is not case-sensitive, but you must use the correctly-spelled, standard country name as provided by the game in *2- Display possible countries*.

After you entering the country name, the game program will determine if the answer is correct.

**When you enter number 4**, the game program will end. All your progress will be cleared but stored in the database. The next time you run the main program, it will create a new game. 

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


