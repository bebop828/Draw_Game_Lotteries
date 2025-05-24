###################################################################
################## Delaware Draw Lotto Games ######################
###################################################################

###################################################################
# last file update- 2025/05/24
# Delaware has Keno Draw Game. 
# Keno not included currently with file. Will update another date
###################################################################


import random

#Delaware Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.sample(range(1, 11), 1)[0]
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = f"Ticket price $1. Cut off time 9:45pm ET. Drawings are held Mon, Wed, Sat 11pm ET"
    lotto_add = f"Add-on- All-Star Multiplier available for $1 extra"
    lotto_rules = f"Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Lotto-America"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)
    

def multi_win():
    multi_num = sorted(random.sample(range(1, 36), 6))
    multi_main = f"Multi-Win Lotto Lucky Numbers: {multi_num}"
    multi_draw = f"Ticket price $2. Cut off to play 7:30pm nightly. Drawings are held Everyday at 7:57pm ET"
    multi_rules = f"Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Multi-Win-Lotto"
    return (multi_main, multi_draw, multi_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19),1)[0]
    lucky_main = f"Lucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = f"Ticket price $2 Cut off time to play 9:30pm ET. Drawings held Everyday at 10:38pm ET"
    lucky_rules = f"Official Rules and Gameplay can be found- https://www.delottery.com/Drawing-Games/Lucky-For-Life"
    return (lucky_main, lucky_draw, lucky_rules)


def play3():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:58pm ET Draw")
        print("2. Night 7:57pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day 1:58pm ET Draw',
            2: 'Night 7:57pm ET Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Play 3 Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Front/Back Pair, or Combination"
    p3_drawings = f"Base ticket prices $.50 or $1. Cut-off time to play is 1:40pm ET for Day Draw and 7:30pm for Night."      
    p3_rules = f"Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Play-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


def play4():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:58pm ET Draw")
        print("2. Night 7:57pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day 1:58pm ET Draw',
            2: 'Night 7:57pm ET Draw'
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
    p4_main = f"Play 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box,or Combination"
    p4_drawings = f"Base ticket prices $.50 or $1. Cut-off time to play is 1:40pm ET for Day Draw and 7:30pm for Night."      
    p4_rules = f"Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Play-4 Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_rules)


def play5():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:58pm ET Draw")
        print("2. Night 7:57pm ET Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day 1:58pm ET Draw',
            2: 'Night 7:57pm ET Draw'
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
    set_5 = random.sample(range(0, 10), 1)    
    p5_main = f"Play 5 Lucky Numbers: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = f"Play 5 has 8 different ways to play and win. Check site for official ways to play!"
    p5_drawings = f"Base ticket prices $.50 or $1. Cut-off time to play is 1:40pm ET for Day Draw and 7:30pm for Night."      
    p5_rules = f"Official Rules and Play can be found- https://www.delottery.com/Drawing-Games/Play-5 Good Luck!"       
    return (p5_main, p5_now, p5_drawings, p5_rules)



de_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: multi_win,
    5: lucky_life,
    6: play3,
    7: play4,
    8: play5
        
}

def play_game():
    print("Delaware Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Multi-Win Lotto")
    print("5. Lucky for Life")
    print("6. Play 3")
    print("7. Play 4")
    print("8. Play 5")
    
    
    
    while True:
                try:
                    de_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                    if de_lotto_game_choice in de_lotto_draw_games:
                        for result in de_lotto_draw_games[de_lotto_game_choice]():
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