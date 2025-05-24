###########################################################################
#################### Louisiana Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/24
###########################################################################

import random

# Louisiana Game Choices
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
    mm_drawings = f"Base ticket price $2. Cut-off time to play is 10pm ET night of drawings. Drawings are held Tues. & Fri. 11pm ET."
    mm_add = f"Available add on- Megaplier $1 extra."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def la_lotto():
    lott_main = sorted(random.sample(range(1, 43), 6))
    lott_numbers_main = f"Lucky Louisiana Lotto Numbers: {lott_main}"
    lott_drawings = f"Base ticket price $1. Cut-off time to play is 9:30pm night of drawings. Drawings are held Wed. & Sat. 9:59pm ET."
    lott_official = f"Official Rules and Play can be found- https://louisianalottery.com/lotto/tab/how-to-play/how-to-play Good Luck!"
    return (lott_numbers_main, lott_drawings, lott_official)

def easy_5():
    easy_main = sorted(random.sample(range(1, 38), 5))
    easy_numbers_main = f"Lucky Louisiana Lotto Numbers: {easy_main}"
    easy_drawings = f"Base ticket price $1. Cut-off time to play is 9:30pm night of drawings. Drawings are held Wed. & Sat. 9:59pm ET."
    easy_add = f"Available add on- ezMatch $1 extra"
    easy_rules = f"Official Rules and Play can be found- https://louisianalottery.com/easy-5/tab/how-to-play Good Luck!"
    return (easy_numbers_main, easy_drawings, easy_add, easy_rules)

def la_pic_3():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo"
    p3_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:30pm. Drawings are held Daily 9:59pm ET."      
    p3_rules = f"Official Rules and Play can be found- https://louisianalottery.com/pick-3/tab/how-to-play Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)

def la_pic_4():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    p4_main = f"Pick 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo"
    p4_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:30pm. Drawings are held Daily 9:59pm ET."      
    p4_rules = f"Official Rules and Play can be found- https://louisianalottery.com/pick-4/tab/how-to-play Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_rules)

def la_pic_5():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    set_5 = random.sample(range(0, 10), 1)
    p5_main = f"Pick 5 Lucky Numbers: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box, or Combo"
    p5_drawings = f"Base ticket prices are $.50 or $1. Cut-off time to play is 9:30pm. Drawings are held Daily 9:59pm ET."      
    p5_rules = f"Official Rules and Play can be found- https://louisianalottery.com/pick-5/tab/how-to-play Good Luck!"    
    return (p5_main, p5_now, p5_drawings, p5_rules)


la_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: la_lotto,
    4: easy_5,
    5: la_pic_3,
    6: la_pic_4,
    7: la_pic_5,    
}

def play_game():
    print("Louisiana Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto")
    print("4. Easy 5")
    print("5. Pick 3")
    print("6. Pick 4")
    print("7. Pick 5")


    while True:
        try:
            la_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if la_lotto_game_choice in la_lotto_draw_games:
                for result in la_lotto_draw_games[la_lotto_game_choice]():
                    print(result)
                break  
            else:
                print("Not a valid option. Please try again.")
        except ValueError:  
            print("Not a valid option. Please try again.")

print("Please note On-line purchase of lotto draw games are not prohibited in Louisiana.")
print("However, for purchases, please see an official lotto retailer.")

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