###########################################################################
###################### Georgia Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/28
# Georgia has Keno Draw Game.
#Keno not included in current version
###########################################################################


import random 

# Georgia Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/powerball.html#tab-howToPlay Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/megamillions.html Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life_ga():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:45pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/cash-for-life.html#tab-howToPlay Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def fantasy_5_ga():
    fantasy_5_ga = sorted(random.sample(range(1, 43), 5))    
    fantasy_5_gaMain = f"Georgia Fantasy 5 Lucky Numbers: {fantasy_5_ga}"
    fantasy_5_gaDrawings = f"Base ticket price $1. Cut-off time to play is 10:45pm ET daily. Drawings held Daily 11:34pm ET."
    fantasy_5_gaAdd = f"Available add on- Ca$h Match $1 extra."
    fantasy_5_gaRules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/fantasy-five.html#tab-howToPlay"    
    return (fantasy_5_gaMain, fantasy_5_gaDrawings, fantasy_5_gaAdd, fantasy_5_gaRules)


def georgia_5():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:29pm ET Draw")
        print("2. Evening 6:59pm ET Draw")

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
    set_5 = random.randint(0, 9)
    georgia_5_main = f"Georgia 5 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    georgia_5_drawings = f"Base ticket price $1.  Drawings held daily 12:29pm ET."
    georgia_5_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/georgia-five.html Good Luck!" 
    return ( georgia_5_main, georgia_5_drawings, georgia_5_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 12:29pm ET Draw")
        print("2. Evening 6:59pm ET Draw")
        print("3. Night 11:34pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day Draw',
            2: 'Evening Draw',
            3: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break

    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)
    c3_main = f"Cash 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    c3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Combo, 1 off, or Pairs"
    c3_drawings = f"Ticket prices are $.50 or $1."
    c3_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/cash-three.html#tab-howToPlay Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 1:30pm ET Draw")
        print("2. Evening 6:59pm ET Draw")
        print("3. Night 11:34pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day Draw',
            2: 'Evening Draw',
            3: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break

    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    c4_main = f"Cash 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    c4_drawings = f"Base ticket prices are $.50 or $1."      
    c4_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/cash-four.html#tab-howToPlay Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def cash_4_life_ga_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def fantasy_5_ga_summary():
    fantasy_5_ga = sorted(random.sample(range(1, 43), 5))
    return ("Fantasy 5", f"Numbers: {fantasy_5_ga}")

def ga5_summary(): 
    draw_time5 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return ("Georgia 5", f"{draw_time5}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}, {set_5}")

def cash3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Cash 3", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def cash4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Cash 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_ga_summary,
    "Fantasy 5": fantasy_5_ga_summary,
    "Georgia 5": ga5_summary,
    "Cash 3": cash3_summary,
    "Cash 4": cash4_summary    
}


#Georgia Games
ga_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: cash_4_life_ga,     
    4: fantasy_5_ga,
    5: georgia_5,
    6: cash_3,
    7: cash_4,
    8: lambda: ga_lotto_draw_games[random.randint(1, 8)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]       
}

#print the menu
def play_game():
    print("Georgia Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. Fantasy 5")
    print("5. Georgia 5")    
    print("6. Cash 3")    
    print("7. Cash 4")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")
        

    #waiter
    while True:
        try:
            ga_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if ga_lotto_game_choice in ga_lotto_draw_games:                        
                result = ga_lotto_draw_games[ga_lotto_game_choice]()

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