###########################################################################
#################### California Draw Lotto Games ##########################
###########################################################################
 
###########################################################################
# last file update- 2025/05/26
# California Games currently not included:
# Daily Derby and Hot Spot
###########################################################################


import random

#California Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Ticket price $2. Cut-off time to play 7pm PST. Drawings are held Mon. Wed. & Sat."     
    pb_official = f"Official Rules and Play can be found- https://www.calottery.com/en/draw-games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Cut-off time to play 7:45pm PST. Drawings are held Tues. Fri."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.calottery.com/en/draw-games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def ca_lotto(): 
    lotto = sorted(random.sample(range(1, 48), 5))
    lotto_mega = random.randint(1, 27)
    lotto_num_main = f"California Lotto + Lucky Numbers: {lotto}, Mega: {lotto_mega}"
    lotto_draw = f"Ticket price $1. Cut-off time for play 7:45pm PST. Drawings held Wed and Sat."
    lotto_rules = f"Official Rules and Play can be found- https://www.calottery.com/en/draw-games/superlotto-plus Good Luck!"
    return (lotto_num_main, lotto_draw, lotto_rules)


def fantasy5():
    fan5_num = sorted(random.sample(range(1, 40), 5))
    fan5_num_main = f"Fantasy 5 Lucky Numbers: {fan5_num}"
    fan5_draw = f"Ticket prices $1. Cut-off time to play 6:30pm PST. Drawings are Mon-Sun."
    fan5_rules = f"Official Rules and Play can be found- https://www.calottery.com/en/draw-games/superlotto-plus Good Luck!"
    return (fan5_num_main, fan5_draw, fan5_rules)


def daily4():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)    
    da4_main = f"Daily 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"   
    da4_now = f"Now you have to decide to play these numbers Straight, Box, or Straight/Box."
    da4_draw = f"Ticket price $1. Cut-off time for play is 6:30pm PST. Drawings are held Mon-Sun"
    da4_rules = f"Official Rules and Play can be found- https://www.calottery.com/en/draw-games/daily-4 Good Luck!"
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
    p3_main = f"Daily 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, or Straight/Box."
    p3_drawings = f"Ticket prices $1. Cut-off time to play is 1pm PST for Mid-Day Draw and 6:30pm PST for Evening."       
    p3_rules = f"Official Rules and Play can be found- https://www.calottery.com/en/draw-games/daily-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)    


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

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "California Lotto +": ca_lotto_summary,
    "Fantasy 5": fantasy5_summary,
    "Daily 4": daily4_summary,
    "Daily 3": daily3_summary    
}

#draw games
ca_lotto_draw_games = { 
    1: powerball,
    2: mega_millions,
    3: ca_lotto,
    4: fantasy5,
    5: daily4,
    6: daily3,
    7: lambda: ca_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]  
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
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6Games")  
    
    
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
    