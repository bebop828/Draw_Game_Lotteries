




import random

# North Carolina
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

def lucky_for_life_nc():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19), 1)[0]
    life_return = f"Lucky Numbers for Lucky For Life: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut-off time to play is 9:30pm ET each night. Drawings are held Nightly 10:30pm ET."    
    life_rules = f"Official Rules and Play can be found- https://nclottery.com/lucky-for-life-how-to-play Good Luck!"    
    return (life_return, life_drawings, life_rules)

def cash_5():
    cash_5_main = sorted(random.sample(range(1, 44), 5))
    cash_5_numbers_main = f"Fantasy 5 Evening Lucky Numbers: {cash_5_main}"
    cash_5_drawings = f"Base ticket price $1. Cut-off time to play is 10:59pm nightly. Drawings held everyday at 11:22pm ET."
    cash_5_add = f"Available add on- EZmatch and/or Double Play for $1 each extra."
    cash_5_rules = f"Official Rules and Play can be found- https://nclottery.com/cash5-how-to-play Good Luck!"    
    return (cash_5_numbers_main, cash_5_drawings, cash_5_add, cash_5_rules)


def pick_4():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Night Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main = f"Pick 4 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, Pairs (Front/Back), or Combo"
    p4_drawings = f"Base ticket prices $.50 or $1. Drawings held Everyday!"
    p4_fire = f"Available add on- FIREBALL (doubles ticket amount)."   
    p4_rules = f"Official Rules and Play can be found- https://nclottery.com/pick4 Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_fire, p4_rules)

def pick_3():
    while True: 
        print("Select a game time to play:")
        print("1. Day Draw")
        print("2. Night Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 plus Fireball Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, Pairs (Front/Back), or Combo"
    p3_drawings = f"Base ticket prices $.50 or $1. Drawings held Everyday!"
    p3_fire = f"Available add on- FIREBALL (doubles ticket amount)."   
    p3_rules = f"Official Rules and Play can be found- https://nclottery.com/pick3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)

nc_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lucky_for_life_nc,
    4: cash_5,
    5: pick_4,
    6: pick_3
    
}

def play_game():
    print("North Carolina Lotto:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky For Life")
    print("4. Cash 5 Double Play")
    print("5. Pick 4")
    print("6. Pick 3")
    

    while True:
        try:
            nc_lotto_game_choice = int(input("Make your selection: "))
            if nc_lotto_game_choice in nc_lotto_draw_games:
                for result in nc_lotto_draw_games[nc_lotto_game_choice]():
                    print(result)
                break 
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  
            print("Not a valid option. Please try again.")

print("Keno Lotto Draw Game is currently not available for selection.")    

def main():
    while True:
        play_game()
        while True:
            play_again = input("\nWould you like to try another draw game? (y/n): ").strip().lower()
            if play_again == 'y':
                break  
            elif play_again == 'n':
                print("Ok! Good Luck!!!")
                return   
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()