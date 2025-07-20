###########################################################################
##################### Kentucky Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/07/20
###########################################################################


import random

# Kentucky Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon, Wed, & Sat about 11pm ET/10pm CT.\nDouble Play drawings are around 11:30pm ET/10:30pm CT." 
    pb_add = "Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = "Official Rules and Play can be found- https://play.kylottery.com/en-us/playnow/powerball.html Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri. 11pm ET/10pm CT."
    mm_add = "Megaplier available with every play."
    mm_rules = "Official Rules and Play can be found- https://play.kylottery.com/en-us/playnow/megamillions.html Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_popKy():
    while True:
        try:
            num_choices = int(input("\nHow many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number 1-15.")

    pop = sorted(random.sample(range(1, 16), k=num_choices))   
    pop_main = f"\nLucky Cash Pop Number(s) : {pop}"
    pop_drawings = "Players can wager from $1, $2, $5, or $10 bet amounts per Cash Pop number played. Multiple Drawings Everyday! " 
    pop_win = "Winning amount for each number will appear on ticket beside number.\nIf number is drawn you win the amount displayed. "  
    pop_rules = "Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/cashpop/index.html Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)
       

def lucky_for_life_ky():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"\nLucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = "Ticket price to play $2. Drawings are held Nightly about 10:35pm ET/9:35pm CT"    
    life_rules = "Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/luckyforlife/index.html Good Luck!"    
    return (life_return, life_drawings, life_rules)


def cash_ball():
    cash_main = sorted(random.sample(range(1, 36), 4))
    cash_ball_main = random.randint(1, 25)
    cash_return = f"\nCa$h Ball Lucky Numbers: {cash_main}, Lucky Ball: {cash_ball_main}."
    cash_drawings = "Ticket price to play $1." 
    cash_add = "Available add on- EZmatch $1 per play."   
    cash_rules = "Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/cashball/index.html Good Luck!"    
    return (cash_return, cash_drawings, cash_add, cash_rules)


def pick_3ky():
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
    p3_drawings = "Ticket wagers range from $.50 thru $5. Drawings held everyday." 
    p3_rules = "Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/pick3/index.html Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


def pick_4ky():
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
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket wagers range from $.50 thru $5. Drawings held everyday."        
    p4_rules = "Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/pick4/index.html Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


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
    spot_draw = "Ticket wager to play varies: $1-5, $10, or $20 per play!\nDrawings held Daily every 4 minutes!"
    spot_add = "Available add on: Bulls-Eye and Multiplier (Doubles the wager price)"
    spot_rules = "Official Rules and Play can be found- https://play.kylottery.com/en-us/playnow/keno.html Good Luck!"
    return(spot_main, spot_draw, spot_add, spot_rules)



# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def cash_popKy_summary():
    pop = random.randint(1, 14)
    return (f"Cash Pop (Single number): {pop}")

def lucky_for_life_ky_summary():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_main}, Lucky Ball: {lucky_ball}")

def cash_ball_summary():
    cash_main = sorted(random.sample(range(1, 36), 4))
    cash_ball_main = random.randint(1, 25)
    return ("Cash Ball", f"Numbers: {cash_main}, Cash Ball: {cash_ball_main}")

def pick3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def pick4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def keno_summary(): 
    spot_num = random.randint(1, 80)
    return ("Keno (Single Spot)", f"Number: {spot_num}") 
    

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash Pop": cash_popKy_summary,
    "Lucky for Life": lucky_for_life_ky_summary,
    "Cash Ball": cash_ball_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary,
    "Keno": keno_summary
}


# Kentucky Game Choices
ky_lotto_draw_games = {
    1: powerball,
    2: mega_millions,    
    3: cash_popKy,
    4: lucky_for_life_ky,
    5: cash_ball,
    6: pick_4ky,
    7: pick_3ky,
    8: keno,
    9: lambda: ky_lotto_draw_games[random.randint(1, 8)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()]
}


#the menu
def play_game():
    print("\nKentucky Lotto Game Choices: ")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash Pop")
    print("4. Lucky For Life")
    print("5. Ca$h Ball")
    print("6. Pick 4")
    print("7. Pick 3") 
    print("8. Keno")
    print("9. Can't Decide? Try Random Game!!!")
    print("10. How About Quick Pick All 8 Games")   

    #waiter
    while True:
        try:
            ky_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ky_lotto_game_choice in ky_lotto_draw_games:                        
                result = ky_lotto_draw_games[ky_lotto_game_choice]()

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
