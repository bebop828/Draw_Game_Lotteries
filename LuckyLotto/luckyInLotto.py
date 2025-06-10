###########################################################################
###################### Indiana Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/06/09
########################################################################### 


import random

# Indiana Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Drawings are held Tues & Fri. around 11pm ET."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life_in():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Drawings are held Nightly around 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/cash4life/ Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def hoosier_lotto(): 
    hoo_num = sorted(random.sample(range(1, 47), 6))
    hoo_main = f"Hoosier Lotto +Plus Lucky Numbers: {hoo_num}"
    hoo_draw = f"Base ticket price $2. Drawings held Wed. & Sat. around 11pm ET"
    hoo_add = f"Available add on- +Plus $1"
    hoo_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/hoosier-lotto Good Luck!"
    return (hoo_main, hoo_draw, hoo_add, hoo_rules)


def cash5(): 
    cash_num = sorted(random.sample(range(1, 46), 5))
    cash_main = f"Ca$h 5 Lucky Numbers: {cash_num}"
    cash_draw = f"Base ticket price $1. Drawings held Daily around 11pm ET."
    cash_add = f"Available add on = EZ Match $1"
    cash_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/cash-5 Good Luck!"
    return (cash_main, cash_draw, cash_add, cash_rules)
    

def quick_draw():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw")
        print("2. Evening Draw")

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
    quick_num = sorted(random.sample(range(1, 80), 10))
    quick_main = f"Quick Draw with Bullseye Lucky Numbers: {quick_num}"
    quick_draw = f"Wager Range varies- $1, $2, $3, $5. Drawings held Daily."
    quick_add = f"Available add on- Bullseye and EZ Match each $1 extra per play."
    quick_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/quick-draw Good Luck!"
    return (quick_main, quick_draw, quick_add, quick_rules)
   
    
def cash_pop():    
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
        print("1. Morning 8:45am ET Draw")
        print("2. Matinee 11:45am ET Draw")
        print("3. Afternoon 2:45pm ET Draw")
        print("4. Evening 6:45pm ET Draw")
        print("5. Late Night 11:45pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter either (1-5)")
            continue

        game_time_mapping = {
            1: 'Morning Draw',
            2: 'Matinee Draw',
            3: 'Afternoon Draw',
            4: 'Evening Draw',
            5: 'Late Night Draw'
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
    pop_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/cash-pop Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)


def daily4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw")
        print("2. Evening Draw")

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
    p4_main = f"Daily 4 with Super Ball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple Ways to Play and Win!!!"
    p4_drawings = f"Ticket Wager range- $.50, $1, $2, $5, $10. "       
    p4_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/daily-4/ Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_rules)    


def daily3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw")
        print("2. Evening Draw")

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
    p3_main = f"Daily 3 with Super Ball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Multiple Ways to Play and Win!!!"
    p3_drawings = f"Ticket Wager range- $.50, $1, $2, $5, $10. "       
    p3_rules = f"Official Rules and Play can be found- https://hoosierlottery.com/games/draw/daily-3 Good Luck!"    
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

def cash_4_life_in_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def hoosier_lotto_summary(): 
    hoo_num = sorted(random.sample(range(1, 47), 6))
    return ("Hoosier Lotto +Plus", f"Numbers: {hoo_num}")

def cash5_summary(): 
    cash_num = sorted(random.sample(range(1, 46), 5))
    return ("Ca$h 5", f"Numbers: {cash_num}")

def quick_draw_summary():
    quick_num = sorted(random.sample(range(1, 80), 10))
    return ("Quick Draw", f"Numbers: {quick_num}")

def cash_pop_summary(): 
    draw_time_pop = random.choice(["Morning", "Matinee", "Afternoon", "Evening", "Late Night"])
    pop = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"{draw_time_pop}: Number: {pop} ")

def daily4_summary(): 
    draw4_time = random.choice(['Mid-day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Daily 4", f"{draw4_time}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def daily3_summary():
    draw3_time = random.choice(['Mid-day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    return ("Daily 3", f"Numbers: {set_1}, {set_2}, {set_3}")

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_in_summary,
    "Hoosier Lotto": hoosier_lotto_summary,
    "Ca$h 5": cash5_summary,
    "Quick Draw": quick_draw_summary,
    "Cash Pop (Single Number)": cash_pop_summary,
    "Daily 4": daily4_summary,
    "Daily 3": daily3_summary    
}


# Indiana Draw Games
in_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: cash_4_life_in,
    4: hoosier_lotto,
    5: cash5,
    6: quick_draw,
    7: cash_pop,
    8: daily4,
    9: daily3,
    10: lambda: in_lotto_draw_games[random.randint(1, 9)](),
    11: lambda: [func() for func in summary_lotto_draw_games.values()]  
}


# print the menu
def play_game():
    print("\nIndiana Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. Hoosier Lotto +Plus")
    print("5. Ca$h 5")
    print("6. Quick draw with Bullseye")
    print("7. Cash Pop")
    print("8. Daily 4 with Super Ball")
    print("9. Daily 3 with Super Ball")
    print("10. Can't Decide? Try a Random Game!")
    print ("11. How About Quick Pick All 9 Games?")
    
    #waiter
    while True:
        try:
            in_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if in_lotto_game_choice in in_lotto_draw_games:                        
                result = in_lotto_draw_games[in_lotto_game_choice]()

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
    