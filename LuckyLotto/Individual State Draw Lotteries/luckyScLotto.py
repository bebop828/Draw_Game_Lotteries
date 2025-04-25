import random

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

def palm_cash_5():
    cash_5_main = sorted(random.sample(range(1, 43), 5))
    cash_5_numbers_main = f"Palmetto Cash 5 Lucky Numbers: {cash_5_main}"
    cash_5_drawings = f"Base ticket price $2. Cut-off time to play is 6:45pm each afternoon. Drawings held at 6:59pm ET daily."    
    cash_5_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/HowToPlay Good Luck!"    
    return (cash_5_numbers_main, cash_5_drawings, cash_5_rules)

def pick_4_day():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main = f"Pick 4 Day Draw plus Fireball Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo.."
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 12:45pm ET each afternoon. Day Drawings held 12:59pm ET everyday."
    p4_fire_mid = f"Available add on- FIREBALL (doubles the ticket price)."    
    p4_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/HowToPlay Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)

def pick_4_eve():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main = f"Pick 4 Evening Draw plus Fireball Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo.."
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 6:45pm ET each afternoon. Evening Drawings held 6:59pm ET everyday."
    p4_fire_mid = f"Available add on- FIREBALL (doubles the ticket price)."    
    p4_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/HowToPlay Good Luck!"
    return (p4_main, p4_now, p4_drawings, p4_fire_mid, p4_rules)

def pick_3_day():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)    
    p3_main = f"Pick 3 Day Draw plus Fireball Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo.."
    p3_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 12:45pm ET each afternoon. Day Drawings held 12:59pm ET everyday."
    p3_fire_mid = f"Available add on- FIREBALL (doubles the ticket price)."    
    p3_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/HowToPlay Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire_mid, p3_rules)

def pick_3_eve():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)    
    p3_main = f"Pick 4 Evening Draw plus Fireball Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo.."
    p3_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 6:45pm ET each afternoon. Evening Drawings held 6:59pm ET everyday."
    p3_fire_mid = f"Available add on- FIREBALL (doubles the ticket price)."    
    p3_rules = f"Official Rules and Play can be found- https://www.sceducationlottery.com/Games/HowToPlay Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_fire_mid, p3_rules)


sc_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: palm_cash_5,
    4: pick_4_day,
    5: pick_4_eve,
    6: pick_3_day,
    7: pick_3_eve,
}

def play_game():
    print("South Carolina Lotto:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Palmetto Cash 5")
    print("4. Pick 4 plus FIREBALL Day Draw")
    print("5. Pick 4 plus FIREBALL Evening Draw")
    print("6. Pick 3 plus FIREBALL Day Draw")
    print("7. Pick 3 plus FIREBALL Evening Draw")

    while True:
        try:
            sc_lotto_game_choice = int(input("Make your selection: "))
            if sc_lotto_game_choice in sc_lotto_draw_games:
                for result in sc_lotto_draw_games[sc_lotto_game_choice]():
                    print(result)
                break 
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  
            print("Not a valid option. Please try again.")

print("Cash Pop Lotto Draw Game is currently not available for selection.")    

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