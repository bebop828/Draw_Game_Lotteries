###########################################################################
#################### Gerorgia Draw Lotto Games ############################
###########################################################################

###########################################################################
# last file update- 2025/05/07
###########################################################################

import random

# Georgia Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def cash_4_life_ga():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.sample(range(1, 5), 1)[0]
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:45pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/cash-for-life.html#tab-howToPlay Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def fantasy_5_ga():
    fantasy_5_ga = sorted(random.sample(range(1, 43), 5))    
    fantasy_5_gaMain = f"Georgia Fantasy 5 Lucky Numbers: {fantasy_5_ga}"
    fantasy_5_gaDrawings = f"Base ticket price $1. Cut-off time to play is 10:45pm ET daily. Drawings held Daily 11:34pm ET."
    fantasy_5_gaAdd = f"Available add on- Ca$h Match $1 extra."
    fantasy_5_gaRules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/fantasy-five.html#tab-howToPlay"    
    return (fantasy_5_gaMain, fantasy_5_gaDrawings, fantasy_5_gaAdd, fantasy_5_gaRules)


def georgia_5():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:29pm ET Draw")
        print("2. Evening 6:59pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:29pm ET Draw',
            2: 'Evening- 6:59pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    set_5 = random.sample(range(0, 10), 1)
    georgia_5_main = f"Georgia 5 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    georgia_5_drawings = f"Base ticket price $1.  Drawings held daily 12:29pm ET."
    georgia_5_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/georgia-five.html Good Luck!" 
    return ( georgia_5_main, georgia_5_drawings, georgia_5_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 12:29pm ET Draw")
        print("2. Evening 6:59pm ET Draw")
        print("3. Night 11:34pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:29pm ET Draw',
            2: 'Evening- 6:59pm ET Draw',
            3: 'Night 11:34pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break

    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1) 
    set_3 = random.sample(range(0, 10), 1)
    c3_main = f"Cash 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    c3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Combo, 1 off, or Pairs"
    c3_drawings = f"Ticket prices are $.50 or $1."
    c3_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/cash-three.html#tab-howToPlay Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 1:30pm ET Draw")
        print("2. Evening 6:59pm ET Draw")
        print("3. Night 11:34pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:29pm ET Draw',
            2: 'Evening- 6:59pm ET Draw',
            3: 'Night 11:34pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break

    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1) 
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    c4_main = f"Cash 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    c4_drawings = f"Base ticket prices are $.50 or $1."      
    c4_rules = f"Official Rules and Play can be found- https://www.galottery.com/en-us/games/draw-games/cash-four.html#tab-howToPlay Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_rules)


ga_lotto_draw_games = {
    1: powerball, 
    2: cash_4_life_ga,
    3: mega_millions,
    4: fantasy_5_ga,
    5: georgia_5,
    6: cash_3,
    7: cash_4        
}

def play_game():
    print("Georgia Lotto Game Choices:")
    print("1. Powerball")
    print("2. Cash 4 Life")
    print("3. Mega Millions")
    print("4. Fantasy 5")
    print("5. Georgia 5")    
    print("6. Cash 3")    
    print("7. Cash 4")    

    while True:
            try:
                ga_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if ga_lotto_game_choice in ga_lotto_draw_games:
                    for result in ga_lotto_draw_games[ga_lotto_game_choice]():
                        print(result)
                    break  
                else:
                    print("Not a valid option. Please try again.")
            except ValueError:  
                print("Not a valid option. Please try again.")

    
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
