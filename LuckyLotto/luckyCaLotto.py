###########################################################################
#################### California Draw Lotto Games ##########################
###########################################################################
 
###########################################################################
# last file update- 2025/07/15
# Daily Derby not currently with file
###########################################################################


import random

#California Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat."     
    pb_official = "Official Rules and Play can be found- https://www.calottery.com/en/draw-games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.calottery.com/en/draw-games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def ca_lotto(): 
    lotto = sorted(random.sample(range(1, 48), 5))
    lotto_mega = random.randint(1, 27)
    lotto_num_main = f"\nCalifornia Lotto + Lucky Numbers: {lotto}, Mega: {lotto_mega}"
    lotto_draw = "Ticket price $1. Drawings held Wed & Sat."
    lotto_rules = "Official Rules and Play can be found- https://www.calottery.com/en/draw-games/superlotto-plus Good Luck!"
    return (lotto_num_main, lotto_draw, lotto_rules)


def fantasy5():
    fan5_num = sorted(random.sample(range(1, 40), 5))
    fan5_num_main = f"\nFantasy 5 Lucky Numbers: {fan5_num}"
    fan5_draw = "Ticket prices $1. Drawings held Daily."
    fan5_rules = "Official Rules and Play can be found- https://www.calottery.com/en/draw-games/superlotto-plus Good Luck!"
    return (fan5_num_main, fan5_draw, fan5_rules)


def daily4():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)    
    da4_main = f"\nDaily 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"   
    da4_now = "Now you have to decide to play these numbers Straight, Box, or Straight/Box."
    da4_draw = "Ticket price $1. Drawings held Daily."
    da4_rules = "Official Rules and Play can be found- https://www.calottery.com/en/draw-games/daily-4 Good Luck!"
    return(da4_main, da4_now, da4_draw, da4_rules)


def daily3():
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
            1: 'Mid-Day',
            2: 'Evening'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    p3_main = f"\nDaily 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Now you have to decide to play these numbers Straight, Box, or Straight/Box."
    p3_drawings = "Ticket prices $1. Drawing held Daily."       
    p3_rules = "Official Rules and Play can be found- https://www.calottery.com/en/draw-games/daily-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)    


def hot_spot(): 
    while True: 
        try:
            num_choices = int(input("How many spots would you like to play? Choose 1-10: ").strip())
            if num_choices < 1 or num_choices > 10:
                print("Invalid selection. Please enter a number 1-10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-10")

    spot_num = sorted(random.sample(range(1, 81), num_choices))
    spot_main = f"\nHot Spot with Bulls-Eye Lucky Numbers: {spot_num}"
    spot_draw = "Ticket wager to play varies. $1-5, $10, or $20 per play!\nDrawings held Daily every 4 minutes!"
    spot_add = "Available add on- Bulls-Eye $2 min"
    spot_rules = "Official Rules and Play can be found - https://www.calottery.com/en/draw-games/hot-spot Good Luck!"
    return(spot_main, spot_draw, spot_add, spot_rules)

# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.sample(range(1, 27), 1)[0]
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.sample(range(1, 26), 1)[0]
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def ca_lotto_summary(): 
    lotto = sorted(random.sample(range(1, 48), 5))
    lotto_mega = random.randint(1, 27)
    return ("California + Lotto", f"Numbers: {lotto}, Mega: {lotto_mega}")

def fantasy5_summary():
    fan5_num = sorted(random.sample(range(1, 40), 5))
    return ("Fantasy 5", f"Numbers: {fan5_num}")

def daily4_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)    
    da4_main = f"Daily 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"
    return (da4_main)

def daily3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Daily 3", f"{draw_time}: Numbers: ({set_1}, {set_2}, {set_3})")

def hot_spot_summary(): 
    spot_num = random.randint(1, 80)
    return ("Hot Spot (Single Spot)", f"Number: {spot_num}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "California Lotto +": ca_lotto_summary,
    "Fantasy 5": fantasy5_summary,
    "Daily 4": daily4_summary,
    "Daily 3": daily3_summary,
    "Hot Spot": hot_spot_summary    
}

#draw games
ca_lotto_draw_games = { 
    1: powerball,
    2: mega_millions,
    3: ca_lotto,
    4: fantasy5,
    5: daily4,
    6: daily3,
    7: hot_spot,
    8: lambda: ca_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]  
}

#the menu
def play_game():
    print("California Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. California Lotto +")
    print("4. Fantasy 5")
    print("5. Daily 4")
    print("6. Daily 3")
    print("7. Hot Spot")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")  
    
    
    #waiter
    while True:
        try:
            ca_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if ca_lotto_game_choice in ca_lotto_draw_games:                        
                result = ca_lotto_draw_games[ca_lotto_game_choice]()

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
    