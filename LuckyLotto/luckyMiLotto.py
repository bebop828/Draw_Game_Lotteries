###########################################################################
################## Michigan Draw Lotto Games ##############################
###########################################################################

###########################################################################
# last file update- 2025/07/11
# Michigan has Keno and Cash Pop. These games to be coded later.
###########################################################################

import random

# Michigan Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add ons- Power Play and Double Play $1 extra."
    pb_official = "Official Rules and Play can be found- https://www.michiganlottery.com/games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.michiganlottery.com/games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"\nLucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price $2. Drawings held Daily"
    lucky_rules = "Official Rules and Gameplay can be found- https://www.michiganlottery.com/games/lucky-for-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def lotto_47():
    lotto_num = sorted(random.sample(range(1, 48), 6))
    lotto_main = f"\nLotto 47 Lucky Numbers: {lotto_num}"
    lotto_draw = "Ticket price to play $1. Drawings are held Wed. & Sat. 7:29pm ET"
    lotto_add = "Available add ons- Double Play and EZ Match $1 each"
    lotto_rules = "Official Rules and Play can be found- https://www.michiganlottery.com/games/classic-lotto-47 Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def fantast_5():
    fant_num = sorted(random.sample(range(1, 40), 5))
    fant_main = f"\nFantasy 5 Lucky Numbers: {fant_num}"
    fant_draw = "Ticket price to play $1. Drawings held Daily 7:29pm ET"
    fant_add = "Available add on- Double Play and EZ Match $1 each"
    fant_rules = "Officail Rules and Play can be found- https://www.michiganlottery.com/games/fantasy-5 Good Luck!"
    return (fant_main, fant_draw, fant_add, fant_rules)

def daily_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:59pm ET Draw")
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
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    p4_main = f"\nDaily 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!."
    p4_drawings = "Ticket Price to Play $1."      
    p4_rules = "Official Rules and Play can be found- https://www.michiganlottery.com/games/daily-4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


def daily3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:59pm ET Draw")
        print("2. Evening 7:59pm ET Draw")

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
    p3_main = f"\nDaily 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Base ticket prices $.50 or $1."     
    p3_rules = "Official Rules and Play can be found- https://www.michiganlottery.com/games/daily-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


# Michigan Game Summaries
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

def lotto_47_summary():
    lotto_num = sorted(random.sample(range(1, 48), 6))
    return ("Lotto 47", f"Numbers: {lotto_num}")

def fantast_5_summary():
    fant_num = sorted(random.sample(range(1, 40), 5))
    return ("Fantasy 5", f"Numbers: {fant_num}")

def daily4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Daily 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def daily3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Daily 3", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_summary,
    "Lotto 47": lotto_47_summary,
    "Fantasy 5": fantast_5_summary,
    "Daily 4": daily4_summary,
    "Daily 3": daily3_summary
}


# Michigan Draw Games
mi_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lucky_life,
    4: lotto_47,
    5: fantast_5,
    6: daily_4,
    7: daily3,
    8: lambda: mi_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nMichigan Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. Lotto 47")
    print("5. Fantasy 5")
    print("6. Daily 4")
    print("7. Daily 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")
    
    
    #waiter
    while True:
        try:
            mi_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if mi_lotto_game_choice in mi_lotto_draw_games:                        
                result = mi_lotto_draw_games[mi_lotto_game_choice]()

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