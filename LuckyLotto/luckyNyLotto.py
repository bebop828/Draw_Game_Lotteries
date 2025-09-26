###########################################################################
############## New York Draw Lotto Games ##################################
###########################################################################

###########################################################################
# last file update- 2025/07/10
###########################################################################

import random

# New York Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available Add on- Powerplay $1 extra."    
    pb_official = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=megamillions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"\nCash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = "Ticket price to play $2. Drawings are held Nightly."      
    rules_c4l = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=cash4life Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def ny_lotto():
    lotto_num = sorted(random.sample(range(1, 60), 6))
    lotto_main = f"\nNew York Lotto Lucky Numbers: {lotto_num}"
    lotto_draw = "Ticket price to play $1. Drawings Wed. & Sat."
    lotto_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=lotto Good Luck!"
    return (lotto_main, lotto_draw, lotto_rules)


def ny_p10():
    p10_num = sorted(random.sample(range(1, 81), 10))
    p10_main = f"\nNew York Pick 10 Lucky Numbers: {p10_num}"
    p10_draw = "Ticket price to play $1. Drawings held Daily."
    p10_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=pick10 Good Luck!"
    return (p10_main, p10_draw, p10_rules)


def quick_draw():    
    while True:
        try:
            print("\nPlay up to 10 numbers per play")
            print("Wager amounts per play from $1, $2, $3, $4, $5, or $10")
            num_choices = int(input("\nHow many Lucky Quick Draw numbers do you wish to play? Choose 1-10: ").strip())
            if num_choices < 1 or num_choices > 10:
                print("Invalid selection. Please enter a number 1-10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-10.")    
        break
    draw = sorted(random.sample(range(1, 81), num_choices))   
    draw_main = f"\nLucky Quick Draw Number(s): {draw}"     
    draw_win = "Winning amounts based off Number Spots Played "  
    draw_game = "Quick Draw Games held every 4 minutes!"
    draw_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=quickdraw Good Luck!"    
    return (draw_main, draw_win, draw_game, draw_rules)


def take_5():
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
            1: 'Mid-Day',
            2: 'Evening'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    take_num = sorted(random.sample(range(1, 40), 5))    
    take_main = f"\nTake 5 Lucky Numbers for {game_time}: {take_num}"
    take_drawings = "Ticket price to play $1. Drawings held Daily!"   
    take_add = "Available add on- Instant Win $1"
    take_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=take5 Good Luck!"    
    return (take_main, take_drawings, take_add, take_rules)


def win_4():
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
    set_4 = random.randint(0, 9)
    w4_main = f"\nWin 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    w4_now = "Multiple ways to play and win."
    w4_drawings = "Ticket prices are $.50 or $1."
    w4_win = "Available add on- Instant Win $1."    
    w4_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=win4 Good Luck!"
    return (w4_main, w4_now, w4_drawings, w4_win, w4_rules)


def numbers():
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
    num_main = f"\nNumbers Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    num_now = "Multiple ways to play and win."
    num_drawings = "Ticket prices to are $.50 or $1."
    num_add = "Available add on- Instant Win $1."    
    num_rules = "Official Rules and Play can be found- https://nylottery.ny.gov/draw-game?game=numbers Good Luck!"
    return (num_main, num_now, num_drawings, num_add, num_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def cash_4_life_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def ny_lotto_summary():
    lotto_num = sorted(random.sample(range(1, 60), 6))
    return ("New York Lotto", f"Numbers: {lotto_num}")

def ny_p10_summary():
    p10_num = sorted(random.sample(range(1, 81), 10))
    return ("New York Pick 10", f"Numbers: {p10_num}")

def quick_draw_summary(): 
    draw = random.randint(1, 80)
    return ("Quick Draw (Single Number)", f"Number: {draw} ")

def take5_summary(): 
    draw_time5 = random.choice(["Mid-Day", "Evening"])
    take_num = sorted(random.sample(range(1, 40), 5)) 
    return ("Take 5", f"{draw_time5}: Numbers: {take_num} ")

def win_4_summary():
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Win 4", f"{draw_time4}: {set_1}, {set_2}, {set_3}, {set_4}")

def numbers_summary(): 
    draw_time3 = random.choice(['Mid-day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    return (f"NY Numbers {draw_time3}: {set_1}, {set_2}, {set_3}")

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_summary,
    "New York Lotto": ny_lotto_summary,
    "New York Pick 10": ny_p10_summary,
    "Quick  Draw": quick_draw_summary,
    "Take 5": take5_summary,
    "Win 4": win_4_summary,
    "Numbers": numbers_summary    
}

# New York Game Choices
ny_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: cash_4_life,
    4: ny_lotto,
    5: ny_p10,
    6: quick_draw,
    7: take_5,    
    8: win_4,    
    9: numbers,    
    10: lambda: ny_lotto_draw_games[random.randint(1, 9)](),    
    11: lambda: [func() for func in summary_lotto_draw_games.values()]
}

# print the menu
def play_game():
    print("\nNew York Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. New York Lotto")
    print("5. New York Pick 10")
    print("6. Quick Draw")
    print("7. Take 5")        
    print("8. Win 4")    
    print("9. Numbers")    
    print("10. Can't Decide? Try Random Game!!!")    
    print("11. How About Quick Pick All 9 Games")
    
    
    #waiter
    while True:
        try:
            ny_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ny_lotto_game_choice in ny_lotto_draw_games:                        
                result = ny_lotto_draw_games[ny_lotto_game_choice]()

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
    




