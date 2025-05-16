###################################################################
############ Connecticut Draw Lottery #############################
###################################################################

###################################################################
# last file update- 2025/05/16 
# Connecticut has Keno Draw Game. 
# Keno not included currently with file. Will update another date
###################################################################

import random 


def powerball(): 
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}" 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Mon. Wed. & Sat. 10:59pm ET ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    mega_main = sorted(random.sample(range(1, 61), 5))
    mega_ball = random.sample(range(1, 27), 1)[0]
    mega_luck = f"Mega Millions Lucky Numbers: {mega_main}, Mega Ball: {mega_ball}"
    mega_draw = f"Ticket Price to play $5. Cut off time is 10pm ET play nights. Drawings held Tuesday and Friday 11pm ET"
    mega_add = f"Megaplier is available with each gameplay."
    mega_official = f"Official rules and Play can be found- https://www.megamillions.com Good Luck!" 
    return (mega_luck, mega_draw, mega_add, mega_official)


def lotto(): 
    lotto_main = sorted(random.sample(range(1, 45), 6))
    lotto_luck = f"Connecticut Lotto! Lucky Numbers: {lotto_main}"
    lotto_draw = f"Ticket prices $1. Cut off time to play 10:20pm ET  Drawings every Tuesday and Friday at 10:38pm ET!"
    lotto_official = f"Offical Rules and Play can be found- https://www.ctlottery.org/Lotto! Good Luck!"
    return (lotto_luck, lotto_draw, lotto_official)
    

def lucky_4Life():
    lucky_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19), 1)[0]
    lucky_luck = f"Lucky 4 Life Lucky Numbers: {lucky_main}, Lucky Ball: {lucky_ball}"
    lucky_draw = f"Tickets are $2. Cut off time for play is 9:30pm ET. Drawings held Nightly 10:30pm ET"
    lucky_official = f"Official Rules and Play can be found- https://www.ctlottery.org/LuckyForLife Good Luck!"
    return(lucky_luck, lucky_draw, lucky_official)


def cash5(): 
    cash_main = sorted(random.sample(range(1, 36), 5))
    possible_kicker = [n for n in range(1, 36) if n not in cash_main]
    cash_kicker = random.choice(possible_kicker)
    cash_luck = f"Lucky Cash 5 with Kicker Numbers: {cash_main}, Kicker: {cash_kicker}"
    cash_draw = f"Tickets are $1. Cut off time to play is 10:20pm ET. Drawings held Nightly 10:29pm ET"
    cash_kicker_info = f"Kicker is optional add-on which cost $.50 extra to play.\nUser will get a number not drawn of original 5 for Gameplay!"
    cash_official = f"Official Rules and Play can be found- https://www.ctlottery.org/Cash5 Good Luck!"
    return(cash_luck, cash_draw, cash_kicker_info, cash_official)
    

def play3():
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
     
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Play 3 with Wild Ball Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Pairs, or Combo"
    p3_drawings = f"Play amounts start at $.50 and go to $5" 
    p3_rules = f"Official Rules and Play can be found- https://www.ctlottery.org/Play3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)
 

def play4():
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
     
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(1, 10), 1)
    p4_main = f"Play 4 with Wild Ball Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Pairs, or Combo"
    p4_drawings = f"Play amounts start at $.50 and go to $5" 
    p4_rules = f"Official Rules and Play can be found- https://www.ctlottery.org/Play4 Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_rules)



ct_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto,
    4: lucky_4Life,
    5: cash5,
    6: play3,
    7: play4  
    
}


def play_game():
    print("Connecticut Lotto Games")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Connecticut Lotto!")
    print("4. Lucky 4 Life")
    print("5. Cash 5 with Kicker")
    print("6. Play 3 with Wild Ball")
    print("7. Play 4 with Wild Ball")
    
    
    while True:
            try:
                ct_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if ct_lotto_game_choice in ct_lotto_draw_games:
                    for result in ct_lotto_draw_games[ct_lotto_game_choice]():
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




