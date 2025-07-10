###########################################################################
############ New Jersey Draw Lotto Games ###############################
###########################################################################

###########################################################################
# last file update- 2025/07/10
###########################################################################

import random

# New Jersey Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET" 
    pb_add = "Available Add ons- Powerplay and Double Play $1 each."    
    pb_official = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/powerball.html Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri. 11pm ET"
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/megamillions.html Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"\nCash 4 Life with Doubler Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = "Base ticket price $2. Drawings are held Nightly 9pm ET."  
    cash_add = "Available add on- Doubler $1 extra"
    rules_c4l = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/cash4life.html Good Luck!"    
    return (numbers_main, drawings_c4l, cash_add, rules_c4l)


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
        break
    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"\nLucky Cash Pop Number(s): {pop}"
    pop_drawings = "Ticket price to play from $1, $2, $5, or $10 per Cash Pop number played.\nDrawings held Daily every 4 minutes." 
    pop_win = "Winning amount printed alongside number on ticket. "  
    pop_rules = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/cashpop.html Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)
    

def pick6():
    p6_num = sorted(random.sample(range(1, 47), 6)) 
    p6_main = f"\nPick 6 with Double Play Lucky Numbers: {p6_num}"
    p6_draw = "Ticket price to play $2. Drawings held Mon. & Thurs 10:57pm ET."
    p6_add = "Available add on- Double Play $1"
    p6_rules = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/pick6lotto.html Good Luck!"
    return (p6_main, p6_draw, p6_add, p6_rules)


def jersey5():
    jersey_num = sorted(random.sample(range(1, 46), 5))
    jersey_main = f"\nJersey Cash 5 with XTRA Lucky Numbers: {jersey_num}"
    jersey_draw = "Ticket price to play $2. Drawings held Daily 10:57pm ET"
    jersey_add = "Available add on- XTRA $1"
    jersey_rules = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/jerseycash.html Good Luck!"
    return (jersey_main, jersey_draw, jersey_add, jersey_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:59pm ET Draw")
        print("2. Evening 10:57pm ET Draw")

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
    p4_main = f"\nPick 4 with Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket wager to play range- $0.50 to $5. Drawings held Daily."
    p4_fire_mid = "Available add ons- FIREBALL (doubles ticket amount)\nAlso, Instant Match $1."    
    p4_rules = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/pick4.html Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:59pm ET Draw")
        print("2. Evening 10:57pm ET Draw")

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
    p3_main = f"\nPick 3 with Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Ticket wager to play range- $0.50 to $5. Drawings held Daily."
    p3_fire_mid = "Available add ons- FIREBALL (doubles ticket amount)\nAlso, Instant Match $1."    
    p3_rules = "Official Rules and Play can be found- https://www.njlottery.com/en-us/drawgames/pick3.html Good Luck!"
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

def cash_4_life_summary():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    return ("Cash 4 Life", f"Numbers: {cash_main}, Cash Ball: {cash_ball}")

def cash_pop_summary():     
    pop = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"Number: {pop}")

def pick6_summary():
    p6_num = sorted(random.sample(range(1, 47), 6)) 
    return ("Pick 6", f"Numbers: {p6_num}")

def jersey5_summary():
    jersey_num = sorted(random.sample(range(1, 46), 5))
    return ("Jersey 5", f"Numbers: {jersey_num}")

def pick4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4 with Fireball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3 with Fireball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_summary,
    "Cash Pop": cash_pop_summary,
    "Pick 6": pick6_summary,
    "Jersey 5": jersey5_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary
}

# New Jersey Game Choices
nj_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: cash_4_life,
    4: cash_pop,
    5: pick6,
    6: jersey5,
    7: pick_4,    
    8: pick_3,    
    9: lambda: nj_lotto_draw_games[random.randint(1, 11)](),  
    10: lambda: [func() for func in summary_lotto_draw_games.values()] 
}   

# print the menu
def play_game():
    print("\nNew Jersey Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life with Doubler")
    print("4. Cash Pop")
    print("5. Pick 6 with Doubler")
    print("6. Jersey 5 with XTRA")
    print("7. Pick 4 with Fireball")        
    print("8. Pick 3 with Fireball")    
    print("9. Can't Decide? Try Random Game!!!")    
    print("10. How About Quick Pick All 8 Games")  
    
    #waiter
    while True:
        try:
            nj_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if nj_lotto_game_choice in nj_lotto_draw_games:                        
                result = nj_lotto_draw_games[nj_lotto_game_choice]()

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



