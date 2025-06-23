###################################################################
############### Minnesota Draw Lotto Games ########################
###################################################################

###################################################################
# last file update- 2025/06/20
################################################################### 


import random

# Minnesota Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Base ticket price $2. Drawings are held Mon. Wed. & Sat. 9:59pm CT" 
    pb_add = "Powerplay add on $1."    
    pb_official = "Official Rules and Play can be found- https://www.mnlottery.com/games/lotto/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri. 10pm CT"
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.mnlottery.com/games/lotto/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = "Ticket price $1. Drawings are held Mon. Wed. & Sat. 9:20pm CT"
    lotto_add = "Add on- All-Star Multiplier available for $1 extra"
    lotto_rules = "Official Rules and Play can be found- https://www.mnlottery.com/games/lotto/lotto-america Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules) 


def gopher():
    gopher_num = sorted(random.sample(range(1, 48), 5))
    gopher_main = f"Gopher 5 Lucky Numbers: {gopher_num}"
    gopher_draw = "Ticket price to play $1. Drawings held Mon. Wed. & Fri. 6:17pm CT"
    gopher_rules = "Offical Rules and Play can be found- https://www.mnlottery.com/games/lotto/gopher-5"
    return (gopher_main, gopher_draw, gopher_rules)


def north5():
    north_nums = sorted(random.sample(range(1, 35), 5))
    north_main = f"North 5 Lucky Numbers: {north_nums}"
    north_draw = "Ticket price to play $1. Drawings held Daily 6:17pm CT"
    north_add = "Available add on- EZ Match $1"
    north_rules = "Official Rules and Play can be found- https://www.mnlottery.com/games/lotto/north-5 Good Luck!"
    return (north_main, north_draw, north_add, north_rules)


def pick3():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    p3_main = f"Pick 3 Lucky Numbers: {set_1}, {set_2}, {set_3}"
    p3_draw = "Ticket Wager to play $.50 & $1. Drawings held Daily 6:17pm CT."
    p3_win = "Multiple ways to Play and Win!"
    p3_rules = "Official Rules and Play can be found- https://www.mnlottery.com/games/lotto/pick-3 Good Luck!"
    return (p3_main, p3_draw, p3_win, p3_rules)

# Minnesota Game Summaries
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lotto_summary():
    lotto_main = sorted(random.sample(range(1, 53), 5))
    lotto_star = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {lotto_star}")

def gopher5_summary():
    gopher_num = sorted(random.sample(range(1, 48), 5))
    return ("Gopher 5", f"Numbers: {gopher_num}")

def north5_summary():
    north_nums = sorted(random.sample(range(1, 35), 5))
    return ("North 5", f"Numbers: {north_nums}")

def pick3_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Gopher 5": gopher5_summary,
    "North 5": north5_summary,
    "Pick 3": pick3_summary
}


#Minnesota Draw Games
mn_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: gopher,
    5: north5,
    6: pick3,
    7: lambda: mn_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]     
}


# print the menu
def play_game():
    print("\nMinnesota Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Gopher 5")
    print("5. North 5")
    print("6. Pick 3")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")       
    
    # waiter
    while True:
        try:
            mn_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if mn_lotto_game_choice in mn_lotto_draw_games:                        
                result = mn_lotto_draw_games[mn_lotto_game_choice]()

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
    
 