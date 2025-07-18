###########################################################################
###################### Arizona Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/07/14
########################################################################### 

import random

#Arizona Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add on- Power Play $1 extra."
    pb_official = "Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def the_pick():
    pick_num = sorted(random.sample(range(1, 45), 6))
    pick_num_main = f"\nThe Pick Lucky Numbers: {pick_num}"
    pick_draw = "Base ticket price $1. Drawings are held Mon. Wed. & Sat."
    pick_add = "Available add ons- EXTRA $1 or $2 option."
    pick_rules = "Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/the-pick/ Good Luck!"
    return (pick_num_main, pick_draw, pick_add, pick_rules)

def triple_twist():
    trip_num = sorted(random.sample(range(1, 43), 6))
    trip_num_main = f"\nTriple Twist Lucky Numbers: {trip_num}"
    trip_draw = "Ticket Cost to play $2. Drawings held Daily!"
    trip_rules = "Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/triple-twist/ Good Luck!"
    return (trip_num_main, trip_draw, trip_rules)

def fantasy5():
    fan5 = sorted(random.sample(range(1, 42), 5))
    fan5_num_main = f"\nFantasy 5 Lucky Numbers: {fan5}"
    fan5_draw = "Ticket price to play $1. Drawings held Daily!"
    fan5_rules = "Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/fantasy-5/ Good Luck!"
    return (fan5_num_main, fan5_draw, fan5_rules)

def pick3():    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9) 
    set_3 = random.randint(0, 9)    
    pk3_main = f"\nPick 3 Lucky Numbers: {set_1, set_2, set_3}"   
    pk3_now = "Now you have to decide to play these numbers Straight, Box, Straight/Box, Front Pair, or Back Pair."
    pk3_draw = "Ticket price to play $1. Drawings held Daily!"
    pk3_rules = "Official Rules and Play can be found- https://www.arizonalottery.com/draw-games/pick-3/ Good Luck!"
    return (pk3_main, pk3_now, pk3_draw, pk3_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def the_pick_summary():
    pick_num = sorted(random.sample(range(1, 45), 6))
    return ("The Pick", f"Numbers: {pick_num}")
    
def triple_twist_summary():
    trip_num = sorted(random.sample(range(1, 43), 6))
    return ("Triple Twist", f"Numbers: {trip_num}")
    
def fantasy5_summary():
    fan5 = sorted(random.sample(range(1, 42), 5))
    return ("Fantasy 5", f"Numbers: {fan5}")    
        
def pick3_summary():        
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Play 3", f"Numbers: ({set_1}, {set_2}, {set_3})")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "The Pick": the_pick_summary,
    "Triple Twist": triple_twist_summary,
    "Fantasy 5": fantasy5_summary,
    "Pick 3": pick3_summary
}

    
#draw games   
az_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: the_pick,
    4: triple_twist,
    5: fantasy5,
    6: pick3,
    7: lambda: az_lotto_draw_games[random.randint(1, 6)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]
}

#the menu
def play_game():
    print("\nArizona Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. The Pick")
    print("4. Triple Twist")
    print("5. Fantasy 5")
    print("6. Pick 3")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 6 Games")
    
    #waiter
    while True:
        try:
            az_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if az_lotto_game_choice in az_lotto_draw_games:                        
                result = az_lotto_draw_games[az_lotto_game_choice]()

                if isinstance(result, list):                    
                    for res in result:
                        if isinstance(res, tuple) and len(res) == 2:
                            print(f"{res[0]} — {res[1]}")
                        else:
                            print(res)
                else:                    
                    for item in result:
                        print(item)
                break  
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  
            print("Not a valid option. Please try again.")
    
#cook 
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