###########################################################################
###################### Wyoming Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/06/09
###########################################################################


import random

# Wyoming Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 8:59pm MT." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://wyolotto.com/games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. & Fri. 9pm MT."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://wyolotto.com/games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_for_life_Wy():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"Lucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Drawings are held Nightly about 8:38pm MT"    
    life_rules = f"Official Rules and Play can be found- https://wyolotto.com/games/lucky-for-life Good Luck!"    
    return (life_return, life_drawings, life_rules)


def cowboy_draw(): 
    cowboy_num1 = sorted(random.sample(range(1, 46), 5))
    cowboy_num2 = sorted(random.sample(range(1, 46), 5))
    cowboy_main = f"Cowboy Draw Lucky Numbers Set 1: {cowboy_num1}"
    cowboy_main2 = f"Cowboy Draw Lucky Numbers Set 2: {cowboy_num2}"
    cowboy_drawing = f"Ticket price for play- $5. Drawings held Mon. & Thur. 2pm MT"
    cowboy_rules = f"Official Rules and Play can be found- https://wyolotto.com/games/cowboy-draw/"
    return (cowboy_main, cowboy_main2, cowboy_drawing, cowboy_rules)


def two_by_two(): 
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    two_main = f"2 by 2 Lucky Red and White Numbers: Red- {two_num_rd}, White- {two_num_wt}"
    two_draw = f"Ticket price $1. Drawings held Daily around 8:30pm MT"
    two_rules = f"Official Rules and Play cab be found- https://wyolotto.com/games/2-by-2/"
    return (two_main, two_draw, two_rules)


# Summary For Each Game 
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

def cowboy_draw_summary(): 
    cowboy_num = sorted(random.sample(range(1, 46), 5))
    cowboy_num2 = sorted(random.sample(range(1, 46), 5))
    return ("Cowboy Draw", f"Set 1: {cowboy_num}, Set 2: {cowboy_num2}")

def two_by_two_summary():
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    return(f"2 by 2 Lucky Numbers: Red- {two_num_rd}, White- {two_num_wt}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_summary,
    "Cowboy Draw": cowboy_draw_summary,
    "2 by 2": two_by_two_summary
}


#draw games
wy_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lucky_for_life_Wy,
    4: cowboy_draw,
    5: two_by_two,
    6: lambda: wy_lotto_draw_games[random.randint(1, 5)](),
    7: lambda: [func() for func in summary_lotto_draw_games.values()]   
}

#print the menu
def play_game():
    print("\nWyoming Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. Cowboy Draw")
    print("5. 2 by 2")
    print("6. Can't Decide? Try Random Game!!!")
    print("7. How About Quick Pick All 5 Games")
    
    
    #waiter
    while True:
        try:
            wy_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if wy_lotto_game_choice in wy_lotto_draw_games:                        
                result = wy_lotto_draw_games[wy_lotto_game_choice]()

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
    
    

    















