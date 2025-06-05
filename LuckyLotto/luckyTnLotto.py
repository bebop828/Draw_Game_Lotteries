###########################################################################
#################### Tennessee Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/06/05
# Tennessee has Keno Draw Game.
# Keno not included in current version
###########################################################################


import random

# Tennessee Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues & Fri."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life_tn():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Drawings are held Nightly!"    
    rules_c4l = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/cash-4-life/ Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_num = f"Lucky Lotto America with Quick Cash Lucky Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. and Sat."    
    lotto_add = f"Available add on games- Quick Cash and All Star Bonus $1 extra each per play"
    lotto_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)


def daily_tn():
    daily_main = sorted(random.sample(range(1, 39), 5))    
    daily_num = f"Daily Tennessee Jackpot with Quick Cash Lucky Numbers: {daily_main}"
    daily_drawings = f"Base ticket price $1. Drawings are held Daily."    
    daily_add = f"Available add on games- Quick Cash $1 extra per play"
    daily_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/daily-tennessee-jackpot Good Luck!"        
    return (daily_num, daily_drawings, daily_add, daily_rules)


def tn_cash(): 
    tncash_main = sorted(random.sample(range(1, 36), 5))
    tncash_ball = random.randint(1, 5)
    tncash_num = f"Lucky Tennessee Cash with Quick Cash Numbers: {tncash_main}, Cash Ball: {tncash_ball}."
    tncash_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. & Fri."    
    tncash_add = f"Available add on games- Quick Cash $1 extra per play"
    tncash_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/tennessee-cash Good Luck!"    
    return (tncash_num, tncash_drawings, tncash_add, tncash_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")        
        print("1. Morning Draw")
        print("2. Mid-day Draw")
        print("3. Evening Draw")

        try:
            choice = int(input("Make selection (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Morning Draw',
            2: 'Mid-Day Draw',
            3: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    c3_main = f"Cash 3 with Wild Ball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    c3_now = f"Now you have to decide to play these numbers Exact, Any Order, Exact/ Any Order, or Combo"
    c3_drawings = f"Base ticket prices either $.50 or $1. Morning, Mid-Day, and Evening Drawings held Mon-Sat. Evening drawings Sun only."
    c3_wild = f"Available add on- Wild Ball (doubles ticket amount)."   
    c3_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/cash3 Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_wild, c3_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")        
        print("1. Morning Draw")
        print("2. Mid-day Draw")
        print("3. Evening Draw")

        try:
            choice = int(input("Make selection (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Morning Draw',
            2: 'Mid-Day Draw',
            3: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    c4_main = f"Cash 4 with Wild Ball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = f"Now you have to decide to play these numbers Exact, Any Order, Exact/ Any Order, or Combo"
    c4_drawings = f"Base ticket prices either $.50 or $1. Morning, Mid-Day, and Evening Drawings held Mon-Sat. Evening drawings Sun only."
    c4_wild = f"Available add on- Wild Ball (doubles ticket amount)."   
    c4_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/cash4 Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_wild, c4_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def cash_4_life_tn_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def lotto_summary():
    lotto_main = sorted(random.sample(range(1, 53), 5))
    lotto_star = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {lotto_star}")

def daily_tn_summary():
    daily_main = sorted(random.sample(range(1, 39), 5))
    return ("Daily Tennessee Jackpot", f"Numbers: {daily_main}")

def tn_cash_summary(): 
    tncash_main = sorted(random.sample(range(1, 36), 5))
    tncash_ball = random.randint(1, 5)
    return ("Tennessee Cash", f"Numbers: {tncash_main}, Cash Ball: {tncash_ball}")

def cash3_summary():    
    draw_time = random.choice(["Morning", "Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Cash 3", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def cash4_summary(): 
    draw_time4 = random.choice(["Morning", "Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Cash 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_tn_summary,
    "Lotto America": lotto_summary,
    "Daily Tennessee Jackpot with Quick Cash": daily_tn_summary,
    "Tennessee Cash": tn_cash_summary,
    "Cash 3": cash3_summary,
    "Cash 4": cash4_summary    
}


# Tennessee Game Choices
tn_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: cash_4_life_tn,
    4: lotto_america,
    5: daily_tn,
    6: tn_cash,
    7: cash_3,
    8: cash_4,
    9: lambda: tn_lotto_draw_games[random.randint(1, 8)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()]
}

# print the menu
def play_game():
    print("\nTennessee Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. Lotto America with Quick Cash")
    print("5. Daily Tennessee Jackpot with Quick Cash")
    print("6. Tennessee Cash with Quick Cash")
    print("7. Cash 3 with Wild Ball")
    print("8. Cash 4 with Wild Ball")
    print("9. Can't Decide? Try Random Game!!!")
    print("10. How About Quick Pick All 8 Games") 
    
    
    # waiter
    while True:
        try:
            tn_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if tn_lotto_game_choice in tn_lotto_draw_games:                        
                result = tn_lotto_draw_games[tn_lotto_game_choice]()

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
