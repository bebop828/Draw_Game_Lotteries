import random

#Va has Keno, I have not yet coded this game yet!
#need to check all the times for draws.


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
    lotto_num = f"Lucky Lotto America Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. and Sat. 10:30pm ET"    
    lotto_add = f"Available add on- All Star Bonus $1 extra per play"
    lotto_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)


def daily_3():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    daily_main = f"Daily 3 lucky numbers: {set_1, set_2, set_3}"
    daily_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, Combo, or Pairs."
    daily_drawings = f"Base ticket prices are $.50 or $1. Cut off time to play is 6:49pm ET day of drawings. Drawings are held Mon-Sat 6:59pm ET."       
    daily_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/daily-3 Good Luck!"
    return (daily_main, daily_now, daily_drawings, daily_rules)


def daily_4():
    set_1 = random.sample(range(0, 10), 1)
    set_2 = random.sample(range(0, 10), 1)
    set_3 = random.sample(range(0, 10), 1)
    set_4 = random.sample(range(0, 10), 1)
    daily_main = f"Daily 4 lucky numbers: {set_1, set_2, set_3, set_4}"
    daily_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box."
    daily_drawings = f"Base ticket prices are $.50 or $1. Cut off time to play is 6:49pm ET day of drawings. Drawings are held Mon-Sat 6:59pm ET."       
    daily_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/daily-4 Good Luck!"
    return (daily_main, daily_now, daily_drawings, daily_rules)


def cash_25():
    cash_main = sorted(random.sample(range(1, 26), 6))
    cash_num = f"Cash 25 Lucky Numbers: {cash_main}"
    cash_drawings = f"Base Tickets to play are $1 Cut off time to play is 6:49pm day of drawings. Draw times are Mon. Tues. Thur. and Fri at 6:59pm ET"
    cash_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/cash-25 Good Luck!"
    return(cash_num, cash_drawings, cash_rules)


def cash_popWv():
    while True:
        try:
            num_choices = int(input("How many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number 1-15.")

    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"Lucky Cash Pop Number(s) : {pop}"
    pop_drawings = f"Base ticket price varies. Players will choose from $1, $2, $5, or $10 bet amounts per Cash Pop numbers played. Multiple Drawings Everyday! " 
    pop_win = f"Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/cash-pop/ Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules)
       


wv_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: daily_3,
    5: daily_4,
    6: cash_25,
    7: cash_popWv
}

def play_game():
    print("West Virgina Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Daily 3")
    print("5. Daily 4")
    print("6. Cash 25")
    print("7. Cash Pop")

    while True:
            try:
                wv_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
                if wv_lotto_game_choice in wv_lotto_draw_games:
                    for result in wv_lotto_draw_games[wv_lotto_game_choice]():
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

