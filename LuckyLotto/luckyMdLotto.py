###########################################################################
############### Maryland Draw Lotto Games #################################
###########################################################################

###########################################################################
# last file update- 2025/08/13
###########################################################################

import random

# Maryland Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available Add ons- Powerplay and Double Play $1 each."    
    pb_official = "Official Rules and Play can be found- https://www.mdlottery.com/games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"\nCash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = "Ticket price to play $2. Drawings are held Daily."    
    rules_c4l = "Official Rules and Play can be found- https://www.mdlottery.com/games/cash4life Good Luck!"        
    return (numbers_main, drawings_c4l, rules_c4l)


def cash_pop():    
    while True:
        try:
            num_choices = int(input("\nHow many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-15.")
    
    while True: 
        print("\nSelect a game time to play:")
        print("1. Morning 9am ET")
        print("2. Mid-day 1pm ET")
        print("3. Afternoon 6pm ET")
        print("4. Night 11pm ET")
        

        try:
            choice = int(input("Make selection and enter (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter either (1-5)")
            continue

        game_time_mapping = {
            1: 'Morning',
            2: 'Mid-day',
            3: 'Afternoon',
            4: 'Night'            
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-5)")
            continue

        game_time = game_time_mapping[choice]
        break
    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"\nLucky Cash Pop Number(s) for {game_time}: {pop}"
    pop_drawings = "Ticket wager amounts vary. Players will choose from $1, $2, $5, or $10 amounts per Cash Pop numbers played." 
    pop_win = "Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/cash-pop Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)


def bonus5():
    bonus_num = sorted(random.sample(range(1, 40), 5))
    bonus_main = f"\nBonus Match 5 Lucky Numbers: {bonus_num}"
    bonus_draw = "Ticket price to play $1. Additional board play pricing available.\nDrawings held Daily."
    bonus_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/bonus-match-5/ Good Luck!"
    return (bonus_main, bonus_draw, bonus_rules)

def multi_match():
    multi_num = sorted(random.sample(range(1, 44), 6))
    multi_main = f"\nMulti Match Lucky Numbers: {multi_num}"
    multi_draw = "Ticket price to play $2. Drawings held Mon. & Thur."
    multi_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/multi-match/ Good Luck!"
    return (multi_main, multi_draw, multi_rules)
    
def pick_5():
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
    set_5 = random.randint(0, 9)
    p5_main = f"\nPick 5 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = "Multiple ways to Play and Win!!!."
    p5_drawings = "Ticket price to play either $.50 or $1. Drawings held Daily."        
    p5_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/pick-3-pick-4-pick-5 Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_rules)


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
    p4_now = "Multiple ways to Play and Win!!!."
    p4_drawings = "Ticket price to play either $.50 or $1. Drawings held Daily."        
    p4_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/pick-3-pick-4-pick-5 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


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
    p3_main = f"\nPick 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!."
    p3_drawings = "Ticket price to play either $.50 or $1. Drawings held Daily."        
    p3_rules = "Official Rules and Play can be found- https://www.mdlottery.com/games/pick-3-pick-4-pick-5 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_rules)


def keno():
    while True: 
        try:
            num_choices = int(input("\nHow many spots would you like to play? Choose 1-10: ").strip())
            if num_choices < 1 or num_choices > 10:
                print("Invalid selection. Please enter a number 1-10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-10")

    spot_num = sorted(random.sample(range(1, 81), num_choices))
    spot_main = f"\nHere are your Keno Lucky Numbers: {spot_num}"
    spot_draw = "Ticket wager to play varies: $1-5, $10, or $20 per play!\nDrawings held Daily every 3 1/2 minutes!"
    spot_add = "Available add on: Bonus (Doubles wager price) or Super Bonus (Triples wager price)"
    spot_rules = "Official Rules and Play can be found- https://www.masslottery.com/games/draw-and-instants/keno Good Luck!"
    return(spot_main, spot_draw, spot_add, spot_rules)


# Maryland Game Summaries
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

def cash_pop_summary(): 
    draw_time_pop = random.choice(["Morning", "Matinee", "Afternoon", "Evening", "Late Night"])
    pop = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"{draw_time_pop}: Number: {pop} ")

def bonus5_summary():
    bonus_num = sorted(random.sample(range(1, 40), 5))
    return ("Bonus Match 5", f"Numbers: {bonus_num}")

def multi_match_summary():
    multi_num = sorted(random.sample(range(1, 44), 6))
    return ("Multi Match", f"Numbers: {multi_num}")

def pick5_summary(): 
    draw_time5 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return ("Pick 5 ", f"{draw_time5}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}, {set_5}")

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

def keno_summary(): 
    spot_num = random.randint(1, 80)
    return ("Keno (Single Spot)", f"Number: {spot_num}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_summary,
    "Cash Pop": cash_pop_summary,
    "Bonus Match 5": bonus5_summary,
    "Multi Match": multi_match_summary,
    "Pick 5": pick5_summary,
    "Pick 4": pick4_summary, 
    "Pick 3": pick3_summary,
    "Keno": keno_summary
}


# Maryland Game Choices
md_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: cash_4_life,
    4: cash_pop,
    5: bonus5,
    6: multi_match,
    7: pick_5,
    8: pick_4,
    9: pick_3,
    10: keno,
    11: lambda: md_lotto_draw_games[random.randint(1, 10)](),
    12: lambda: [func() for func in summary_lotto_draw_games.values()]        
}


# print the menu
def play_game():
    print("\nMaryland Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. Cash Pop")
    print("5. Bonus Match 5")
    print("6. Multi Match")
    print("7. Pick 5")
    print("8. Pick 4")
    print("9. Pick 3")
    print("10. Keno")
    print("11. Can't Decide? Try a Random Game!")
    print("12. How About Quick Pick All 10 Games")
    
    #waiter
    while True:
        try:
            md_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if md_lotto_game_choice in md_lotto_draw_games:                        
                result = md_lotto_draw_games[md_lotto_game_choice]()

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
    
    




