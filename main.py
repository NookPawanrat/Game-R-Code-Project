import db_functions as game

print("\nIn a world full of threats, the company 'ContaMega Inc.' has created\na deadly chemical called 'Ricina'.\nThe damage to the environment is too high, so with global law\nenforcement, the R-Code Project is starting in order to\ncatch them, but ContaMega Inc. keeps releasing “Ricina” worldwide\nto destroy the evidence.\n\nRed code alert! We need you, agent!\nIt is your mission to stop them and their lethal creation Ricina.\nUsing your skills as a detective, you need to move to different locations\nwhere Ricina has been dumped and discover the secret code hiding behind\nthe clues we've found.\n\nHurry up and explore the first crime scene, before it's too late for\nthe world...\n\n")

name = game.set_player_name()
id = game.id
game.random_visit_location("4")
game.update_crime_location(game.id, 10)
while True:
    try:
        option = int(input(f"\nSelect one of the following actions, agent {name}:\n1- Explore the crime scene\n2- Display possible countries\n3- Move to destination\n4- Close the case\nYour selection: "))
        if option == 1:
            game.get_hint_by_country(game.visited_locations[game.correct_visited_locations+1])
        elif option == 2:
            countries = game.get_countries()
            print("\nThe countries where we know Ricina could be release are:")
            for country in countries:
                print(country)
        elif option == 3:
            answer = input(f"Enter location, agent {name}:\n")
            location = game.check_location_exist(answer)
            if location:
                game.update_player_location(id, location)
                correct = game.check_if_correct(id, location)
                win = game.check_if_win_or_lose(id)
                if win:
                    break
        elif option == 4:
            print(f"\nSad to see you leave us, agent {name}. Your case is close now and\nthe world's safety remains in danger.\n")
            break
        else:
            print(f"\nYou need to be serious, agent {name}.\nRead the options and insert a number from 1 to 4.")
    except:
        print(f"\nTry that again!\nContaMega Inc. could be playing with our system. If the problem\npersist, then the program needs to be checked by our\nR-code project team members.\nSend a message to your commander and wait for instructions.\nThis is not over, agent {name}.")
