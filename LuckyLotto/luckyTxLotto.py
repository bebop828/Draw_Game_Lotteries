import random

def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Available add on- Megaplier $1 extra."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def tx_lotto():
    tx_num = sorted(random.sample(range(1, 55), 6))    
    tx_numbers_main = f"Texas Lotto Lucky Numbers: {tx_num}"
    tx_drawings = f"Base ticket price $1. Cut-off time to play is 10:02pm CT night of drawings. Drawings are held Mon. Wed. Sat. 10:12pm CT."
    tx_add = f"Available add on- Extra $1 per play."
    tx_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/#HowToPlay Good Luck!"    
    return (tx_numbers_main, tx_drawings, tx_add, tx_rules)

def tx_2step():
    step_num = sorted(random.sample(range(1, 36), 4))    
    step_num_bonus = random.sample(range(1, 36), 1)[0]
    step_numbers_main = f"Lucky Texas 2 Step Numbers: {step_num}, Bonus Ball: {step_num_bonus}"
    step_drawings = f"Base ticket price $1. Cut-off time to play is 10:02pm CT night of drawings. Drawings are held Mon. Thur. 10:12pm CT."    
    step_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Texas_Two_Step/#HowToPlay Good Luck!"    
    return (step_numbers_main, step_drawings, step_rules)

def all_nothing():    
    while True:
        print("Select a game time to play:")
        print("1: Morning- 10am CT Drawing")
        print("2: Day- 12:27pm CT Drawing")
        print("3: Evening- 6pm CT Drawing")
        print("4: Night- 10:12pm CT Drawing")
        
        try:
            choice = int(input("Make Selection and enter (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4")
            continue  
        
        game_time_mapping = {
            1: 'Morning- 10am CT Drawing',
            2: 'Day- 12:27pm CT Drawing',
            3: 'Evening- 6pm CT Drawing',
            4: 'Night- 10:12pm CT Drawing'
        }
        
        if choice not in game_time_mapping:
            print("Invalid selection. Please choose a number between 1 and 4.")
            continue         
        
        game_time = game_time_mapping[choice]
        break    
    all_num = sorted(random.sample(range(1, 25), 12))    
    all_num_main = f"Lucky Texas All or Nothing Numbers for {game_time}: {all_num}"
    all_draw = f"Base ticket cost $2. Drawings held Mon-Sat."
    all_rules = "Official Rules and Play can be found here: https://www.texaslottery.com/export/sites/lottery/Games/All_or_Nothing/index.html#HowToPlay Good Luck!"
    return (all_num_main, all_draw, all_rules)
    
def pick_3():
    while True:
        print("Select a game time to play Pick 3 with FIREBALL:")
        print("1: Morning- 10am CT Drawing")
        print("2: Day- 12:27pm CT Drawing")
        print("3: Evening- 6pm CT Drawing")
        print("4: Night- 10:12pm CT Drawing")

        try:
            choice = int(input("Make Selection and enter (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4.")
            continue  

        game_time_mapping = {
            1: 'Morning- 10am CT Drawing',
            2: 'Day- 12:27pm CT Drawing',
            3: 'Evening- 6pm CT Drawing',
            4: 'Night- 10:12pm CT Drawing'
        }

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose a number between 1 and 4.")
            continue  
        
        game_time = game_time_mapping[choice]
        break 
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 plus FIREBALL  Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Exact, Any Order, Exact/Any Order, or Combo"
    p3_drawings = f"Base ticket prices are $.50 or $1."
    p3_fire = f"Available add on- FIREBALL (doubles the ticket cost)."   
    p3_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Pick_3/index.html#HowToPlay Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_fire, p3_rules)

def daily_4():
    while True:
        print("Select a game time to play Pick 3 with FIREBALL:")
        print("1: Morning- 10am CT Drawing")
        print("2: Day- 12:27pm CT Drawing")
        print("3: Evening- 6pm CT Drawing")
        print("4: Night- 10:12pm CT Drawing")

        try:
            choice = int(input("Make Selection and enter (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter 1-4.")
            continue  

        game_time_mapping = {
            1: 'Morning- 10am CT Drawing',
            2: 'Day- 12:27pm CT Drawing',
            3: 'Evening- 6pm CT Drawing',
            4: 'Night- 10:12pm CT Drawing'
        }

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose a number between 1 and 4.")
            continue  
        
        game_time = game_time_mapping[choice]
        break 
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main = f"Texas Daily 4 plus FIREBALL Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Stgraight/Box, or Combo"
    p4_drawings = f"Base ticket prices are $.50 or $1."
    p4_fire = f"Available add on- FIREBALL (doubles the ticket cost)."   
    p4_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Daily_4/index.html#HowToPlay Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_fire, p4_rules)

def cash_5():
    c5_num = sorted(random.sample(range(1, 36), 5))    
    c5_numbers_main = f"Lucky Cash 5 Numbers: {c5_num}"
    c5_drawings = f"Base ticket price $1. Cut-off time to play is 10:02pm CT night of drawings. Drawings are held Mon-Sat 10:12pm CT."    
    c5_rules = f"Official Rules and Play can be found- https://www.texaslottery.com/export/sites/lottery/Games/Cash_Five/index.html#HowToPlay Good Luck!"    
    return (c5_numbers_main, c5_drawings, c5_rules)

tx_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: tx_lotto,
    4: tx_2step,
    5: all_nothing,
    6: pick_3,
    7: daily_4,
    8: cash_5,
}


def play_game():
    print("Texas Lotto:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto Texas with Extra")
    print("4. Texas 2 Step")
    print("5. All or Nothing")
    print("6. Pick 3 with FIREBALL")
    print("7. Daily 4 with FIREBALL")
    print("8. Cash 5")

    while True:
        try:
            tx_lotto_game_choice = int(input("Make your selection: "))
            if tx_lotto_game_choice in tx_lotto_draw_games:
                for result in tx_lotto_draw_games[tx_lotto_game_choice]():
                    print(result)
                break  # execute the program again
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  #this helped fix invalid user input
            print("Not a valid option. Please try again.")

    
def main():
    while True:
        play_game()
        while True:
            play_again = input("\nWould you like to try another draw game? (y/n): ").strip().lower()
            if play_again == 'y':
                break  # Exit the inner loop and play the game again
            elif play_again == 'n':
                print("Ok! Good Luck!!!")
                return  # Exit 
            else:
                print("That is not an acceptable response. Please try again.")

if __name__ == "__main__":
    main()