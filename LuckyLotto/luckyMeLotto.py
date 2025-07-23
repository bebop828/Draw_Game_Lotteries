###########################################################################
################## Maine Draw Lotto Games #################################
###########################################################################

###########################################################################
# last file update- 2025/07/22
###########################################################################

import random

# Maine Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET" 
    pb_add = "Available Add ons- Powerplay and Double Play $1 each."    
    pb_official = "Official Rules and Play can be found- https://www.mainelottery.com/games/powerball.shtml Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri. 11pm ET"
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/megamillions.shtml Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_num = f"\nLucky Lotto America Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = "Ticket price to play $1. Drawings are held Mon. Wed. & Sat. 10:15pm ET"  
    lotto_add = "Available add on- All Star Bonus $1"      
    lotto_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/lotto-america.shtml Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"\nLucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price to play $2. Drawings held Daily 10:38pm ET"
    lucky_rules = "Official Rules and Gameplay can be found- https://www.mainelottery.com/games/lucky-for-life.html Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def mega_bucks():
    bucks_num = sorted(random.sample(range(1, 42), 5))
    bucks_mega = random.randint(1, 6)
    bucks_main = f"\nLucky MegaBucks Numbers: {bucks_num}, Mega Number: {bucks_mega}"
    bucks_draw = "Ticket price to play $2. Drawings held Mon. Wed. & Sat. 7:59pm ET"
    bucks_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/megabucksplus.shtml Good Luck!"
    return (bucks_main, bucks_draw, bucks_rules)

    
def gimme():
    gimme_num = sorted(random.sample(range(1, 40), 5))
    gimme_main = f"\nGimme 5 Lucky Numbers: {gimme_num}"
    gimme_draw = "Ticket price to play $1. Drawings held Mon-Fri 7pm ET"
    gimme_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/gimme5.html Good Luck!"
    return (gimme_main, gimme_draw, gimme_rules)


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
        print("Select a game time to play:")
        print("1. Early Bird 8:30am ET Draw")
        print("2. Brunch 11:30am ET Draw")
        print("3. Matinee 2:30pm ET Draw")
        print("4. Suppertime 6:30pm ET Draw")
        print("5. Night Owl 11:30pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter either (1-5)")
            continue

        game_time_mapping = {
            1: 'Early Bird',
            2: 'Brunch',
            3: 'Matinee',
            4: 'Suppertime',
            5: 'Night Owl'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-5)")
            continue

        game_time = game_time_mapping[choice]
        break
    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"\nLucky Cash Pop Number for {game_time}: {pop}"
    pop_drawings = "Ticket wager amount varies. Players will choose from $1, $2, $5, or $10 amounts per Cash Pop numbers played." 
    pop_win = "Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/CashPOP.shtml Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)

def pick4():
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
    p4_main = f"\nPick 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket price to play $1. Drawings held Daily."       
    p4_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/pickFourDailyNumbers.shtml Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


def pick3():
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
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Ticket prices to play $.50 or $1. Drawings held Daily."       
    p3_rules = "Official Rules and Play can be found- https://www.mainelottery.com/games/pickThreeDailyNumbers.shtml Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


# Maine Game Summaries
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lotto_summary():
    lotto_main = sorted(random.sample(range(1, 53), 5))
    lotto_star = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {lotto_star}")

def lucky_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    life_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {life_ball}")

def mega_bucks_summary():
    bucks_num = sorted(random.sample(range(1, 42), 5))
    bucks_mega = random.randint(1, 6)
    return ("MegaBucks", f"Numbers: {bucks_num}, Mega: {bucks_mega}")

def gimme_summary():
    gimme_num = sorted(random.sample(range(1, 40), 5))
    return ("Gimme 5", f"Numbers: {gimme_num}")

def cash_pop_summary(): 
    draw_time_pop = random.choice(["Early Bird", "Brunch", "Matinee", "Suppertime", "Night Owl"])
    pop = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"{draw_time_pop}: Numbers: {pop} ")

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
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "MegaBucks": mega_bucks_summary,
    "Gimme 5": gimme_summary,
    "Cash Pop": cash_pop_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary
}

# Maine Game Choices
me_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: mega_bucks,
    6: gimme,
    7: cash_pop,
    8: pick4, 
    9: pick3,
    10: lambda: me_lotto_draw_games[random.randint(1, 9)](),
    11: lambda: [func() for func in summary_lotto_draw_games.values()]    
}

# print the menu
def play_game():
    print("\nMaine Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. MegaBucks")
    print("6. Gimme 5")
    print("7. Cash Pop")
    print("8. Pick 4")
    print("9. Pick 3")
    print("10. Can't Decide? Try Random Game!!!")
    print("11. How About Quick Pick All 9 Games")
    
    #waiter
    while True:
        try:
            me_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if me_lotto_game_choice in me_lotto_draw_games:                        
                result = me_lotto_draw_games[me_lotto_game_choice]()

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