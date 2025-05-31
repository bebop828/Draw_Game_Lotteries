import random


#I need to look into each of these lotto draw games for draw times and freq. This is not finished.
#Test over and over. 
#Need to add disclaimer for lottery addiction.

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


def cash_4_life_tn():
    cash_main = sorted(random.sample(range(1, 61), 5))
    cash_ball = random.sample(range(1, 5), 1)[0]
    numbers_main = f"Cash 4 Life Lucky Numbers: {cash_main}, Cash Ball: {cash_ball}."
    drawings_c4l = f"Base ticket price $2. Cut-off time to play is 8:30pm ET each night. Drawings are held Nightly 9pm ET."    
    rules_c4l = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/cash-4-life/ Good Luck!"    
    return (numbers_main, drawings_c4l, rules_c4l)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.sample(range(1, 11), 1)[0]
    lotto_num = f"Lucky Lotto America with Quick Cash Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. and Sat."    
    lotto_add = f"Available add on games- Quick Cash and All Star Bonus $1 extra each per play"
    lotto_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)


def daily_tn():
    daily_main = sorted(random.sample(range(1, 39), 5))    
    daily_num = f"Daily Tennessee Jackpot with Quick Cash Numbers: {daily_main}"
    daily_drawings = f"Base ticket price $1. Drawings are held Daily."    
    daily_add = f"Available add on games- Quick Cash $1 extra per play"
    daily_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/daily-tennessee-jackpot Good Luck!"        
    return (daily_num, daily_drawings, daily_add, daily_rules)


def tn_cash(): 
    tncash_main = sorted(random.sample(range(1, 36), 5))
    tncash_ball = random.sample(range(1, 6), 1)[0]
    tncash_num = f"Lucky Tennessee Cash with Quick Cash Numbers: {tncash_main}, Cash Ball: {tncash_ball}."
    tncash_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. and Fri."    
    tncash_add = f"Available add on games- Quick Cash $1 extra per play"
    tncash_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/tennessee-cash Good Luck!"    
    return (tncash_num, tncash_drawings, tncash_add, tncash_rules)


def cash_3():
    while True: 
        print("Select a game time to play:")        
        print("1. Morning Draw")
        print("2. Mid-day Draw")
        print("3. Evening Draw")

        try:
            choice = int(input("Make selection (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Morning Draw',
            2: 'Mid-Day Draw',
            3: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    c3_main = f"Cash 3 with Wild Ball Lucky Numbers: {game_time}: {set_1, set_2, set_3}"
    c3_now = f"Now you have to decide to play these numbers Exact, Any Order, Exact/ Any Order, or Combo"
    c3_drawings = f"Base ticket prices either $.50 or $1. Morning, Mid-Day, and Evening Drawings held Mon-Sat. Evening drawings Sun only."
    c3_wild = f"Available add on- Wild Ball (doubles ticket amount)."   
    c3_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/cash3 Good Luck!"    
    return (c3_main, c3_now, c3_drawings, c3_wild, c3_rules)


def cash_4():
    while True: 
        print("Select a game time to play:")        
        print("1. Morning Draw")
        print("2. Mid-day Draw")
        print("3. Evening Draw")

        try:
            choice = int(input("Make selection (1-3): ").strip())
        except ValueError:
            print("Invalid input. Please enter (1-3)")
            continue

        game_time_mapping = {
            1: 'Morning Draw',
            2: 'Mid-Day Draw',
            3: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please enter (1-3)")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.sample(range(1, 10), 1)
    set_2 = random.sample(range(1, 10), 1)   
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    c4_main = f"Cash 4 with Wild Ball Lucky Numbers: {game_time}: {set_1, set_2, set_3, set_4}"
    c4_now = f"Now you have to decide to play these numbers Exact, Any Order, Exact/ Any Order, or Combo"
    c4_drawings = f"Base ticket prices either $.50 or $1. Morning, Mid-Day, and Evening Drawings held Mon-Sat. Evening drawings Sun only."
    c4_wild = f"Available add on- Wild Ball (doubles ticket amount)."   
    c4_rules = f"Official Rules and Play can be found- https://tnlottery.com/games/how-to-play/cash4 Good Luck!"    
    return (c4_main, c4_now, c4_drawings, c4_wild, c4_rules)



tn_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: cash_4_life_tn,
    4: lotto_america,
    5: daily_tn,
    6: tn_cash,
    7: cash_3,
    8: cash_4
}




def play_game():
    print("Tennessee Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Cash 4 Life")
    print("4. Lotto America with Quick Cash")
    print("5. Daily Tennessee Jackpot with Quick Cash")
    print("6. Tennessee Cash with Quick Cash")
    print("7. Cash 3 with Wild Ball")
    print("8. Cash 4 with Wild Ball")


    while True:
            try:
                tn_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if tn_lotto_game_choice in tn_lotto_draw_games:
                    for result in tn_lotto_draw_games[tn_lotto_game_choice]():
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




