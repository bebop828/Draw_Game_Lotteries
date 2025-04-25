import random


#Va has Keno, I have not yet coded this game yet!
#need to check all the times for draws.


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


def cash_4_life_va():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.sample(range(1, 5), 1)[0]
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:30pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/cash4life Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def cash_popva():    
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
        print("1. Coffee Break 9am ET Draw")
        print("2. Lunch Break 12pm ET Draw")
        print("3. Rush Hour 5pm ET Draw")
        print("4. Prime Time 9pm ET Draw")
        print("5. After Hours 11:59pm ET Draw")

        try:
            choice = int(input("Make selection and enter (1-5): ").strip())
        except ValueError:
            print("Invalid input. Please enter either (1-5)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 1:05pm ET Draw',
            2: 'Evening- 11:15pm ET Draw',
            3: 'Afternoon 2:45am ET Draw',
            4: 'Evening 6:45am ET Draw',
            5: 'Late Night 11:45 ET Draw'
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
    pop_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/cashpop Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)


def bank_aMillion():
    main = sorted(random.sample(range(1, 41), 6))
    va_lotto_main = f"Lucky Numbers for Bank A Milion: {main}"
    va_lotto_drawings = f"Base ticket to play is $2. Play style varies."
    va_time= f"Cut-off time to play is 10:45pm ET night of drawings. Drawings are held Wed. Sat. 11:15pm ET."    
    va_lotto_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/bankamillion Good Luck!"    
    return (va_lotto_main, va_lotto_drawings, va_time,va_lotto_rules)


def cash_5EZva():
    main = sorted(random.sample(range(1, 46), 6))
    c5_lotto_main = f"Ca$h 5 with EZ Match Lucky Numbers: {main}"
    c5_lotto_drawings = f"Base ticket price $1."
    c5_lotto_add = f"Available add on- EZ Match for $1 extra."
    c5_lotto_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/cash5 Good Luck!"    
    return (c5_lotto_main, c5_lotto_drawings, c5_lotto_add, c5_lotto_rules)

def pick_5():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm ET Draw")
        print("2. Night 11pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day 1:59pm ET Draw',
            2: 'Night 11pm ET Draw'
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
    p5_now = f"Now you have to decide to play these numbers Exact, Any Order, or 50/50."
    p5_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:53pm ET for Day Drawings and 10:45pm ET for Night Draws."
    p5_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p5_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/pick5 Good Luck!"
    return (p5_main, p5_now, p5_drawings, p5_fire, p5_rules)

def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm ET Draw")
        print("2. Night 11pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day 1:59pm ET Draw',
            2: 'Night 11pm ET Draw'
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
    p4_main = f"Pick 4 with Fireball for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, or Combo."
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:53pm ET for Day Drawings and 10:45pm ET for Night Draws."
    p4_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/pick4 Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire, p4_rules)

def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm ET Draw")
        print("2. Night 11pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day 1:59pm ET Draw',
            2: 'Night 11pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)        
    p3_main = f"Pick 3 with Fireball for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, Combo, or Pairs."
    p3_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:53pm ET for Day Drawings and 10:45pm ET for Night Draws."
    p3_fire = f"Available add on- FIREBALL (doubles ticket amount)."    
    p3_rules = f"Official Rules and Play can be found- https://www.valottery.com/data/draw-games/pick3 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)





va_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: cash_4_life_va,
    4: cash_popva,
    5: bank_aMillion,
    6: cash_5EZva,
    7: pick_5,
    8: pick_4,
    9: pick_3    
}



def play_game():
    print("Virgina Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Mllions")
    print("3. Cash 4 Life")
    print("4. Cash Pop")
    print("5. Bank A Million")
    print("6. Ca$h 5 with EZ Match")
    print("7. Pick 5 with FIREBALL")
    print("8. Pick 4 with FIREBALL")
    print("9. Pick 3 with FIREBALL")


    while True:
        try:
            va_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if va_lotto_game_choice in va_lotto_draw_games:
                for result in va_lotto_draw_games[va_lotto_game_choice]():
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