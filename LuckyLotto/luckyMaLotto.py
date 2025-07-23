###########################################################################
############# Massachusetts Draw Lotto Games ##############################
###########################################################################

###########################################################################
# last file update- 2025/07/22
########################################################################### 

import random

# Massachusetts Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET" 
    pb_add = "Available Add on- Powerplay $1."    
    pb_official = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri. 11pm ET"
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"\nLucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price to play $2. Drawings held Daily 10:38pm ET"
    lucky_rules = "Official Rules and Gameplay can be found- https://www.masslottery.com/games/draw-and-instants/lucky-for-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def megabucks():
    mega_num = sorted(random.sample(range(1, 45), 6))
    mega_main = f"\nMegabucks Lucky Numbers: {mega_num}"
    mega_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat. 9pm ET"
    mega_rules = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/megabucks Good Luck!"
    return (mega_main, mega_draw, mega_rules)


def mass_cash():
    mass_num = sorted(random.sample(range(1, 36), 5))
    mass_main = f"\nMass Ca$h Lucky Numbers: {mass_num}"
    mass_draw = "Ticket price to play $1. Drawings held Daily 9pm ET"
    mass_rules = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/mass-cash Good Luck!"
    return (mass_main, mass_draw, mass_rules)


def wheel():
    while True:
        print("\nSelect a game type to play:")
        print("1. Number Choice Selection")
        print("2. Odd/Even")
        print("3. Red/Black")

        try:
            choice = int(input("Which do you choose: 1-3: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1, 2, or 3.")
            continue

        game_type_mapping = {
            1: 'Number Choice Selection',
            2: 'Odd/Even',
            3: 'Red/Black'
        }

        if choice not in game_type_mapping:
            print("Invalid selection. Please choose 1-3.")
            continue

        game_type = game_type_mapping[choice]
        print(f"\nYou selected: {game_type}\n")

        # Option 1
        if choice == 1:
            print("You may choose up to 36 unique numbers from 1 to 36.")
            print("Bet amounts per number can be $1, $2, or $5 each.")

            while True:
                try:
                    num_count = int(input("How many numbers would you like to choose? (1–36): ").strip())
                    if 1 <= num_count <= 36:
                        break
                    else:
                        print("Please enter a number between 1 and 36.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            numbers_chosen = sorted(random.sample(range(1, 37), num_count))
            wheel_main = f"\nWheel of Luck Lucky Number(s): {numbers_chosen}"
            wheel_rules = (
                "Ticket price range for each number play $1, $2, or $5. "
                "\nOfficial Rules and Play can be found: "
                "https://www.masslottery.com/games/draw-and-instants/wheel-of-luck"
            )
            return (wheel_main, wheel_rules)

        # Option 2
        elif choice == 2:
            selection = random.choice(['Odd', 'Even'])
            wheel_main = f"\nWheel of Luck Odd/Even Selection: {selection}"
            wheel_rules = (
                "Ticket price range for play $1, $2, $5. "
                "\nOfficial Rules and Play can be found: "
                "https://www.masslottery.com/games/draw-and-instants/wheel-of-luck"
            )
            return (wheel_main, wheel_rules)

        # Option 3
        elif choice == 3:
            selection = random.choice(['Red', 'Black'])
            wheel_main = f"\nWheel of Luck Red/Black Selection: {selection}"
            wheel_rules = (
                "Ticket price range for play $1, $2, $5. "
                "\nOfficial Rules and Play can be found: "
                "https://www.masslottery.com/games/draw-and-instants/wheel-of-luck"
            )
            return (wheel_main, wheel_rules)


def num_game():
    while True: 
        print("\nSelect a game time to play:")
        print("1. Mid-day")
        print("2. Evening")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day Draw',
            2: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    n4_main = f"\nThe Numbers Game Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    n4_now = "Multiple Ways to Bet, Play, and Win!!!"
    n4_drawings = "Ticket prices start as low as $.25"      
    n4_rules = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/the-numbers-game Good Luck!"
    return (n4_main, n4_now, n4_drawings, n4_rules)


def keno():
    while True: 
        try:
            num_choices = int(input("\nHow many spots would you like to play? Choose 1-12: ").strip())
            if num_choices < 1 or num_choices > 12:
                print("Invalid selection. Please enter a number 1-12.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-12")

    spot_num = sorted(random.sample(range(1, 81), num_choices))
    spot_main = f"\nHere are your Keno Lucky Numbers: {spot_num}"
    spot_draw = "Ticket wager on each drawing from $1 to $20!\nDrawings held Daily every 3 minutes!"
    spot_add = "Available add on: Bonus (Doubles the wager price)"
    spot_rules = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/keno Good Luck!"
    return(spot_main, spot_draw, spot_add, spot_rules)


# Massachusetts Game Summaries
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lucky_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    life_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {life_ball}")
    
def megabucks_summary():
    mega_num = sorted(random.sample(range(1, 45), 6))
    return ("Megabucks", f"Numbers: {mega_num}")

def mass_cash_summary():
    mass_num = sorted(random.sample(range(1, 36), 5))
    return ("Mass Ca$h", f"Numbers: {mass_num}")

def wheel_summary():
    wheel_num = random.randint(1, 36)
    wheel_num2 = random.choice(['Even', 'Odd'])
    wheel_num3 = random.choice(['Red', 'Black'])
    return ("Wheel of Luck- choose your play type", f"\nType 1 (Single) Play: {wheel_num}\nType 2 Play: {wheel_num2}\nType 3 Play: {wheel_num3}")

def num_game_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("The Numbers Game", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def keno_summary(): 
    spot_num = random.randint(1, 80)
    return ("Keno (Single Spot)", f"Number: {spot_num}")

# Massachusetts Game Summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky Lotto": lucky_summary,
    "Megabucks": mega_summary,
    "Mass Ca$h": mass_cash_summary,
    "Wheel of Luck": wheel_summary,
    "The Numbers Game": num_game_summary,
    "Keno": keno_summary    
}

# Massachusetts Game Choices
ma_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: lucky_life,
    4: megabucks,
    5: mass_cash,
    6: wheel,
    7: num_game,    
    8: keno,
    9: lambda: ma_lotto_draw_games[random.randint(1, 8)](),    
    10: lambda: [func() for func in summary_lotto_draw_games.values()]
}   


# print the menu
def play_game():
    print("\nMassachusetts Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. Megabucks")
    print("5. Mass Ca$h")
    print("6. Wheel of Luck")
    print("7. The Numbers Game")
    print("8. Keno")        
    print("9. Can't Decide? Try Random Game!!!")    
    print("10. How About Quick Pick All 8 Games") 
    
    #waiter
    while True:
        try:
            ma_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ma_lotto_game_choice in ma_lotto_draw_games:                        
                result = ma_lotto_draw_games[ma_lotto_game_choice]()

                if isinstance(result, list):
                    for res in result:
                        if isinstance(res, tuple) and len(res) == 2:
                            print(f"{res[0]} — {res[1]}")
                        else:
                            print(res)
                else:                    
                    for item in result:
                        print(item)
                break  
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  
            print("Not a valid option. Please try again.")
    

#cook
def main():
    while True:
        play_game()
        while True:
            play_again = input("\nWould you like to try another draw game? (y/n): ").strip().lower()
            if play_again == 'y':
                break  
            elif play_again == 'n':
                print("Ok! Good Luck and Go WIN Big!!!")
                return  
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()