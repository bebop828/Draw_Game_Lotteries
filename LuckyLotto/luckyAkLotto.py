###########################################################################
##################### Arkansas Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/07/14
###########################################################################

import random 

# Arkansas Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add on- Power Play $1 extra."
    pb_official = "Official Rules and Play can be found- https://www.myarkansaslottery.com/games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues & Fri."
    mm_add = "Megaplier available with every gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.myarkansaslottery.com/games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def ark_lotto():
    lotto_main = sorted(random.sample(range(1, 41), 6))
    lotto_numbers_main = f"\nLucky Lotto Arkansas Numbers: {lotto_main}"
    lotto_drawings = "Base ticket price $2. Drawings are held Wed. & Sat. 9:00pm CT."    
    lotto_rules = "Official Rules and Play can be found- https://www.myarkansaslottery.com/games/lotto Good Luck!"
    return (lotto_numbers_main, lotto_drawings, lotto_rules)


def nat_stJack():
    nat_main = sorted(random.sample(range(1, 40), 5))
    nat_numbers_main = f"\nLucky Natural State Jackpot Numbers: {nat_main}"
    nat_drawings = "Ticket price to play $1. Drawings are held Daily 8:00pm CT."    
    nat_rules = "Official Rules and Play can be found- https://www.myarkansaslottery.com/games/natural-state-jackpot Good Luck!"
    return (nat_numbers_main, nat_drawings, nat_rules)


def lucky_4Life():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"\nLucky For Life Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = "Ticket price to play $2. Drawings are held Nightly 9:30pm CT."    
    life_rules = "Official Rules and Play can be found- https://www.myarkansaslottery.com/games/lucky-for-life Good Luck!"    
    return (life_return, life_drawings, life_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 12:59pm Draw")
        print("2. Evening 6:59pm Draw")
        
        try:
            choice = int(input("Make selection and enter 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter 1 or 2")
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
    c4_main = f"\nCash 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = "Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    c4_drawings = "Ticket prices to play are $.50 or $1. \nMid-Day 12:59pm CT Drawings Held Monday-Saturday.\nEvening 6:59pm CT Drawings Held Monday-Sunday"     
    c4_rules = "Official Rules and Play can be found- https://www.myarkansaslottery.com/games/cash-4 Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 12:59pm CT Draw")
        print("2. Evening 6:59pm CT Draw")
        
        try:
            choice = int(input("Make selection and enter 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter 1 or 2")
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
    c3_main = f"\nCash 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    c3_now = "Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    c3_drawings = "Base ticket prices are $.50 or $1.\nMid-Day 12:59pm CT Drawings Held Monday-Saturday.\nEvening 6:59pm CT Drawings Held Monday-Sunday"      
    c3_rules = "Official Rules and Play can be found-https://www.myarkansaslottery.com/games/cash-3 Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def ark_lotto_summary():
    lotto_main = sorted(random.sample(range(1, 41), 6))
    return ("Arkansas Lotto", f"Numbers: {lotto_main}")

def nat_stJack_summary():
    nat_main = sorted(random.sample(range(1, 40), 5))
    return ("Natural State Jackpot", f"Numbers: {nat_main}")

def lucky_4Life_summary():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_main}, Lucky Ball: {lucky_ball}")

def cash4_summary(): 
    draw_time4 = random.choice(["Mid-Day", "Evening"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Cash 4", f"{draw_time4}: Numbers: ({set_1}, {set_2}, {set_3}, {set_4})")

def cash3_summary():    
    draw_time = random.choice(["Mid-Day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Cash 3", f"{draw_time}: Numbers: ({set_1}, {set_2}, {set_3})")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Arkansas Lotto": ark_lotto_summary,
    "Natural State Jackpot": nat_stJack_summary,
    "Lucky for Life": lucky_4Life_summary,
    "Cash 4": cash4_summary,
    "Cash 3": cash3_summary    
}

#draw games
ak_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: ark_lotto,
    4: nat_stJack,
    5: lucky_4Life,
    6: cash_4,
    7: cash_3,
    8: lambda: ak_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]    
}

#the menu
def play_game(): 
    print("\nArkansas Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto Arkansas")
    print("4. Natural State Jackpot")
    print("5. Lucky For Life")
    print("6. Cash 4")
    print("7. Cash 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")

    #waiter
    while True:
        try:
            ak_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ak_lotto_game_choice in ak_lotto_draw_games:                        
                result = ak_lotto_draw_games[ak_lotto_game_choice]()

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

