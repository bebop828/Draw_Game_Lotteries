###################################################################
################## Delaware Draw Lotto Games ######################
###################################################################

###################################################################
# last file update- 2025/05/26
# Delaware has Keno Draw Game. 
# Keno not included currently with file. Will update another date
###################################################################


import random

#Delaware Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = "Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri. 11pm ET."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Mega-Millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"\nLotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = "Ticket price $1. Drawings are held Mon. Wed. & Sat. 11pm ET"
    lotto_add = "Add-on- All-Star Multiplier available for $1 extra"
    lotto_rules = "Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Lotto-America Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)
    

def multi_win():
    multi_num = sorted(random.sample(range(1, 36), 6))
    multi_main = f"\nMulti-Win Lotto Lucky Numbers: {multi_num}"
    multi_draw = f"Ticket price to play $2. Drawings held Daily 7:57pm ET"
    multi_rules = f"Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Multi-Win-Lotto Good Luck!"
    return (multi_main, multi_draw, multi_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"\nLucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price to play $2. Drawings held Daily 10:38pm ET"
    lucky_rules = "Official Rules and Gameplay can be found- https://www.delottery.com/Drawing-Games/Lucky-For-Life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def play3():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Night Draw")

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
    p3_main = f"\nPlay 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Ticket price tio play $.50 or $1. Drawings held Daily."      
    p3_rules = "Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Play-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


def play4():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Night Draw")

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
    p4_main = f"\nPlay 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket price to play $.50 or $1. Drawings held Daily."      
    p4_rules = "Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Play-4 Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_rules)


def play5():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Night Draw")

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
    p5_main = f"Play 5 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = "Multiple ways to Play and Win!!!"
    p5_drawings = "Ticket price to play $.50 or $1. Drawings held Daily."      
    p5_rules = "Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Play-5 Good Luck!"       
    return (p5_main, p5_now, p5_drawings, p5_rules)


def keno():
    while True: 
        try:
            num_choices = int(input("How many spots would you like to play? Choose 1-10: ").strip())
            if num_choices < 1 or num_choices > 10:
                print("Invalid selection. Please enter a number 1-10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-10")

    spot_num = sorted(random.sample(range(1, 81), num_choices))
    spot_main = f"\nHere are your Keno Lucky Numbers: {spot_num}"
    spot_draw = "Ticket wager to play varies: $1-5, $10, or $20 per play!\nDrawings held Daily every 4 minutes!"
    spot_add = "Available add on: Bonus (Doubles the ticket price)"
    spot_rules = "Official Rules and Play can be found- https://www.delottery.com/Keno Good Luck!"
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

def lotto_summary():
    lotto_main = sorted(random.sample(range(1, 53), 5))
    lotto_star = random.sample(range(1, 11), 1)[0]
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {lotto_star}")

def multi_win_summary():
    multiWin_num = sorted(random.sample(range(1, 36), 6))
    return ("Multi-Win", f"Numbers: {multiWin_num}")

def lucky_life_summary():
    luckyL_num = sorted(random.sample(range(1, 49), 5))
    luckyL_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {luckyL_num}, Lucky Ball: {luckyL_ball}")

def play3_summary():    
    draw_time = random.choice(["Day", "Night"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Play 3", f"{draw_time}: Numbers: ({set_1}, {set_2}, {set_3})")

def play4_summary(): 
    draw_time4 = random.choice(["Day", "Night"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Play 4", f"{draw_time4}: Numbers: ({set_1}, {set_2}, {set_3}, {set_4})")

def play5_summary(): 
    draw_time5 = random.choice(["Day", "Night"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return ("Play 5", f"{draw_time5}: Numbers: ({set_1}, {set_2}, {set_3}, {set_4}, {set_5})")

def keno_summary(): 
    spot_num = random.randint(1, 80)
    return ("Keno (Single Spot)", f"Number: {spot_num}") 

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Multi-Win": multi_win_summary,
    "Lucky for Life": lucky_life_summary,
    "Play 5": play5_summary,
    "Play 4": play4_summary,
    "Play 3": play3_summary,
    "Keno": keno_summary
}

#draw games
de_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: multi_win,
    5: lucky_life,
    6: play5,
    7: play4,
    8: play3,
    9: keno, 
    10: lambda: de_lotto_draw_games[random.randint(1, 9)](),
    11: lambda: [func() for func in summary_lotto_draw_games.values()]
        
}

#print the menu
def play_game():
    print("\nDelaware Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Multi-Win Lotto")
    print("5. Lucky for Life")
    print("6. Play 5")
    print("7. Play 4")
    print("8. Play 3")
    print("9. Keno")
    print("10. Can't Decide? Try Random Game!!!")
    print("11. How About Quick Pick All 9 Games")
    
    
    #waiter
    while True:
        try:
            de_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if de_lotto_game_choice in de_lotto_draw_games:                        
                result = de_lotto_draw_games[de_lotto_game_choice]()

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