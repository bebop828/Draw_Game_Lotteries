###########################################################################
################## Oregon Draw Lotto Games ################################
###########################################################################

###########################################################################
# last file update- 2025/07/10
# Oregon has Keno. 
# Keno not currently included in file
###########################################################################

import random

# Oregon Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available Add on- Powerplay $1 extra."    
    pb_official = "Official Rules and Play can be found- https://www.oregonlottery.org/jackpot/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.oregonlottery.org/jackpot/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def megabucks():
    mega_num = sorted(random.sample(range(1, 49), 6))
    mega_main = f"\nMegabucks Lucky Numbers: {mega_num}"
    mega_draw = "Ticket price to play $1. Drawings held Mon. Wed. & Sat."
    mega_add = "Available add on- Kicker $1"
    mega_rules = "Official Rules and Play can be found- https://www.oregonlottery.org/jackpot/megabucks/ Good Luck!"
    return (mega_main, mega_draw, mega_add, mega_rules)


def win_life():
    win_num = sorted(random.sample(range(1, 78), 4))
    win_main = f"\nWin for Life Lucky Numbers: {win_num}"
    win_draw = "Ticket price to play $2. Drawings held Mon. Wed. & Sat."
    win_rules = "Official Rules and Play can be found- https://www.oregonlottery.org/jackpot/win-for-life/ Good Luck!"
    return (win_main, win_draw, win_rules)


def cash_pop():    
    while True:
        try:
            print("Play up to 15 numbers per play")
            print("Wager amounts per play from $1, $2, $3, $4, $5, or $10")
            num_choices = int(input("How many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-15.")    
        break
    draw = sorted(random.sample(range(1, 16), num_choices))   
    draw_main = f"\nLucky Cash Pop Number(s): {draw}"     
    draw_win = "Winning amounts printed beside number on play ticket! "  
    draw_game = "Cash Pop Draws 16x Daily!"
    draw_rules = "Official Rules and Play can be found- https://www.oregonlottery.org/jackpot/cash-pop/ Good Luck!"    
    return (draw_main, draw_win, draw_game, draw_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1pm")
        print("2. Afternoon 4pm")
        print("3. Evening 7pm")
        print("4. Night 10pm")

        try:
            choice = int(input("Make selection and enter 1-4: ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4")
            continue

        game_time_mapping = {
            1: 'Mid-Day Draw',
            2: 'Afternoon Draw',
            3: 'Evening Draw',
            4: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please select a valid number 1-4")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    p4_main = f"\nPick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!"
    p4_drawings = f"Ticket wager amounts are $.50 or $1."       
    p4_rules = f"Official Rules and Play can be found- https://www.oregonlottery.org/jackpot/pick-4/ Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


# Oregon Game Summaries
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def megabucks_summary():
    mega_num = sorted(random.sample(range(1, 49), 6))
    return ("Megabucks", f"Numbers: {mega_num}")

def win_life_summary():
    win_num = sorted(random.sample(range(1, 78), 4))
    return ("Win for Life", f"Numbers: {win_num}")

def cash_pop_summary():
    draw = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"Number: {draw} ")

def pick4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Afternoon", "Evening", "Night"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

# Oregon Game Summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Megabucks": megabucks_summary,
    "Win for Life": win_life_summary,
    "Cash Pop": cash_pop_summary,
    "Pick 4": pick4_summary
}


# Oregon Game Choices
or_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: megabucks,
    4: win_life,
    5: cash_pop,
    6: pick_4,
    7: lambda: or_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]
}

# print the menu
def play_game():
    print("\nOregon Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Megabucks")
    print("4. Win for Life")
    print("5. Cash Pop")
    print("6. Pick 4")
    print("7. Can't Decide? Try Random Game!!!")        
    print("8. How About Quick Pick All 6 Games")    
    
    #waiter
    while True:
        try:
            or_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if or_lotto_game_choice in or_lotto_draw_games:                        
                result = or_lotto_draw_games[or_lotto_game_choice]()

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
          



