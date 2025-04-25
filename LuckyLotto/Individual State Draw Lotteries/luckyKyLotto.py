import random

#need to have draw times confirmed 
#Ky has Keno. Keno not writen in
#Cash Pop is written to produce how ever many picks user would like to play. Ky has drawings every 4 min

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


def ky_5():
    ky_main = sorted(random.sample(range(1, 40), 5))
    ky_num_main = f"Kentucky 5 Lucky Numbers: {ky_main}"
    ky_drawings = f"Base ticket $1."
    ky_add = f"Available add on- Xtra $1 per play."
    ky_rules = f"Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/kentucky5/index.html Good Luck!"
    return(ky_num_main, ky_drawings, ky_add, ky_rules)


def cash_popKy():
    while True:
        try:
            num_choices = int(input("How many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number 1-15.")

    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"Lucky Cash Pop Number(s) : {pop}"
    pop_drawings = f"Base ticket price varies. Players will choose from $1, $2, $5, or $10 bet amounts per Cash Pop numbers played. Multiple Drawings Everyday! " 
    pop_win = f"Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = f"Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/cashpop/index.html Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)
       

def lucky_for_life_ky():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19), 1)[0]
    life_return = f"Lucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut-off time to play is 9:30pm ET each night. Drawings are held Nightly 10:30pm ET."    
    life_rules = f"Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/luckyforlife/index.html Good Luck!"    
    return (life_return, life_drawings, life_rules)


def cash_ball():
    cash_main = sorted(random.sample(range(1, 36), 4))
    cash_ball_main = random.sample(range(1, 26), 1)[0]
    cash_return = f"Ca$h Ball Lucky Numbers: {cash_main}, Lucky Ball: {cash_ball_main}."
    cash_drawings = f"Base ticket price $1." 
    cash_add = f"Available add on- EZmatch $1 per play."   
    cash_rules = f"Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/cashball/index.html Good Luck!"    
    return (cash_return, cash_drawings, cash_add, cash_rules)


def pick_3ky():
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
            1: 'Mid-Day- Draw',
            2: 'Evening- Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
     
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 plus Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Super Straight, or Pairs"
    p3_drawings = f"Base ticket prices $.50 or $1." 
    p3_rules = f"Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/pick3/index.html Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


def pick_4ky():
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
            1: 'Mid-Day Draw',
            2: 'Evening Draw'
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
    p4_now = f"Now you have to decide to play these numbers Straight, Box, or Straight/Box."
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 1:20pm ET for Mid_Day Draw and 9:35pm ET for Evening."
    p4_fire_mid = f"Available add on- FIREBALL (doubles ticket amount)."    
    p4_rules = f"Official Rules and Play can be found- https://www.kylottery.com/apps/draw_games/pick4/index.html Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)


ky_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: ky_5,
    4: cash_popKy,
    5: lucky_for_life_ky,
    6: cash_ball,
    7: pick_3ky,
    8: pick_4ky
}


def play_game():
    print("Kentucky Lotto Game Choices: ")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Kentucky 5")
    print("4. Cash Pop")
    print("5. Lucky For Life")
    print("6. Ca$h Ball with EZmatch")
    print("7. Pick 3") 
    print("8. Pick 4")

    while True:
            try:
                ky_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if ky_lotto_game_choice in ky_lotto_draw_games:
                    for result in ky_lotto_draw_games[ky_lotto_game_choice]():
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
