import random 

#needs to have times confirmed. 

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


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.sample(range(1, 11), 1)[0]
    lotto_num = f"Lucky Lotto America with EZ-Match Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. and Sat. 9:15pm CT"    
    lotto_add = f"Available add on- All Star Bonus $1 extra per play"
    lotto_rules = f"Official Rules and Play can be found- https://www.lottery.ok.gov/draw-games/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)


def lucky_for_life_ok():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19), 1)[0]
    life_return = f"Lucky Numbers for Lucky For Life: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut off to play is 8:30pm CT. Drawings are held Nightly 9:30pm CT."    
    life_rules = f"Official Rules and Play can be found- https://www.lottery.ok.gov/draw-games/lucky-for-life Good Luck!"    
    return (life_return, life_drawings, life_rules)


def pick_3():
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    p3_main = f"Pick 3 Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = f"Now you have to decide to play these numbers Straight, Box, Front Pair, or Back Pair"
    p3_drawings = f"Tickets are $1. Cut-off time to play is 8:59pm CT. Drawings held Daily."
    p3_rules = f"Official Rules and Play can be found- https://www.lottery.ok.gov/draw-games/pick-3 Good Luck!"
    return (p3_main, p3_now, p3_drawings, p3_rules)


def cash_5ok():
    cash_main = sorted(random.sample(range(1, 37), 5))    
    cash_return = f"Lucky Numbers for Cash 5: {cash_main}."
    cash_drawings = f"Ticket prices are $1."    
    cash_rules = f"Official Rules and Play can be found- https://www.lottery.ok.gov/draw-games/cash-5 Good Luck!"    
    return (cash_return, cash_drawings, cash_rules)    



ok_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_for_life_ok,
    5: pick_3,
    6: cash_5ok
}


def play_game():
    print("Oklahoma Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky For Life")
    print("5. Pick 3")
    print("6. Cash 5")




    while True:
        try:
            ok_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if ok_lotto_game_choice in ok_lotto_draw_games:
                for result in ok_lotto_draw_games[ok_lotto_game_choice]():
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
