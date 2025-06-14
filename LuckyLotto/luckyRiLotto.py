###########################################################################
################# Rhode Island Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/06/14
# Rhode Island has Keno. Keno not currently included in file
###########################################################################  


import random

# Rhode Island Game Choices
def powerball():
    pb_main = sorted(random.random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 110:59pm ET." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.rilot.com/en-us/powerball.html Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. & Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.rilot.com/en-us/megamillions.html Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

    
def lucky_for_life_ri():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"Lucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Drawings are held Nightly  about 10:35pm ET"    
    life_rules = f"Official Rules and Play can be found- https://www.rilot.com/en-us/lucky-for-life.html Good Luck!"    
    return (life_return, life_drawings, life_rules)


def wild_money():
    wild_num = sorted(random.sample(range(1, 39), 5))
    wild_main = f"Wild Money Lucky Numbers: {wild_num}"
    wild_draw = f"Ticket price to play $1. Drawings held Daily around 7:29pm ET"
    wild_rules = f"Official Rules and Play can be found - https://www.rilot.com/en-us/wild-money.html Good Luck!"
    return (wild_main, wild_draw, wild_rules)


def the_numbers():
    while True:
        print("Please select a game time to play: ")
        print("1. Mid-day 1:30pm ET Draw")
        print("2. Evening 7:29pm ET Draw")

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
    
    while True:
        print("\nNow, choose the game play type:")
        print("1. 4 Digit")
        print("2. 3 Digit")
        print("3. Back 3")
        print("4. 2 Digit")

        try:
            game_choice = int(input("Enter your selection (1–4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        game_type_mapping = {
            1: '4 Digit',
            2: '3 Digit',
            3: 'Back 3',
            4: '2 Digit'
        }

        if game_choice not in game_type_mapping:
            print("Invalid selection. Please choose a number from 1 to 4.")
            continue

        game_type = game_type_mapping[game_choice]
        break 
    
    
    if game_choice == 1:  # 4 Digit
        nums = [random.randint(0, 9) for _ in range(4)]
        result = f"The Lucky Numbers for {game_time} - 4 Digit: {nums}"
        wager = "Ticket wagers range: $0.50, $1, $2, $5"
        time = "Drawings held Daily."
        fill = "Now you will have to choose to play these numbers Straight, Box, or Combo"
        card = "For 4 Digit fill in your numbers to each play column on the game slip."
        play = "Official Rules and Gameplay can be found- https://www.rilot.com/en-us/the-numbers.html Good Luck!"
    elif game_choice == 2:  # 3 Digit
        nums = [random.randint(0, 9) for _ in range(3)]
        result = f"The Lucky Numbers for {game_time} - 3 Digit: {nums}"
        wager = "Ticket wagers range: $0.50, $1, $2, $5"
        time = "Drawings held Daily."
        fill = "Now you will have to choose to play these numbers Straight, Box, or Combo"
        card = "For 3 Digit fill in your numbers to first 3 columns on the game slip."
        play = "Official Rules and Gameplay can be found- https://www.rilot.com/en-us/the-numbers.html Good Luck!"
    elif game_choice == 3:  # Back 3
        nums = [random.randint(0, 9) for _ in range(3)]
        result = f"The Lucky Numbers for {game_time} - Back 3: {nums}"
        wager = "Ticket wagers range: $0.50, $1, $2, $5"
        time = "Drawings held Daily."
        fill = "Now you will have to choose to play these numbers Straight, Box, or Combo"
        card = "For Back 3 Digit fill in the last 3 columns on the game slip."
        play = "Official Rules and Gameplay can be found- https://www.rilot.com/en-us/the-numbers.html Good Luck!"
    elif game_choice == 4:  # 2 Digit
        nums = [random.randint(0, 9) for _ in range(2)]
        result = f"The Lucky Numbers for {game_time} - 2 Digit: {nums}"
        wager = "Ticket wagers range: $0.50, $1, $2, $5"
        time = "Drawings held Daily."
        fill = "Now you will have to choose to play these numbers Straight, Box, or Combo"
        card = "For 2 Digit fill in first 2 columns on the game slip."
        play = "Official Rules and Gameplay can be found- https://www.rilot.com/en-us/the-numbers.html Good Luck!"

    return result, wager, time, fill, card, play


# Summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lucky_for_life_ri_summary():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_main}, Lucky Ball: {lucky_ball}")

def wild_money_summary():    
    wild_num = sorted(random.sample(range(1, 39), 5))
    return ("Wild Money", f"Numbers: {wild_num}")

def the_numbers_summary():
    draw_time = random.choice(['Mid-day', 'Evening'])
    draw_type = random.choice(['4 Digit', '3 Digit', 'Back 3', '2 Digit'])
    if draw_type == '4 Digit':  # 4 Digit
        nums = [random.randint(0, 9) for _ in range(4)]
        result = f"The Numbers {draw_time} - 4 Digit: {nums} Good Luck!"
    elif draw_type == '3 Digit':  # 3 Digit
        nums = [random.randint(0, 9) for _ in range(3)]
        result = f"The Numbers {draw_time} - 3 Digit: {nums} Good Luck!"
    elif draw_type == 'Back 3':  # 3 Digit
        nums = [random.randint(0, 9) for _ in range(3)]
        result = f"The Numbers {draw_time} - Back 3: {nums} Good Luck!"
    elif draw_type == '2 Digit':  # 2 Digit
        nums = [random.randint(0, 9) for _ in range(2)]
        result = f"The Numbers {draw_time} - 2 Digit: {nums} Good Luck!"
    return result

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_for_life_ri_summary,
    "Wild Money": wild_money_summary,
    "The Numbers": the_numbers_summary    
}


# Rhode Island Game Choices
ri_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: lucky_for_life_ri,
    4: wild_money,
    5: the_numbers,   
    6: lambda: ri_lotto_draw_games[random.randint(1, 5)](),
    7: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nRhode Island Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. Wild Money")
    print("5. The Numbers")
    print("6. Can't Decide? Try Random Game!")
    print("7. How About Quick Pick All 5 Games")   
    
    #waiter
    while True:
        try:
            ri_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ri_lotto_game_choice in ri_lotto_draw_games:                        
                result = ri_lotto_draw_games[ri_lotto_game_choice]()

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
    
    