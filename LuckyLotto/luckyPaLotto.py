###########################################################################
################## Pennsylvania Draw Lotto Games ##########################
###########################################################################

###########################################################################
# last file update- 2025/07/10
# Pennsylvania has Keno.
# Keno not currently included in file
###########################################################################


import random

# Pennsylvania Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/Powerball.aspx Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier available with every play."
    mm_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/Mega-Millions.aspx Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def cash_4_life():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.randint(1, 4)
    numbers_main = f"\nCash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = "Ticket price to play $2. Drawings are held Nightly."    
    rules_c4l = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/Cash4Life.aspx Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def match6():
    match_num = sorted(random.sample(range(1, 50), 6))
    match_main = f"\nMatch 6 Lucky Numbers: {match_num}"
    match_draw = "Ticket Price to play $2"
    match_info = "For each Match 6 Lotto game-grid played, \nyou will automatically receive two additional sets of six numbers randomly selected by the computer."
    match_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/Match-6.aspx Good Luck!"
    return (match_main, match_draw, match_info, match_rules)


def cash5():
    cash_num = sorted(random.sample(range(1, 44), 5))
    cash_main = f"\nCash 5 with Quick Cash Lucky Numbers: {cash_num}"
    cash_draw = "Ticket price to play $2. Drawing held Daily!"
    cash_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/Cash-5.aspx Good Luck!"
    return (cash_main, cash_draw, cash_rules)


def treasure_hunt():
    treasure_num = sorted(random.sample(range(1, 31), 5))
    treasure_main = f"\nTreasure Hunt Lucky Numbers: {treasure_num}"
    treasure_draw = "Ticket price to play $1. Drawings held Daily!"
    treasure_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/Treasure-Hunt.aspx Good Luck!"
    return (treasure_main, treasure_draw, treasure_rules)


def pick_5():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Evening Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
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
    p5_main = f"\nPick 5 with Wildball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = "Multiple ways to Play and Win!!!"
    p5_drawings = "Ticket price to play $1."
    p5_fire = "Available add on- WildBALL (doubles ticket amount)."    
    p5_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/PICK-5.aspx Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_fire, p5_rules)

def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Evening Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
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
    p4_main = f"\nPick 4 with Wildball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket price to play $1."
    p4_fire = "Available add on- WildBALL (doubles ticket amount)."    
    p4_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/PICK-4.aspx Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire, p4_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Evening Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
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
    p3_main = f"\nPick 3 with Wildball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Ticket price to play $1."
    p3_fire = "Available add on- WildBALL (doubles ticket amount)."    
    p3_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/PICK-3.aspx Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


def pick_2():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Evening Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)           
    p2_main = f"\nPick 2 with Wildball Lucky Numbers for {game_time}: {set_1, set_2}"
    p2_now = "Multiple ways to Play and Win!!!"
    p2_drawings = "Ticket price to play $1."
    p2_fire = "Available add on- WildBALL (doubles ticket amount)."    
    p2_rules = "Official Rules and Play can be found- https://www.palottery.pa.gov/Draw-Games/PICK-3.aspx Good Luck!"
    return (p2_main, p2_now, p2_drawings, p2_fire, p2_rules)


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

def match6_summary():
    match_num = sorted(random.sample(range(1, 50), 6))
    return ("Match 6", f"Numbers: {match_num}")

def cash5_summary():
    cash_num = sorted(random.sample(range(1, 44), 5))
    return ("Cash 5", f"Numbers: {cash_num}")

def treasure_hunt_summary():
    treasure_num = sorted(random.sample(range(1, 31), 5))
    return ("Treasure Hunt", f"Numbers: {treasure_num}")

def pick5_summary(): 
    draw_time5 = random.choice(["Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return ("Pick 5 with Wildball", f"{draw_time5}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}, {set_5}")

def pick4_summary(): 
    draw_time4 = random.choice(["Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4 with Wildball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():    
    draw_time = random.choice(["Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3 with Wildball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def pick2_summary(): 
    draw_time = random.choice(["Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    return ("Pick 2 with Wildball", f"{draw_time}: Numbers: {set_1}, {set_2}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Cash 4 Life": cash_4_life_summary,
    "Match 6": match6_summary,
    "Cash 5": cash5_summary,
    "Treasure Hunt": treasure_hunt_summary,
    "Pick 5": pick5_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary,
    "Pick 2": pick2_summary    
}

# Pennsylvania Game Choices
pa_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: cash_4_life,
    4: match6,
    5: cash5,
    6: treasure_hunt,
    7: pick_5,    
    8: pick_4,    
    9: pick_3,    
    10: pick_2,    
    11: lambda: pa_lotto_draw_games[random.randint(1, 10)](),
    12: lambda: [func() for func in summary_lotto_draw_games.values()]      
}

# print the menu
def play_game():
    print("\nPennsylvania Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. Match 6")
    print("5. Cash 5")
    print("6. Treasure Hunt")
    print("7. Pick 5")        
    print("8. Pick 4")    
    print("9. Pick 3")    
    print("10. Pick 2")    
    print("11. Can't Decide? Try Random Game!!!")
    print("12. How About Quick Pick All 10 Games")
   
    #waiter
    while True:
        try:
            pa_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if pa_lotto_game_choice in pa_lotto_draw_games:                        
                result = pa_lotto_draw_games[pa_lotto_game_choice]()

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





