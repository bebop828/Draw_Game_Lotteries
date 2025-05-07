###########################################################################
###################### Arizona Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/06
###########################################################################

import random

#Arizona Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play in Arizona varies throughout the year. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Cut-off time to play in Arizona varies throughout the year. Drawings are held Tues. Fri. 11pm ET."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def the_pick():
    pick_num = sorted(random.sample(range(1, 45), 6))
    pick_num_main = f"The Pick Lucky Numbers: {pick_num}"
    pick_draw = f"Base ticket price $1. Cut-off time to play is 6:59pm MST. Drawings are held Mon, Wed, Sat."
    pick_add = f"Available add ons- EXTRA $1 or $2 option."
    pick_rules = f"Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/the-pick/ Good Luck!"
    return (pick_num_main, pick_draw, pick_add, pick_rules)

def triple_twist():
    trip_num = sorted(random.sample(range(1, 43), 6))
    trip_num_main = f"Triple Twist Lucky Numbers: {trip_num}"
    trip_draw = f"Ticket Cost $2. Cut-off time to play is 6:59pm MST. Drawings are held Mon-Sun."
    trip_rules = f"Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/triple-twist/ Good Luck!"
    return (trip_num_main, trip_draw, trip_rules)

def fantasy5():
    fan5 = sorted(random.sample(range(1, 42), 5))
    fan5_num_main = f"Fantasy 5 Lucky Numbers: {fan5}"
    fan5_draw = f"Base ticket price $1. Cut-off time to play is 6:59pm MST. Drawings are held Mon-Sun"
    fan5_rules = f"Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/fantasy-5/ Good Luck!"
    return (fan5_num_main, fan5_draw, fan5_rules)

def pick3():    
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1) 
    set_3 = random.sample(range(0, 10), 1)    
    pk3_main = f"Pick 3 Lucky Numbers: {set_1, set_2, set_3}"   
    pk3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, Front Pair, or Back Pair."
    pk3_draw = f"Ticket price $1. Cut-off time for play is 6:59pm MST. Drawings are held Mon-Sun"
    pk3_rules = f"Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/pick-3/ Good Luck!"
    return (pk3_main, pk3_now, pk3_draw, pk3_rules)
    
   
az_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: the_pick,
    4: triple_twist,
    5: fantasy5,
    6: pick3

}


def play_game():
    print("Arizona Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. The Pick")
    print("4. Triple Twist")
    print("5. Fantasy 5")
    print("6. Pick 3")
    
    
    while True:
            try:
                az_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if az_lotto_game_choice in az_lotto_draw_games:
                    for result in az_lotto_draw_games[az_lotto_game_choice]():
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