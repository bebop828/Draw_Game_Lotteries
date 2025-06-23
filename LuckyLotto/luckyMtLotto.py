###################################################################
################# Montana Draw Lotto Games ########################
###################################################################

###################################################################
# last file update- 2025/06/18
###################################################################  


import random
 
#Montana Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $3. Drawings are held Mon. Wed. & Sat. 8:59pm MT" 
    pb_add = f"Powerplay option available with every play."
    pb_add2 = f"Double Play add on $1 extra"
    pb_official = f"Official Rules and Play can be found- https://www.montanalottery.com/en/view/game/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_add2, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Drawings are held Tues. & Fri. 9pm MT"
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.montanalottery.com/en/view/game/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = f"Ticket price $1. Drawings are held Mon, Wed, Sat 9pm MT"
    lotto_add = f"Add on- All-Star Multiplier available for $1 extra"
    lotto_rules = f"Official Rules and Play can be found- https://www.montanalottery.com/en/view/game/lotto-america Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"Lucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = f"Ticket price $2. Drawings held Daily at 8:35pm MT"
    lucky_rules = f"Official Rules and Gameplay can be found- https://www.montanalottery.com/en/view/game/lucky-for-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def montana_cash():
    montana_num = sorted(random.sample(range(1, 46), 5))
    montana_main = f"Lucky Montana Cash with Max Cash Numbers: {montana_num}"
    montana_draw = f"Ticket price to play $1. Drawings held Wed. & Sat. 8pm MT"
    montana_add = f"Available add on- Max Cash $1"
    montana_rules = f"Official Rules and Play can be found- https://www.montanalottery.com/en/view/game/montana-cash Good Luck!"
    return (montana_main, montana_draw, montana_add, montana_rules)


def big_sky():
    big_num = sorted(random.sample(range(1, 32), 4))
    big_bonus = random.randint(1, 16)
    big_main = f"Big $ky Bonus Lucky Numbers: {big_num}, Bonus Ball: {big_bonus}"
    big_draw = f"Ticket price to play $2. Drawings held Daily at 7:30pm MT"
    big_rules = f"Official Rules and Play can be found- https://www.montanalottery.com/en/view/game/big-sky-bonus Good Luck!"
    return (big_main, big_draw, big_rules)


# Summary For Each Game 
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lotto_summary():
    lotto_main = sorted(random.sample(range(1, 53), 5))
    lotto_star = random.randint(1, 10)
    return ("Lotto America", f"Numbers: {lotto_main}, Star Ball: {lotto_star}")

def lucky_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    life_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {life_ball}")

def montana_cash_summary():
    montana_num = sorted(random.sample(range(1, 46), 5))
    return ("Montana Ca$h", f"Numbers: {montana_num}")

def big_sky_summary():
    big_num = sorted(random.sample(range(1, 32), 4))
    big_bonus = random.randint(1, 16)
    return ("Big $ky Bonus", f"Numbers: {big_num}, Bonus Ball: {big_bonus}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "Montana Cash": montana_cash_summary,
    "Big $ky Bonus": big_sky_summary
}


#draw games
mt_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: montana_cash,
    6: big_sky,
    7: lambda: mt_lotto_draw_games[random.randint(1, 7)](),
    8: lambda: [func() for func in summary_lotto_draw_games.values()]    
}


#print the menu
def play_game():
    print("\nMontana Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. Montana Cash with Max Cash")
    print("6. Big $ky Bonus")
    print("7. Can't Decide? Try Random Game!!!")
    print("8. How About Quick Pick All 7 Games")
    
    #waiter
    while True:
        try:
            mt_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if mt_lotto_game_choice in mt_lotto_draw_games:                        
                result = mt_lotto_draw_games[mt_lotto_game_choice]()

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
    
    




