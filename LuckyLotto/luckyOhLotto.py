###########################################################################
################## Ohio Draw Lotto Games ##################################
###########################################################################

###########################################################################
# last file update- 2025/07/10
# Ohio has Keno. 
# Keno not currently included in file
###########################################################################

import random

# Ohio Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET" 
    pb_add = "Available Add on- Powerplay $1 extra."    
    pb_official = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri. 11pm ET"
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_for_life():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"\nLucky Numbers for Lucky For Life: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = "Ticket price to play $2. Drawings held Daily."    
    life_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/lucky-for-life Good Luck!"    
    return (life_return, life_drawings, life_rules)


def lotto_classic():
    lotto_num = sorted(random.sample(range(1, 50), 6))
    lotto_main = f"\nClassic Lotto +Kicker Lucky Numbers: {lotto_num}"
    lotto_draw = "Ticket price to play $1. Drawings held Mon. Wed. & Sat. 7:05pm ET."
    lotto_add = "Available add on- Kicker $1"
    lotto_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/classic-lotto#tab1 Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def roll_cash5():
    roll_num = sorted(random.sample(range(1, 40), 5))
    roll_main = f"\nRolling Cash 5 Lucky Numbers: {roll_num}"
    roll_draw = "Ticket price to play $1. Drawings held Daily."
    roll_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/rolling-cash-5 Good Luck!"
    return (roll_main, roll_draw, roll_rules)


def pick_5():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:29pm ET")
        print("2. Evening 7:29pm ET")

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
    p5_now = "Multiple ways to Play and Win!!!"
    p5_drawings = "Ticket price to play $.50 or $1. Drawings held Daily."        
    p5_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/pick-5 Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_rules)    


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:29pm ET")
        print("2. Evening 7:29pm ET")

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
    p4_drawings = "Ticket price to play $.50 or $1. Drawings held Daily."        
    p4_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/pick-4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)    


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:29pm ET")
        print("2. Evening 7:29pm ET")

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
    p3_drawings = "Ticket price to play $.50 or $1. Drawings held Daily."        
    p3_rules = "Official Rules and Play can be found- https://www.ohiolottery.com/games/draw-games/pick-3 Good Luck!"
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

def lucky_for_life_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {lucky_ball}")

def lotto_classic_summary():
    lotto_num = sorted(random.sample(range(1, 50), 6))
    return ("Classic Lotto", f"Numbers: {lotto_num}")

def roll_cash5_summary():
    roll_num = sorted(random.sample(range(1, 40), 5))
    return ("Rolling Cash 5", f"Numbers: {roll_num}")

def pick5_summary():
    game_time = random.choice(['Mid-day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return (f"Pick 5 Lucky Numbers for {game_time}: {set_1}, {set_2}, {set_3}, {set_4}, {set_5}")

def pick4_summary():
    game_time = random.choice(['Mid-day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)    
    return (f"Pick 4 Lucky Numbers for {game_time}: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():
    game_time = random.choice(['Mid-day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)    
    return (f"Pick 3 Lucky Numbers for {game_time}: {set_1}, {set_2}, {set_3}")


# Ohio Game Summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_for_life_summary,
    "Classic Lotto": lotto_classic_summary,
    "Rolling Cash": roll_cash5_summary,
    "Pick 5": pick5_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary
}

# Ohio Game Choices
oh_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: lucky_for_life,
    4: lotto_classic,
    5: roll_cash5,
    6: pick_5,
    7: pick_4,
    8: pick_3,
    9: lambda: oh_lotto_draw_games[random.randint(1, 8)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()]
}

# print the menu
def play_game():
    print("\nOhio Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. Classic Lotto")
    print("5. Rolling Cash 5")
    print("6. Pick 5")
    print("7. Pick 4")        
    print("8. Pick 3")    
    print("9. Can't Decide? Try Random Game!!!")    
    print("10. How About Quick Pick All 8 Games") 
    
    
    #waiter
    while True:
        try:
            oh_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if oh_lotto_game_choice in oh_lotto_draw_games:                        
                result = oh_lotto_draw_games[oh_lotto_game_choice]()

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
          