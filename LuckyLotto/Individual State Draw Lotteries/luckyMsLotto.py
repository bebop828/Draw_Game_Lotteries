import random


#need to verify draw times and cut-offs.


def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Available add on- Megaplier $1 extra."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.sample(range(1, 11), 1)[0]
    lotto_num = f"Lucky Lotto America with EZ-Match Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. and Sat. 9:15pm CT"    
    lotto_add = f"Available add on games- EZ-Match and All Star Bonus $1 extra each per play"
    lotto_rules = f"Official Rules and Play can be found- https://www.mslottery.com/games/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)

def match_5multi(): 
    match_main = sorted(random.sample(range(1, 38), 5))
    match_numbers_main = f"Lucky Match 5 with Multiplier Numbers: {match_main}"
    match_drawings = f"Base ticket price $2. Drawings held Daily 9:30pm CT."
    match_add = f"Available add on- Multiplier $1 extra"
    match_rules = f"Official Rules and Play can be found- https://www.mslottery.com/games/mm5 Good Luck!"
    return (match_numbers_main, match_drawings, match_add, match_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 2:30pm CT Draw")
        print("2. Evening 9:30pm CT Draw")
        
        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 2:30pm CT Draw',
            2: 'Evening- 9:30pm CT Draw'            
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
    c4_main = f"Cash 4 with Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = f"Now you have to decide to play these numbers Exact, Any, Exact/ Any, or Combo."
    c4_drawings = f"Base ticket prices are $.50 or $1."      
    c4_add = f"Available add on- FIREBALL (doubles the ticket price)"
    c4_rules = f"Official Rules and Play can be found- https://www.mslottery.com/games/cash-4/ Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_add, c4_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 2:30pm CT Draw")
        print("2. Evening 9:30pm CT Draw")
        
        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 2:30pm CT Draw',
            2: 'Evening- 9:30pm CT Draw'            
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break

    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1) 
    set_3 = random.sample(range(0, 10), 1)
    c3_main = f"Cash 3 with Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    c3_now = f"Now you have to decide to play these numbers Exact, Any, Exact/ Any, or Combo."
    c3_drawings = f"Base ticket prices are $.50 or $1."      
    c3_add = f"Available add on- FIREBALL (doubles the ticket price)"
    c3_rules = f"Official Rules and Play can be found-https://www.mslottery.com/games/cash-3/ Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_add, c3_rules)



ms_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: match_5multi,
    5: cash_4,
    6: cash_3,

}

def play_game():
    print("Mississippi Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America with EZ-Match")
    print("4. Match 5 with Multiplier")
    print("5. Cash 4 with FIREBALL")
    print("6. Cash 3 with FIREBALL")




    while True:
        try:
            ms_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if ms_lotto_game_choice in ms_lotto_draw_games:
                for result in ms_lotto_draw_games[ms_lotto_game_choice]():
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