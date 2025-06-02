###########################################################################
################# North Carolina Draw Lotto Games #########################
###########################################################################

###########################################################################
# last file update- 2025/06/02
# NC has Keno. Keno not currently included with file
###########################################################################


import random

# North Carolina Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://nclottery.com/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://nclottery.com/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def lucky_for_life_nc():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"Lucky Numbers for Lucky For Life: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut-off time for retail play is 9:30pm ET each night. Drawings are held Nightly 10:30pm ET."    
    life_rules = f"Official Rules and Play can be found- https://nclottery.com/lucky-for-life-how-to-play Good Luck!"    
    return (life_return, life_drawings, life_rules)

def cash_5():
    cash_5_main = sorted(random.sample(range(1, 44), 5))
    cash_5_numbers_main = f"Cash 5 with Double Play Lucky Numbers: {cash_5_main}"
    cash_5_drawings = f"Base ticket price $1. Drawings held everyday at 11:22pm ET."
    cash_5_add = f"Available add on- EZmatch and/or Double Play for $1 each extra."
    cash_5_rules = f"Official Rules and Play can be found- https://nclottery.com/cash5-how-to-play Good Luck!"    
    return (cash_5_numbers_main, cash_5_drawings, cash_5_add, cash_5_rules)


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
    p3_main = f"Pick 3 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Multiple ways to Play and Win!"
    p3_drawings = f"Base ticket prices $.50 or $1. Drawings held 2x a day, daily!"
    p3_fire = f"Available add on- FIREBALL (doubles ticket amount)."   
    p3_rules = f"Official Rules and Play can be found- https://nclottery.com/pick3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


def pick_4():
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
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    p4_main = f"Pick 4 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple ways to Play and Win!"
    p4_drawings = f"Base ticket prices are $.50 or $1. Drawings held 2x a day, daily!"
    p4_fire_mid = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://nclottery.com/pick4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lucky_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    life_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {life_ball}")

def cash_5_summary():
    cash_5_main = sorted(random.sample(range(1, 44), 5))
    return ("Cash 5", f"Numbers: {cash_5_main}")

def pick3_summary():    
    draw_time = random.choice(["Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3 with Fireball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def pick4_summary(): 
    draw_time4 = random.choice(["Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4 with Fireball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_summary,
    "Cash 5": cash_5_summary,
    "Pick 3": pick3_summary,
    "Pick 4": pick4_summary
}


# North Carolina Game Choices
nc_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lucky_for_life_nc,
    4: cash_5,
    5: pick_3,
    6: pick_4,
    7: lambda: nc_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]
}

# print the menu
def play_game():
    print("North Carolina Lotto:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky For Life")
    print("4. Cash 5 Double Play")
    print("5. Pick 3")
    print("6. Pick 4 ")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")

    # waiter
    while True:
        try:
            nc_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if nc_lotto_game_choice in nc_lotto_draw_games:                        
                result = nc_lotto_draw_games[nc_lotto_game_choice]()

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
                print("Ok! Good Luck!!!")
                return   
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()