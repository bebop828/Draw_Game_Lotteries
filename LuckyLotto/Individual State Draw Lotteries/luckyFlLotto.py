###########################################################################
###################### Florida Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/07
###########################################################################


import random

# Florida Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def cash_4_life_fl():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.sample(range(1, 5), 1)[0]
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:30pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/cash4life Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def florida_lotto_x():
    main = sorted(random.sample(range(1, 54), 6))
    fl_lotto_main = f"Florida Lotto X with Double Play Lucky Numbers: {main}"
    fl_lotto_drawings = f"Base ticket price $2. Cut-off time to play is 10:55pm ET night of drawings. Drawings are held Wed. Sat. 11:15pm ET."
    fl_lotto_add = f"Available add ons- Double Play and EZmatch each for $1 extra."
    fl_lotto_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/florida-lotto Good Luck!"    
    return (fl_lotto_main, fl_lotto_drawings, fl_lotto_add,fl_lotto_rules)


def jackpot_triple_play():
    jackpot = sorted(random.sample(range(1, 47), 6))
    jack_main = f"Jackpot Triple Play with Combo Lucky Numbers: {jackpot}"
    jack_drawings = f"Base ticket price $1. Cut-off to play is 10:55pm ET night of drawings. Drawings held Tues. Fri. 11:15pm ET."
    jack_add = f"Available add on- Combo for $1 extra."
    jack_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/jackpot-triple-play Good Luck!"    
    return (jack_main, jack_drawings, jack_add, jack_rules)


def fantasy_5():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:05pm ET Draw")
        print("2. Evening 11:15pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 1:05pm ET Draw',
            2: 'Evening- 11:15pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    fantasy = sorted(random.sample(range(1, 37), 5))    
    fantasy_main = f"Lucky Fantasy 5 Numbers for {game_time}: {fantasy}"
    fantasy_drawings = f"Base ticket price $1. Cut-off time to play is 12:45pm ET Mid-day drawings and 10:55pm ET for evening."
    fantasy_add = f"Available add on- EZmatch $1 extra."
    fantasy_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/fantasy5 Good Luck!"    
    return (fantasy_main, fantasy_drawings, fantasy_add, fantasy_rules)

def cash_pop():    
    while True:
        try:
            num_choices = int(input("How many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-15.")
    
    while True: 
        print("Select a game time to play:")
        print("1. Morning 8:45am ET Draw")
        print("2. Matinee 11:45am ET Draw")
        print("3. Afternoon 2:45pm ET Draw")
        print("4. Evening 6:45pm ET Draw")
        print("5. Late Night 11:45pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter either (1-5)")
            continue

        game_time_mapping = {
            1: 'Morning- 8:45am ET Draw',
            2: 'Matinee- 11:45pm ET Draw',
            3: 'Afternoon 2:45pm ET Draw',
            4: 'Evening 6:45pm ET Draw',
            5: 'Late Night 11:45pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-5)")
            continue

        game_time = game_time_mapping[choice]
        break
    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"Lucky Cash Pop Number for {game_time}: {pop}"
    pop_drawings = f"Base ticket price varies. Players will choose from $1, $2, $5, or $10 bet amounts per Cash Pop numbers played." 
    pop_win = f"Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/cash-pop Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)


def pick_2():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm ET Draw")
        print("2. Evening 11:15pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 1:30pm ET Draw',
            2: 'Evening- 9:45pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    pick2_main = f"Lucky Pick 2 plus FIREBALL Numbers for {game_time}: {set_1, set_2}"
    pick_2_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Front/Back"
    pick2_drawings = f"Base ticket price $.50 or $1. Cut-off time to play is 1:17pm ET Mid-day drawings and 9:32pm ET for evening."
    pick2_add = f"Available add on- FIREBALL (doubles ticket amount)."
    pick2_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-2 Good Luck!"    
    return (pick2_main, pick_2_now, pick2_drawings, pick2_add, pick2_rules)


def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm ET Draw")
        print("2. Evening 11:15pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 1:30pm ET Draw',
            2: 'Evening- 9:45pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 plus Fireball Mid-Day Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo"
    p3_drawings = f"Base ticket prices $.50 or $1. Cut-off time to play is 1:19pm ET for Mid-Day Draw and 9:34pm for Evening."
    p3_fire = f"Available add on- FIREBALL (doubles ticket amount)."   
    p3_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm ET Draw")
        print("2. Evening 11:15pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 1:30pm ET Draw',
            2: 'Evening- 9:45pm ET Draw'
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
    p4_main = f"Pick 4 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:20pm ET for Mid_Day Draw and 9:35pm ET for Evening."
    p4_fire_mid = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


def pick_5():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day 1:30pm ET Draw")
        print("2. Evening 11:15pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 1:30pm ET Draw',
            2: 'Evening- 9:45pm ET Draw'
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
    p5_main = f"Pick 5 with Fireball for {game_time}: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    p5_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:18pm ET for Mid_Day Draw and 9:33pm ET for Evening."
    p5_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p5_rules = f"Official Rules and Play can be found- https://floridalottery.com/games/draw-games/pick-5 Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_fire, p5_rules)



fl_lotto_draw_games = {
    1: powerball,
    2: cash_4_life_fl,
    3: mega_millions,
    4: florida_lotto_x,
    5: jackpot_triple_play,
    6: fantasy_5,
    7: cash_pop,    
    8: pick_2,    
    9: pick_3,    
    10: pick_4,    
    11: pick_5    
}

def play_game():
    print("Florida Lotto Game Choices:")
    print("1. Powerball")
    print("2. Cash 4 Life")
    print("3. Mega Millions")
    print("4. Florida Lotto X")
    print("5. Jackpot Triple Play")
    print("6. Fantasy 5")
    print("7. Cash Pop")        
    print("8. Pick 2")    
    print("9. Pick 3")    
    print("10. Pick 4")    
    print("11. Pick 5")   


    while True:
        try:
            fl_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if fl_lotto_game_choice in fl_lotto_draw_games:
                for result in fl_lotto_draw_games[fl_lotto_game_choice]():
                    print(result)
                break  
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  
            print("Not a valid option. Please try again.")

    print("Curious if your numbers have been drawn before? Visit https://floridalottery.com/games/winning-numbers/history and look for yourself!!!")

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