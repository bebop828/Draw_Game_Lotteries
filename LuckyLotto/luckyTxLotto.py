###########################################################################
#################### Texas Draw Lotto Games ###############################
###########################################################################

###########################################################################
# last file update- 2025/06/06
###########################################################################

import random

def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues & Fri."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Mega_Millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def tx_lotto():
    tx_num = sorted(random.sample(range(1, 55), 6))    
    tx_numbers_main = f"Lucky Numbers for Lotto Texas with Extra: {tx_num}"
    tx_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. & Sat 10:12pm CT."
    tx_add = f"Available add on- Extra $1 per play."
    tx_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/#HowToPlay Good Luck!"    
    return (tx_numbers_main, tx_drawings, tx_add, tx_rules)


def tx_2step():
    step_num = sorted(random.sample(range(1, 36), 4))    
    step_num_bonus = random.randint(1, 35)
    step_numbers_main = f"Lucky Texas 2 Step Numbers: {step_num}, Bonus Ball: {step_num_bonus}"
    step_drawings = f"Base ticket price $1. Drawings are held Mon & Thur. 10:12pm CT."    
    step_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Texas_Two_Step/#HowToPlay Good Luck!"    
    return (step_numbers_main, step_drawings, step_rules)


def all_nothing():    
    while True:
        print("Select a game time to play:")
        print("1: Morning- 10am CT Drawing")
        print("2: Day- 12:27pm CT Drawing")
        print("3: Evening- 6pm CT Drawing")
        print("4: Night- 10:12pm CT Drawing")
        
        try:
            choice = int(input("Make Selection and enter (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4")
            continue  
        
        game_time_mapping = {
            1: 'Morning Drawing',
            2: 'Day Drawing',
            3: 'Evening Drawing',
            4: 'Night Drawing'
        }
        
        if choice not in game_time_mapping:
            print("Invalid selection. Please choose a number between 1 and 4.")
            continue         
        
        game_time = game_time_mapping[choice]
        break    
    all_num = sorted(random.sample(range(1, 25), 12))    
    all_num_main = f"Lucky Texas All or Nothing Numbers for {game_time}: {all_num}"
    all_draw = f"Base ticket cost $2. Drawings held Mon-Sat."
    all_rules = "Official Rules and Play can be found here: https://www.texaslottery.com/export/sites/lottery/Games/All_or_Nothing/index.html#HowToPlay Good Luck!"
    return (all_num_main, all_draw, all_rules)
 
    
def pick_3():
    while True:
        print("Select a game time to play Pick 3 plus FIREBALL:")
        print("1: Morning- 10am CT Drawing")
        print("2: Day- 12:27pm CT Drawing")
        print("3: Evening- 6pm CT Drawing")
        print("4: Night- 10:12pm CT Drawing")

        try:
            choice = int(input("Make Selection and enter (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4.")
            continue  

        game_time_mapping = {
            1: 'Morning Drawing',
            2: 'Day Drawing',
            3: 'Evening Drawing',
            4: 'Night Drawing'
        }

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose a number between 1 and 4.")
            continue  
        
        game_time = game_time_mapping[choice]
        break 
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    p3_main = f"Pick 3 plus FIREBALL  Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Exact, Any Order, Exact/Any Order, or Combo"
    p3_drawings = f"Base ticket prices are $.50 or $1."
    p3_fire = f"Available add on- FIREBALL (doubles the ticket cost)."   
    p3_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Pick_3/index.html#HowToPlay Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


def daily_4():
    while True:
        print("Select a game time to play Daily 4 plus FIREBALL:")
        print("1: Morning- 10am CT Drawing")
        print("2: Day- 12:27pm CT Drawing")
        print("3: Evening- 6pm CT Drawing")
        print("4: Night- 10:12pm CT Drawing")

        try:
            choice = int(input("Make Selection and enter (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4.")
            continue  

        game_time_mapping = {
            1: 'Morning Drawing',
            2: 'Day Drawing',
            3: 'Evening Drawing',
            4: 'Night Drawing'
        }

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose a number between 1 and 4.")
            continue  
        
        game_time = game_time_mapping[choice]
        break 
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    p4_main = f"Texas Daily 4 plus FIREBALL Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Stgraight/Box, or Combo"
    p4_drawings = f"Base ticket prices are $.50 or $1."
    p4_fire = f"Available add on- FIREBALL (doubles the ticket cost)."   
    p4_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Daily_4/index.html#HowToPlay Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_fire, p4_rules)


def cash_5():
    c5_num = sorted(random.sample(range(1, 36), 5))    
    c5_numbers_main = f"Lucky Cash 5 Numbers: {c5_num}"
    c5_drawings = f"Base ticket price $1. Drawings are held Mon-Sat 10:12pm CT."    
    c5_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Cash_Five/index.html#HowToPlay Good Luck!"    
    return (c5_numbers_main, c5_drawings, c5_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def tx_lotto_summary():
    tx_num = sorted(random.sample(range(1, 55), 6)) 
    return ("Lotto Texas", f"Numbers: {tx_num}")

def tx_2step_summary():
    step_num = sorted(random.sample(range(1, 36), 4))    
    step_num_bonus = random.randint(1, 35)
    return ("Texas 2 Step", f"Numbers: {step_num}, Bonus Ball: {step_num_bonus}")

def all_nothing_summary(): 
    draw_time = random.choice(["Morning", "Day", "Evening", "Night"])
    all_num = sorted(random.sample(range(1, 25), 12))
    return ("All or Nothing", f"{draw_time}: Numbers: {all_num}")

def pick3_summary():    
    draw_time = random.choice(["Morning", "Day", "Evening", "Night"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3 plus Fireball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def daily4_summary(): 
    draw_time4 = random.choice(["Morning", "Day", "Evening", "Night"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Daily 4 plus Fireball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def cash_5_summary():
    c5_num = sorted(random.sample(range(1, 36), 5)) 
    return ("Cash 5", f"Numbers: {c5_num}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto Texas": tx_lotto_summary,
    "Texas 2 Step": tx_2step_summary,
    "All or Nothing": all_nothing_summary,
    "Pick 3": pick3_summary, 
    "Daily 4": daily4_summary,   
    "Cash 5": cash_5_summary
}


# Texas Game Choices
tx_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: tx_lotto,
    4: tx_2step,
    5: all_nothing,
    6: pick_3,
    7: daily_4,
    8: cash_5,
    9: lambda: tx_lotto_draw_games[random.randint(1, 8)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nTexas Lotto:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto Texas with Extra")
    print("4. Texas 2 Step")
    print("5. All or Nothing")
    print("6. Pick 3 with FIREBALL")
    print("7. Daily 4 with FIREBALL")
    print("8. Cash 5")
    print("9. Can't Decide? Try Random Game!!!")
    print("10. How About Quick Pick All 8 Games")
        
    
    # waiter
    while True:
        try:
            tx_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if tx_lotto_game_choice in tx_lotto_draw_games:                        
                result = tx_lotto_draw_games[tx_lotto_game_choice]()

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