###########################################################################
#################### Missouri Draw Lotto Games ############################
###########################################################################

###########################################################################
# last file update- 2025/05/24
###########################################################################


import random

# Missouri Games Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def cash_4_life_mo():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.sample(range(1, 5), 1)[0]
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    cash_add = f"Available add-on- EZ Match for $1 extra per play"
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:30pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://www.molottery.com/cash4life Good Luck!"    
    return (numbers_main, cash_add, drawings_c4l, rules_c4l)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def mo_lotto():
    lotto_main = sorted(random.sample(range(1, 45), 6))
    lotto_num_main = f"Missouri Lucky Lotto Numbers: {lotto_main}" 
    lotto_drawings = f"Base ticket price $1. Drawings are Wed. and Sat. at 8:59pm CT."
    lotto_add = f"Available add on- EZ Match for $1 extra per play"
    lotto_rules = f"Official Rules and Play can be found- https://www.molottery.com/lotto Good Luck!"
    return (lotto_num_main, lotto_drawings, lotto_add, lotto_rules)


def show_lotto():
    show_main = sorted(random.sample(range(1, 40), 5))
    show_num_main = f"Missouri Lucky Show Me Cash Lotto Numbers: {show_main}"
    show_drawings = f"Base ticket price $1. Drawings held daily at 8:59pm CT."
    show_add = f"Available add on- EZ Match for $1 extra per play."
    show_rules = f"Official Rules and Play can be found- https://www.molottery.com/show-me-cash Good Luck!"
    return (show_num_main, show_drawings, show_add, show_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:45pm CT Draw")
        print("2. Evening 8:59pm CT Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:45 pm CT Draw',
            2: 'Evening- 8:59pm CT Draw'
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
    p4_main = f"Pick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Front Pair, Back Pair, Front Three, Back Three, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1."
    p4_fire_mid = f"Available add on- EZ Match for $1 extra per play or Wild Ball (doubles the ticket price)."    
    p4_rules = f"Official Rules and Play can be found- https://www.molottery.com/pick4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 12:45pm CT Draw")
        print("2. Evening 8:59pm CT Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:45 pm CT Draw',
            2: 'Evening- 8:59pm CT Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)    
    p3_main = f"Pick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Front Pair, Back Pair, or Combo."
    p3_drawings = f"Base ticket prices are $.50 or $1."
    p3_fire_mid = f"Available add on- EZ Match for $1 extra per play or Wild Ball (doubles the ticket price)."    
    p3_rules = f"Official Rules and Play can be found- https://www.molottery.com/pick3 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire_mid, p3_rules)


mo_lotto_draw_games = {
    1: powerball,
    2: cash_4_life_mo,
    3: mega_millions,
    4: mo_lotto,
    5: show_lotto,
    6: pick_4,
    7: pick_3,


}





def play_game():
    print("Missouri Lotto Game Choices")
    print("1. Powerball")
    print("2. Cash 4 Life")
    print("3. Mega Millions")
    print("4. Lotto")
    print("5. Show Me Cash")
    print("6. Pick 4")
    print("7. Pick 3")



    while True:
            try:
                mo_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if mo_lotto_game_choice in mo_lotto_draw_games:
                    for result in mo_lotto_draw_games[mo_lotto_game_choice]():
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


