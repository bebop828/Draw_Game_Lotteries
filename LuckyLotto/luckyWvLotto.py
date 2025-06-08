###########################################################################
############### West Virgina Draw Lotto Games #############################
###########################################################################

###########################################################################
# last file update- 2025/06/07
# WV has Keno Draw Game.
# Keno not included in current version
########################################################################### 


import random


# West Virgina Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 10:59pm ET." 
    pb_add = f"Available add on- Power Play $1 extra."
    pb_official = f"Official Rules and Play can be found- https://wvlottery.com/games/draw-games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues & Fri. 11pm ET."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://wvlottery.com/games/draw-games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_num = f"Lucky Lotto America Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Base ticket price $1. Drawings are held Mon. Wed. & Sat. 10:30pm ET"    
    lotto_add = f"Available add on- All Star Bonus $1 extra per play"
    lotto_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/lotto-america Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_add, lotto_rules)


def daily_3():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    daily_main = f"Daily 3 lucky numbers: {set_1, set_2, set_3}"
    daily_now = f"Now you have to decide to play these numbers Exact, Any Order, 50/50, Combo, or Pairs."
    daily_drawings = f"Base ticket prices are $.50 or $1. Drawings are held Mon-Sat 6:59pm ET."       
    daily_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/daily-3 Good Luck!"
    return (daily_main, daily_now, daily_drawings, daily_rules)


def daily_4():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    daily_main = f"Daily 4 lucky numbers: {set_1, set_2, set_3, set_4}"
    daily_now = f"Now you have to decide to play these numbers Straight, Box, Straight/Box."
    daily_drawings = f"Base ticket prices are $.50 or $1. Drawings are held Mon-Sat 6:59pm ET."       
    daily_rules = f"Official Rules and Play can be found- https://wvlottery.com/draw-games/daily-4 Good Luck!"
    return (daily_main, daily_now, daily_drawings, daily_rules)


def cash_25():
    cash_main = sorted(random.sample(range(1, 26), 6))
    cash_num = f"Cash 25 Lucky Numbers: {cash_main}"
    cash_drawings = f"Base Tickets to play are $1. Draw times are Mon. Tues. Thur. & Fri at 6:59pm ET"
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
       

# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lotto_america_summary(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {star_ball}")

def daily_3_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Daily 3", f"Numbers: {set_1}, {set_2}, {set_3}")

def daily_4_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Daily 4", f"Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def cash_25_summary():
    cash_main = sorted(random.sample(range(1, 26), 6))
    return ("Cash 25", f"Numbers: {cash_main}")

def cash_pop_summary():     
    pop = random.randint(1, 15)
    return ("Cash Pop (Single Number)", f"Number: {pop} ")

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_america_summary,
    "Daily 3": daily_3_summary,
    "Daily 4": daily_4_summary, 
    "Cash 25": cash_25_summary,
    "Cash Pop": cash_pop_summary     
}

# West Virgina Game Choices
wv_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: daily_3,
    5: daily_4,
    6: cash_25,
    7: cash_popWv,
    8: lambda: wv_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]
}


# print the menu
def play_game():
    print("\nWest Virgina Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Daily 3")
    print("5. Daily 4")
    print("6. Cash 25")
    print("7. Cash Pop")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How about Quick Pick all 7 Games")
    
    
    # waiter
    while True:
        try:
            wv_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if wv_lotto_game_choice in wv_lotto_draw_games:                        
                result = wv_lotto_draw_games[wv_lotto_game_choice]()

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

   
# cook
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

