###########################################################################
################## North Dakota  Draw Lotto Games ##########################
###########################################################################

###########################################################################
# last file update- 2025/06/29
########################################################################### 


import random

# North Dakota Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.lottery.nd.gov/games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.lottery.nd.gov/games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = f"Ticket price $1. Drawings are held Mon. Wed. & Sat."
    lotto_add = f"Add on- All-Star Multiplier available for $1 extra"
    lotto_rules = f"Official Rules and Play can be found- https://www.lottery.nd.gov/games/lotto-america Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"Lucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = f"Ticket price $2. Drawings held Daily"
    lucky_rules = f"Official Rules and Gameplay can be found- https://www.lottery.nd.gov/games/lucky-for-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def two_by_two(): 
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    two_main = f"2 by 2 Lucky Red and White Numbers: Red- {two_num_rd}, White- {two_num_wt}"
    two_draw = f"Ticket price $1. Drawings held Daily around 8:30pm MT"
    two_rules = f"Official Rules and Play cab be found- https://www.lottery.nd.gov/games/2-by-2 Good Luck!"
    return (two_main, two_draw, two_rules)


# North Dakota Game Summaries
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
    lotto_star = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {lotto_star}")

def lucky_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    life_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {life_ball}")

def two_by_two_summary():
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    return(f"2 by 2 Lucky Numbers: Red- {two_num_rd}, White- {two_num_wt}")


#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "2 by 2": two_by_two_summary
}

#draw games
nd_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: two_by_two,
    6: lambda: nd_lotto_draw_games[random.randint(1, 5)](),
    7: lambda: [func() for func in summary_lotto_draw_games.values()] 
}

#print the menu
def play_game():
    print("\nNorth Dakota Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. 2 by 2")
    print("6. Can't Decide? Try a Random Game!!!")
    print("7. How About Random All 5 Games")
    
    #waiter
    while True:
        try:
            nd_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if nd_lotto_game_choice in nd_lotto_draw_games:                        
                result = nd_lotto_draw_games[nd_lotto_game_choice]()

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