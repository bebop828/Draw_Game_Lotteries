###########################################################################
#################### Virgina Draw Lotto Games #############################
###########################################################################

###########################################################################
# last file update- 2025/06/07
# Virgina has Keno Draw Game.
# Keno not included in current version
########################################################################### 


import random


# Virgina Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues & Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/megamillions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life_va():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/cash4life Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def cash_popva():    
    while True:
        try:
            num_choices = int(input("How many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-15.")
    
    while True: 
        print("Select a game time to play:")
        print("1. Coffee Break 9am ET Draw")
        print("2. Lunch Break 12pm ET Draw")
        print("3. Rush Hour 5pm ET Draw")
        print("4. Prime Time 9pm ET Draw")
        print("5. After Hours 11:59pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter either (1-5)")
            continue

        game_time_mapping = {
            1: 'Coffee Break',
            2: 'Lunch',
            3: 'Rush hour',
            4: 'Prime Time',
            5: 'After Hours'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-5)")
            continue

        game_time = game_time_mapping[choice]
        break
    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"Lucky Cash Pop Number for {game_time}: {pop}"
    pop_drawings = f"Base ticket price varies. Players will choose from $1, $2, $5, or $10 bet amounts per Cash Pop numbers played." 
    pop_win = f"Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/cashpop Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)


def bank_aMillion():
    main = sorted(random.sample(range(1, 41), 6))
    va_lotto_main = f"Lucky Numbers for Bank A Milion: {main}"
    va_lotto_drawings = f"Base ticket to play is $2. Play style varies."
    va_time= f"Drawings are held Wed & Sat. 11:15pm ET."    
    va_lotto_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/bankamillion Good Luck!"    
    return (va_lotto_main, va_lotto_drawings, va_time,va_lotto_rules)


def cash_5EZva():
    main = sorted(random.sample(range(1, 46), 6))
    c5_lotto_main = f"Ca$h 5 with EZ Match Lucky Numbers: {main}"
    c5_lotto_drawings = f"Base ticket price $1. Drawings held daily!"
    c5_lotto_add = f"Available add on- EZ Match $1 extra."
    c5_lotto_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/cash5 Good Luck!"    
    return (c5_lotto_main, c5_lotto_drawings, c5_lotto_add, c5_lotto_rules)


def pick_5():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm ET Draw")
        print("2. Night 11pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
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
    p5_main = f"Pick 5 with Fireball for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = f"Now you have to decide to play these numbers Exact, Any Order, or 50/50."
    p5_drawings = f"Base ticket prices are $.50 or $1. Drawings held daily."
    p5_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p5_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/pick5 Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_fire, p5_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm ET Draw")
        print("2. Night 11pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
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
    p4_main = f"Pick 4 with Fireball for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1. Drawings held daily!"
    p4_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/pick4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire, p4_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm ET Draw")
        print("2. Night 11pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)        
    p3_main = f"Pick 3 with Fireball for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, Combo, or Pairs."
    p3_drawings = f"Base ticket prices are $.50 or $1. Drawings held daily!."
    p3_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p3_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/pick3 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def cash_4_life_va_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def cash_pop_summary(): 
    draw_time_pop = random.choice(["Coffee Break", "Lunch", "Rush Hour", "Prime Time", "After Hours"])
    pop = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"{draw_time_pop}: Numbers: {pop} ")

def bank_aMillion_summary():
    main = sorted(random.sample(range(1, 41), 6))
    return ("Bank a Million", f"Numbers: {main}")

def cash_5EZva_summary():
    main = sorted(random.sample(range(1, 46), 6))
    return ("Ca$h 5", f"Numbers: {main}")

def pick5_summary():
    draw_time5 = random.choice(['Day', 'Night'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return ("Pick 5 with Fireball", f'{draw_time5}: Numbers {set_1}, {set_2}, {set_3}, {set_4}, {set_5}')

def pick4_summary():
    draw_times4 = random.choice(['Day', 'Night'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4 with Fireball", f"Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick_3_summary(): 
    draw_time_3 = random.choice(['Day', 'Night'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    return ("Pick 3 with Fireball", f"Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_va_summary,
    "Cash Pop": cash_pop_summary, 
    "Bank a Million": bank_aMillion_summary,
    "Ca$h 5": cash_5EZva_summary,  
    "Pick 5": pick5_summary, 
    "Pick 4": pick4_summary, 
    "Pick 3": pick_3_summary
}


# Virgina Game choices
va_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: cash_4_life_va,
    4: cash_popva,
    5: bank_aMillion,
    6: cash_5EZva,
    7: pick_5,
    8: pick_4,
    9: pick_3,
    10: lambda: va_lotto_draw_games[random.randint(1, 9)](), 
    11: lambda: [func() for func in summary_lotto_draw_games.values()]   
}


# print the menu
def play_game():
    print("\nVirgina Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Mllions")
    print("3. Cash 4 Life")
    print("4. Cash Pop")
    print("5. Bank A Million")
    print("6. Ca$h 5 with EZ Match")
    print("7. Pick 5 with FIREBALL")
    print("8. Pick 4 with FIREBALL")
    print("9. Pick 3 with FIREBALL")
    print("10. Can't Decide? Try Random Game!!!")
    print("11. How About Quick Pick All 9 Games") 


    # waiter
    while True:
        try:
            va_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if va_lotto_game_choice in va_lotto_draw_games:                        
                result = va_lotto_draw_games[va_lotto_game_choice]()

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