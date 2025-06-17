###########################################################################
################ New Mexico Draw Lotto Games ##############################
###########################################################################

###########################################################################
# last file update- 2025/06/17
###########################################################################  



import random

# New Mexico Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 8:59pm MT" 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.nmlottery.com/games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Drawings are held Tues. Fri. 9pm MT."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.nmlottery.com/games/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = f"Ticket price $1. Drawings are held Mon. Wed. & Sat around 9:15pm MT."
    lotto_add = f"Add-on- All-Star Multiplier available for $1 extra"
    lotto_rules = f"Official Rules and Play can be found- https://www.nmlottery.com/games/lotto-america/ Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def roadrun_cash():
    road_num = sorted(random.sample(range(1, 38), 5))
    road_main = f"Roadrunner Cash Lucky Numbers: {road_num}"
    road_draw = f"Ticket price to play $1. Drawings are held Daily 9:30pm MT."
    road_rules = f"Official Rules and Play can be found- https://www.nmlottery.com/games/roadrunner-cash/"
    return (road_main, road_draw, road_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw 1pm")
        print("2. Evening Draw 9:30pm")

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
    p4_main = f"Pick 4 Plus Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple ways to Play and Win!"
    p4_drawings = f"Ticket wager $1. Drawings held Daily!"        
    p4_rules = f"Official Rules and Play can be found- https://www.nmlottery.com/games/pick-4-plus Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw 1pm")
        print("2. Evening Draw 9:30pm")

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
    p3_main = f"Pick 3 Plus Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Multiple ways to Play and Win!"
    p3_drawings = f"Ticket wager $1. Drawings held Daily!"      
    p3_rules = f"Official Rules and Play can be found- https://www.nmlottery.com/games/pick-3-plus Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


#summaries for each game
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

def roadrun_cash_summary():
    road_num = sorted(random.sample(range(1, 38), 5))
    return ("Roadrunner Cash:", f"Numbers: {road_num}")

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
    "Roadrunner Cash": roadrun_cash_summary,
    "Pick 4 Plus": pick4_summary,
    "Pick 3 Plus": pick3_summary
}


# Iowa Lotto Draw Games
nm_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: roadrun_cash,
    5: pick_4,
    6: pick_3, 
    7: lambda: nm_lotto_draw_games[random.randint(1,6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]    
}


# print the menu
def play_game():
    print("\nNew Mexico Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Roadrunner Cash")
    print("5. Pick 4")
    print("6. Pick 3")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")
    
    
    # waiter
    while True:
        try:
            nm_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if nm_lotto_game_choice in nm_lotto_draw_games:
                result = nm_lotto_draw_games[nm_lotto_game_choice]()
                
                if isinstance(result, list):
                    for res in result:
                        if isinstance(res, tuple) and len(res) == 2:
                            print(f"{res[0]} - {res[1]}")
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
                print("That is not an acceptable responce. Please try again.")
                
if __name__ == "__main__":
    main()