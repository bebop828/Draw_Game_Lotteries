###########################################################################
##################### Arkansas Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/06
###########################################################################

import random

# Arkansas Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier available with each play."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def ark_lotto():
    lotto_main = sorted(random.sample(range(1, 41), 6))
    lotto_numbers_main = f"Lucky Lotto Arkansas Numbers: {lotto_main}"
    lotto_drawings = f"Base ticket price $2. Drawings are held Wed. & Sat. 9:00pm CT."    
    lotto_rules = f"Official Rules and Play can be found- https://www.myarkansaslottery.com/games/lotto Good Luck!"
    return (lotto_numbers_main, lotto_drawings, lotto_rules)


def nat_stJack():
    nat_main = sorted(random.sample(range(1, 40), 5))
    nat_numbers_main = f"Lucky Natural State Jackpot Numbers: {nat_main}"
    nat_drawings = f"Base ticket price $1. Cut off to purchase tickets 7:59pm CT. Drawings are held Daily 8:00pm CT."    
    nat_rules = f"Official Rules and Play can be found- https://www.myarkansaslottery.com/games/natural-state-jackpot Good Luck!"
    return (nat_numbers_main, nat_drawings, nat_rules)


def lucky_4Life():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19), 1)[0]
    life_return = f"Lucky For Life Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut-off time to play is 8:30pm CT. Drawings are held Nightly 9:30pm CT."    
    life_rules = f"Official Rules and Play can be found- https://www.myarkansaslottery.com/games/lucky-for-life Good Luck!"    
    return (life_return, life_drawings, life_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 12:59pm CT Draw")
        print("2. Evening 6:59pm CT Draw")
        
        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:59pm CT Draw',
            2: 'Evening- 6:59pm CT Draw'            
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
    c4_drawings = f"Base ticket prices are $.50 or $1. Mid-Day 12:59pm CT Drawings Held Monday-Saturday. Evening 6:59pm CT Drawings Held Monday-Sunday"     
    c4_rules = f"Official Rules and Play can be found- https://www.myarkansaslottery.com/games/cash-4 Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-Day 12:59pm CT Draw")
        print("2. Evening 6:59pm CT Draw")
        
        try:
            choice = int(input("Make selection and enter (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Mid-Day- 12:59pm CT Draw',
            2: 'Evening- 6:59pm CT Draw'            
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
    c3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo."
    c3_drawings = f"Base ticket prices are $.50 or $1. Mid-Day 12:59pm CT Drawings Held Monday-Saturday. Evening 6:59pm CT Drawings Held Monday-Sunday"      
    c3_rules = f"Official Rules and Play can be found-https://www.myarkansaslottery.com/games/cash-3 Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_rules)


ak_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: ark_lotto,
    4: nat_stJack,
    5: lucky_4Life,
    6: cash_4,
    7: cash_3
}



def play_game():
    print("Arkansas Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto Arkansas")
    print("4. Natural State Jackpot")
    print("5. Lucky For Life")
    print("6. Cash 4")
    print("7. Cash 3")


    while True:
            try:
                ak_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if ak_lotto_game_choice in ak_lotto_draw_games:
                    for result in ak_lotto_draw_games[ak_lotto_game_choice]():
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

