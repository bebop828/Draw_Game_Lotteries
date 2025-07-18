###################################################################
############### Illinois Draw Lotto Games #########################
###################################################################

###################################################################
# last file update- 2025/05/29
################################################################### 


import random

#Illinois Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add on- Powerplay $1 extra."    
    pb_official = "Official Rules and Play can be found- https://www.illinoislottery.com/dbg/play/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.illinoislottery.com/dbg/play/megamillions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def luckyday_lotto():
    while True: 
        print("\nSelect a game time to play:")
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
    lucky_num = sorted(random.sample(range(1, 46), 5))
    lucky_main = f"\nLucky Day Lotto Lucky Numbers for {game_time}: {lucky_num}"
    lucky_draw = "Ticket price to play $1. Drawings held everyday 2x a day"
    lucky_add = "Available add on- EZ Match for $1 per play"
    lucky_rules = "Official Rules and Gameplay can be found- https://www.illinoislottery.com/dbg/play/luckydaylotto Good Luck!"
    return (lucky_main, lucky_draw, lucky_add, lucky_rules)


def lotto_extrashot():
    lotto_num = sorted(random.sample(range(1, 51), 6))
    lotto_main = f"\nLotto with Extra Shot Lucky Numbers: {lotto_num}"
    lotto_draw = "Ticket price to play $2. Drawings held Mon. Thur. & Sat."
    lotto_add = "Available add on- Extra Shot $1"
    lotto_rules = "Official Rules and Gameplay can be found- https://www.illinoislottery.com/dbg/play/lotto Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def pick_3():
    while True: 
        print("\nSelect a game time to play:")
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
    p3_main = f"\nPick 3 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Ticket price range to play- $.50 - $5. Drawings held Daily."
    p3_fire = "Available add on- FIREBALL (doubles ticket amount)."   
    p3_rules = "Official Rules and Play can be found- https://www.illinoislottery.com/dbg/play/pick3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


def pick_4():
    while True: 
        print("\nSelect a game time to play:")
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
    p4_main = f"\nPick 4 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket price to play range $.50 - $5. Drawings held Daily."
    p4_fire_mid = "Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = "Official Rules and Play can be found- https://www.illinoislottery.com/dbg/play/pick4 Good Luck!"
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

def luckyday_lotto_summary():
    draw_time = random.choice(["Mid-Day", "Evening"])
    lucky_num = sorted(random.sample(range(1, 46), 5))
    return ("Lucky Day Lotto", f"Draw Time: {draw_time}, Numbers: {lucky_num}")

def lotto_extrashot_summary():
    lotto_num = sorted(random.sample(range(1, 51), 6))
    return ("Lotto with Extra Shot", f"Numbers: {lotto_num}")

def pick3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3 with Fireball", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

def pick4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4 with Fireball", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky Day Lotto": luckyday_lotto_summary,
    "Lotto with Extra Shot": lotto_extrashot_summary,
    "Pick 4 with Fireball": pick4_summary,
    "Pick 3 with Fireball": pick3_summary
}


# Illinois Game Choices
il_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: luckyday_lotto, 
    4: lotto_extrashot,
    5: pick_4,
    6: pick_3,
    7: lambda: il_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nIllinois Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky Day Lotto")
    print("4. Lotto with Extra Shot")
    print("5. Pick 4 with Fireball")
    print("6. Pick 3 with Fireball")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")


#waiter
    while True:
        try:
            il_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if il_lotto_game_choice in il_lotto_draw_games:                        
                result = il_lotto_draw_games[il_lotto_game_choice]()

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