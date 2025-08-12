###########################################################################
################# Mississippi Draw Lotto Games ############################
###########################################################################

###########################################################################
# last file update- 2025/08/12
###########################################################################


import random

# Mississippi Games Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Ticket price to play $2. Drawings are held Mon. Wed. & Sat. 9:59pm CT." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.mslottery.com/games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price to play $5. Drawings are held Tues. & Fri. 10pm CT."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_num = f"\nLucky Lotto America with EZ-Match Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Ticket price to play $1. Drawings are held Mon. Wed. & Sat. 9:15pm CT"    
    lotto_add = f"Available add on games- EZ-Match and All Star Bonus $1 extra each per play"
    lotto_rules = f"Official Rules and Play can be found- https://www.mslottery.com/games/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)

def match_5multi(): 
    match_main = sorted(random.sample(range(1, 38), 5))
    match_numbers_main = f"\nLucky Match 5 with Multiplier Numbers: {match_main}"
    match_drawings = f"Ticket price to play $2. Drawings held Daily 9:30pm CT."
    match_add = f"Available add on- Multiplier $1 extra"
    match_rules = f"Official Rules and Play can be found- https://www.mslottery.com/games/mm5 Good Luck!"
    return (match_numbers_main, match_drawings, match_add, match_rules)


def cash_4():
    while True: 
        print("\nSelect a game time to play:")
        print("1. Mid-Day")
        print("2. Evening")
        
        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day Draw',
            2: 'Evening Draw'            
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
    c4_main = f"\nCash 4 with Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = f"Multiple ways to Play and Win!!!"
    c4_drawings = f"Ticket prices for play- $.50 or $1."      
    c4_add = f"Available add on- FIREBALL (doubles the ticket price)"
    c4_rules = f"Official Rules and Play can be found- https://www.mslottery.com/games/cash-4/ Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_add, c4_rules)


def cash_3():
    while True: 
        print("\nSelect a game time to play:")
        print("1. Mid-Day")
        print("2. Evening")
        
        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day Draw',
            2: 'Evening Draw'            
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break

    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)
    c3_main = f"\nCash 3 with Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    c3_now = f"Multiple ways for you to Play and Win!!!"
    c3_drawings = f"Ticket prices for play- $.50 or $1."      
    c3_add = f"Available add on- FIREBALL (doubles the ticket price)"
    c3_rules = f"Official Rules and Play can be found-https://www.mslottery.com/games/cash-3/ Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_add, c3_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lotto_america_summary(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {star_ball}")

def match_5multi_summary(): 
    match_main = sorted(random.sample(range(1, 38), 5))
    return ("Match 5 with Multiplier", f"Numbers: {match_main}")

def cash4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Cash 4 with Fireball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def cash3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Cash 3 with Fireball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_america_summary,
    "Match 5 with Multiplier": match_5multi_summary,
    "Cash 4 with Fireball": cash4_summary,
    "Cash 3 with Fireball": cash3_summary
}


# Mississippi Game Choices
ms_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: match_5multi,
    5: cash_4,
    6: cash_3,
    7: lambda: ms_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nMississippi Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America with EZ-Match")
    print("4. Match 5 with Multiplier")
    print("5. Cash 4 with FIREBALL")
    print("6. Cash 3 with FIREBALL")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")
        
    #waiter
    while True:
        try:
            ms_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ms_lotto_game_choice in ms_lotto_draw_games:                        
                result = ms_lotto_draw_games[ms_lotto_game_choice]()

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
                print("Ok! Good Luck and Go WIN Big!!!")
                return   
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()