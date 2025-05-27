###########################################################################
##################### Colorado Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/27
###########################################################################

import random

# Colorado Game Choices
def powerball(): 
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Cut-off time to play is 8pm MT night of drawings. Drawings are held Tues and Fri."
    mm_add = f"Megaplier comes with every ticket purchase."
    mm_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/megamillions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_for_life_co():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"Lucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut-off time to play is 7:30pm MT each night. Drawings are held Nightly 8:30pm MT."    
    life_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/luckyforlife/ Good Luck!"    
    return (life_return, life_drawings, life_rules)


def co_lotto():
    co_main = sorted(random.sample(range(1, 41), 6))
    co_return = f"Colorado Lotto+ Lucky Numbers: {co_main}"
    co_draw = f"Base ticket cost $2. Top Prize up to $250,000. Drawings held Mon, Wed, Sat."
    co_add = f"Available add on- Play Plus $1"
    co_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/lotto/ Good Luck!"
    return(co_return, co_draw, co_add, co_rules)


def cash5(): 
    cash5_num = sorted(random.sample(range(1, 33), 5))
    cash5_return = f"Cash 5 Lucky Numbers: {cash5_num}"
    cash5_draw = f"Base ticket cost $1. Drawings are held nightly."
    cash5_add = f"Available add on- EZ Match $1 extra"
    cash5_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/cash5/"
    return (cash5_return, cash5_draw, cash5_add, cash5_rules)


def pick_3():
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
            1: 'Mid-Day',
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
    p3_main = f"Pick 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now decide if you play these numbers Exact, Any Order, Exact/Any Order, Front Pair, or Back Pair"
    p3_drawings = f"Ticket bet prices- $.50, $1, $2, or $5"      
    p3_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/pick3/ Good Luck!"    
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

def lucky_4Life_summary():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_main}, Lucky Ball: {lucky_ball}")

def co_lotto_summary():
    co_main = sorted(random.sample(range(1, 41), 6))
    return ("Colorado Lotto+", f"Numbers: {co_main}")

def cash5_summary(): 
    cash5_num = sorted(random.sample(range(1, 33), 5))
    return ("Cash 5", f"Numbers: {cash5_num}")

def pick3_summary():        
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Play 3", f"Numbers: ({set_1}, {set_2}, {set_3})")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_4Life_summary,
    "Colorado Lotto+": co_lotto_summary,
    "Cash 5": cash5_summary,
    "Pick 3": pick3_summary
}


#game choices
co_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lucky_for_life_co,
    4: co_lotto,
    5: cash5,
    6: pick_3,
    7: lambda: co_lotto_draw_games[random.randint(1, 6)](), 
    8: lambda: [func() for func in summary_lotto_draw_games.values()]  
}

#the menu
def play_game():
    print("Colorado Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. Colorado Lotto")
    print("5. Cash 5")
    print("6. Pick 3")  
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")  

    #waiter
    while True:
        try:
            co_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if co_lotto_game_choice in co_lotto_draw_games:                        
                result = co_lotto_draw_games[co_lotto_game_choice]()

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