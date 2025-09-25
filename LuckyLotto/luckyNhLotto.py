###########################################################################
############ New Hampshire Draw Lotto Games ###############################
###########################################################################

###########################################################################
# last file update- 2025/09/24
###########################################################################

import random

# New Hampshire Draw Games
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available Add on- Powerplay $1 extra."    
    pb_official = "Official Rules and Play can be found- https://www.nhlottery.com/game/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.nhlottery.com/game/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"\nLucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price $2. Drawings held Daily."
    lucky_rules = "Official Rules and Gameplay can be found- https://www.nhlottery.com/game/lucky-for-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def mega_bucks():
    bucks_num = sorted(random.sample(range(1, 42), 5))
    bucks_mega = random.randint(1, 6)
    bucks_main = f"\nLucky MegaBucks Numbers: {bucks_num}, Mega Number: {bucks_mega}"
    bucks_draw = "Ticket price to play $2. Drawings held Mon. Wed. & Sat."
    bucks_rules = "Official Rules and Play can be found- https://www.nhlottery.com/game/megabucks Good Luck!"
    return (bucks_main, bucks_draw, bucks_rules)

    
def gimme():
    gimme_num = sorted(random.sample(range(1, 40), 5))
    gimme_main = f"\nGimme 5 Lucky Numbers: {gimme_num}"
    gimme_draw = "Ticket price to play $1. Drawings held Mon-Fri."
    gimme_rules = "Official Rules and Play can be found- https://www.nhlottery.com/game/gimme-five Good Luck!"
    return (gimme_main, gimme_draw, gimme_rules)


def keno ():
    while True: 
        try:
            num_choices = int(input("How many spots would you like to play? Choose 1-12: ").strip())
            if num_choices < 1 or num_choices > 12:
                print("Invalid selection. Please enter a number 1-12.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-10")

    spot_num = sorted(random.sample(range(1, 81), num_choices))
    spot_main = f"\nHere are your Keno Lucky Numbers: {spot_num}"
    spot_draw = "Ticket Wager to play varies: $1, $2, $3, $4, $5, $10, $15, $20 or $25 per play!\nDrawings held daily from 11:05 AM to 1:00 AM Every 5 minutes!"
    spot_add = "Available add on: Keno 603 Plus (doubles the ticket price)"
    spot_rules = "Official Rules and Play can be found- https://www.nhlottery.com/game/keno Good Luck!"
    return(spot_main, spot_draw, spot_add, spot_rules)


def pick4():
    while True:        
        print("Select a game time to play:")
        print("1. Day")
        print("2. Evening")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day',
            2: 'Evening'
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
    p4_drawings = "Each play costs $0.50 minimum and increases in increments of $0.50, with a maximum bet of $5 per ticket.\nDrawings held Daily."       
    p4_rules = "Official Rules and Play can be found- https://www.nhlottery.com/game/pick-four Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_rules)


def pick3():
    while True: 
        print("Select a game time to play:")
        print("1. Day")
        print("2. Evening")

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
    p3_main = f"\nPick 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Each play costs $0.50 minimum and increases in increments of $0.50, with a maximum bet of $5 per ticket.\nDrawings held Daily."       
    p3_rules = "Official Rules and Play can be found- https://www.nhlottery.com/game/pick-three Good Luck!"    
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

def keno_summary(): 
    spot_num = random.randint(1, 80)
    return ("Keno (Single Spot)", f"Number: {spot_num}")

def pick4_summary(): 
    draw_time4 = random.choice(["Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4", f"{draw_time4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():    
    draw_time = random.choice(["Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"{draw_time}: Numbers: {set_1}, {set_2}, {set_3}")

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_summary,
    "MegaBucks": mega_bucks_summary,
    "Gimme 5": gimme_summary,
    "Keno": keno_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary
}

# New Hampshire Game Choices
nh_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: lucky_life,
    4: mega_bucks,
    5: gimme,
    6: keno,
    7: pick4, 
    8: pick3,
    9: lambda: nh_lotto_draw_games[random.randint(1, 8)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()]    
}

# print the menu
def play_game():
    print("\nNew Hampshire Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. MegaBucks")
    print("5. Gimme 5")
    print("6. Keno")    
    print("7. Pick 4")
    print("8. Pick 3")
    print("9. Can't Decide? Try Random Game!!!")
    print("10. How About Quick Pick All 8 Games")
    
    #waiter
    while True:
        try:
            nh_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if nh_lotto_game_choice in nh_lotto_draw_games:                        
                result = nh_lotto_draw_games[nh_lotto_game_choice]()

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
    

    
    