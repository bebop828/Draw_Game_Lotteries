###########################################################################
#################### Wisconsin Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/06/12
###########################################################################  


import random

# Wisconsin Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 9:59pm CT." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://wilottery.com/games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. & Fri. 10pm CT."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://wilottery.com/games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def mega_bucks():
    bucks_num = sorted(random.sample(range(1, 50), 6))
    bucks_main = f"MegaBucks Lucky Numbers: {bucks_num}"
    bucks_draw = f"Ticket price to play $1. Drawings held Wed. & Sat. after 9pm CT"
    bucks_add = f"Available add on- EZ Match $1."
    bucks_rule = f"Official Rules and Play can be found- https://wilottery.com/games/megabucks Good Luck!"
    return (bucks_main, bucks_draw, bucks_add, bucks_rule)


def badger5():
    badger_num = sorted(random.sample(range(1, 32), 5))
    badger_main = f"Badger 5 Lucky Numbers: {badger_num}"
    badger_draw = f"Ticket price to play $1. Drawings are held Daily after 9pm CT."
    badger_rule = f"Official Rules and Play can be found- https://wilottery.com/games/badger-5 Good Luck!"
    return (badger_main, badger_draw, badger_rule)


def super_cash(): 
    super_num = sorted(random.sample(range(1, 40), 6))
    super_main = f"$uper Cash Lucky Numbers: {super_num}"
    super_draw = f"Ticket price to play $1. Drawings held Daily!"
    super_rule = f"Official Rules and Play can be found- https://wilottery.com/games/supercash Good Luck!"
    return (super_main, super_draw, super_rule)


def all_nothing():
    while True:
        print("Select a game time to play:")
        print("1. Mid-day Draw 1:30pm CT")
        print("2. Evening Draw 9pm CT")
        
        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue
        
        game_time_mapping = {
            1: 'Mid-day', 
            2: 'Evening'            
        }    
        
        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue
        
        game_time = game_time_mapping[choice]
        break
    all_num = sorted(random.sample(range(1, 23), 11))
    all_main = f"All or Nothing Lucky {game_time} Numbers: {all_num}"
    all_draw = f"Ticket prices $2. Drawings held Daily."
    all_rules = f"Official Rules and Play can be found- https://wilottery.com/games/all-or-nothing Good Luck!"
    return (all_main, all_draw, all_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm CT Draw")
        print("2. Evening 9pm CT Draw")

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
    p4_main = f"Pick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple ways to Play and Win!"
    p4_drawings = f"Ticket prices are $.50 or $1. Drawings held daily."        
    p4_rules = f"Official Rules and Play can be found- https://wilottery.com/games/pick-4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm CT Draw")
        print("2. Evening 9pm CT Draw")

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
    p4_main = f"Pick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple ways to Play and Win!"
    p4_drawings = f"Ticket prices are $.50 or $1. Drawings held daily."        
    p4_rules = f"Official Rules and Play can be found- https://wilottery.com/games/pick-4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm CT Draw")
        print("2. Evening 9pm CT Draw")

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
    p3_main = f"Pick 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Multiple ways to Play and Win!"
    p3_drawings = f"Ticket prices are $.50 or $1. Drawings held daily."        
    p3_rules = f"Official Rules and Play can be found- https://wilottery.com/games/pick-3 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def mega_bucks_summary():
    bucks_num = sorted(random.sample(range(1, 50), 6))
    return ("MegaBucks", f"Numbers: {bucks_num}")

def badger5_summary():
    badger_num = sorted(random.sample(range(1, 32), 5))
    return ("Badger 5", f"Numbers: {badger_num}")

def super_cash_summary(): 
    super_num = sorted(random.sample(range(1, 40), 6))
    return ("$uper Cash", f"Numbers: {super_num}")

def all_nothing_summary(): 
    draw_time = random.choice(['Mid-day', 'Evening'])
    all_num = sorted(random.sample(range(1, 23), 11))
    return ("All or Nothing", f"Numbers: {all_num}")

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

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "MegaBucks": mega_bucks_summary,
    "Badger 5": badger5_summary,
    "$uper Cash": super_cash_summary,
    "All or Nothing": all_nothing_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary    
}

# Wisconsin Game Choices
wi_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: mega_bucks,
    4: badger5,
    5: super_cash,
    6: all_nothing,
    7: pick_4,
    8: pick_3,
    9: lambda: wi_lotto_draw_games[random.randint(1, 8)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()]
}

# print the menu
def play_game():
    print("\nWisconsin Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. MegaBucks")
    print("4. Badger 5")
    print("5. $uper Cash")
    print("6. All or Nothing")
    print("7. Pick 4")        
    print("8. Pick 3")    
    print("9. Can't Decide? Try Random Game!!!")    
    print("10. How About Quick Pick All 8 Games")    
    
    #waiter
    while True:
        try:
            wi_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if wi_lotto_game_choice in wi_lotto_draw_games:                        
                result = wi_lotto_draw_games[wi_lotto_game_choice]()

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