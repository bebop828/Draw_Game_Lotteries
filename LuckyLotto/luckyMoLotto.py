###########################################################################
################### Missouri Draw Lotto Games #############################
###########################################################################

###########################################################################
# last file update- 2025/08/12
###########################################################################


import random

# Missouri Games Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Ticket price to play $2. Drawings held Mon. Wed. & Sat. 9pm CT" 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.molottery.com/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price to play $5. Drawings are held Tues. & Fri. 10pm CT."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.molottery.com/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life_mo():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"\nCash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    cash_add = f"Available add-on- EZ Match for $1 extra per play"
    drawings_c4l = f"Ticket price to play $2. Drawings are held Nightly 8pm CT."    
    rules_c4l = f"Official Rules and Play can be found- https://www.molottery.com/cash4life Good Luck!"    
    return (numbers_main, drawings_c4l, cash_add, rules_c4l)


def mo_lotto():
    lotto_main = sorted(random.sample(range(1, 45), 6))
    lotto_num_main = f"\nMissouri Lucky Lotto Numbers: {lotto_main}" 
    lotto_drawings = f"Ticket price to play $1. Drawings are Wed. & Sat. 8:59pm CT."
    lotto_add = f"Available add on- EZ Match for $1 extra per play"
    lotto_rules = f"Official Rules and Play can be found- https://www.molottery.com/lotto Good Luck!"
    return (lotto_num_main, lotto_drawings, lotto_add, lotto_rules)


def show_lotto():
    show_main = sorted(random.sample(range(1, 40), 5))
    show_num_main = f"\nMissouri Lucky Show Me Cash Lotto Numbers: {show_main}"
    show_drawings = f"Ticket price to play $1. Drawings held Daily 8:59pm CT."
    show_add = f"Available add on- EZ Match for $1 extra per play."
    show_rules = f"Official Rules and Play can be found- https://www.molottery.com/show-me-cash Good Luck!"
    return (show_num_main, show_drawings, show_add, show_rules)


def pick_4():
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
    p4_main = f"\nPick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple ways to Play and Win!!!"
    p4_drawings = f"Ticket prices for play- $.50 or $1."
    p4_fire_mid = f"Available add on- EZ Match for $1 extra per play or Wild Ball (doubles the ticket price)."    
    p4_rules = f"Official Rules and Play can be found- https://www.molottery.com/pick4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


def pick_3():
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
    p3_main = f"\nPick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Multiple ways to Play and Win!!!"
    p3_drawings = f"Ticket prices for play- $.50 or $1."
    p3_fire_mid = f"Available add on- EZ Match for $1 extra per play or Wild Ball (doubles the ticket price)."    
    p3_rules = f"Official Rules and Play can be found- https://www.molottery.com/pick3 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire_mid, p3_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def cash_4_life_mo_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def mo_lotto_summary():
    lotto_main = sorted(random.sample(range(1, 45), 6))
    return ("Missouri Lotto", f"Numbers: {lotto_main}")

def show_lotto_summary():
    show_main = sorted(random.sample(range(1, 40), 5))
    return ("Show Me Cash", f"Numbers: {show_main}")

def pick4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_mo_summary,
    "Missouri Lotto": mo_lotto_summary,
    "Show Me Cash": show_lotto_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary
}

# Missouri Game Choices
mo_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: cash_4_life_mo,    
    4: mo_lotto,
    5: show_lotto,
    6: pick_4,
    7: pick_3,
    8: lambda: mo_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nMissouri Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")   
    print("4. Lotto")
    print("5. Show Me Cash")
    print("6. Pick 4")
    print("7. Pick 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")

    #waiter
    while True:
        try:
            mo_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if mo_lotto_game_choice in mo_lotto_draw_games:                        
                result = mo_lotto_draw_games[mo_lotto_game_choice]()

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
