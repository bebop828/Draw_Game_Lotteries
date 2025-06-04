###########################################################################
################## South Carolina Draw Lotto Games ########################
###########################################################################

###########################################################################
# last file update- 2025/06/04
# South Carolina has Cash Pop. This game is not included in file currently
###########################################################################


import random 

# South Carolina Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/Powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/MegaMillions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def palm_cash_5():
    cash_5_main = sorted(random.sample(range(1, 43), 5))
    cash_5_numbers_main = f"Palmetto Cash 5 Lucky Numbers: {cash_5_main}"
    cash_5_drawings = f"Base ticket price $2. Cut-off time to play is 6:45pm each afternoon. Drawings held at 6:59pm ET daily."    
    cash_5_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/PalmettoCash5 Good Luck!"    
    return (cash_5_numbers_main, cash_5_drawings, cash_5_rules)

def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw")
        print("2. Evening Draw")

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
    p4_main = f"Pick 4 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1. Multiple Drawings Daily!"
    p4_fire_mid = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/Pick4 Good Luck! Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)

def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw")
        print("2. Evening Draw")

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
    p4_main = f"Pick 3 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1. Multiple Drawings Daily!"
    p4_fire_mid = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/Pick3 Good Luck! Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def palm_cash_5_summary():
    cash_5_main = sorted(random.sample(range(1, 43), 5))
    return ("Palmetto Cash 5", f"Numbers: {cash_5_main}")

def pick4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4 with Fireball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3 with Fireball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Palmetto Cash 5": palm_cash_5_summary,
    "Pick 4 with Fireball": pick4_summary,
    "Pick 3 with Fireball": pick3_summary
}


# South Carolina Game Choices
sc_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: palm_cash_5,
    4: pick_4,
    5: pick_3,
    6: lambda: sc_lotto_draw_games[random.randint(1, 5)](),    
    7: lambda: [func() for func in summary_lotto_draw_games.values()] 
}

# print the menu
def play_game():
    print("South Carolina Lotto:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Palmetto Cash 5")
    print("4. Pick 4 plus FIREBALL")
    print("5. Pick 3 plus FIREBALL")
    print("6. Can't Decide? Try Random Game!!!")
    print("7. How About Quick Pick All 5 Games")
    

# waiter
    while True:
        try:
            sc_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if sc_lotto_game_choice in sc_lotto_draw_games:                        
                result = sc_lotto_draw_games[sc_lotto_game_choice]()

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

   
# cook
def main():
    while True:
        play_game()
        while True:
            play_again = input("\nWould you like to try another draw game? (y/n): ").strip().lower()
            if play_again == 'y':
                break  
            elif play_again == 'n':
                print("Ok! Good Luck!!!")
                return   
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()