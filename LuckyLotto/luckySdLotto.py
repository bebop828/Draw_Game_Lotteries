###########################################################################
################## South Dakota  Draw Lotto Games ##########################
###########################################################################

###########################################################################
# last file update- 2025/06/26
########################################################################### 


import random

# South Dakota Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://lottery.sd.gov/game/powerball-power-play/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. Fri."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://lottery.sd.gov/game/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america(): 
    lotto_main = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_num = f"Lucky Lotto America Numbers: {lotto_main}, Star Ball: {star_ball}."
    lotto_drawings = f"Ticket price to play $1. Drawings are held Mon. Wed. & Sat."        
    lotto_rules = f"Official Rules and Play can be found- https://lottery.sd.gov/game/lotto-america/ Good Luck!"    
    return (lotto_num, lotto_drawings, lotto_rules)


def lucky_life():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    life_return = f"Lucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Ticket price to play $2. Drawings are held Daily"    
    life_rules = f"Official Rules and Play can be found- https://lottery.sd.gov/game/lucky-for-life/ Good Luck!"    
    return (life_return, life_drawings, life_rules)


def dakota_cash():
    cash_num = sorted(random.sample(range(1, 36), 5))
    cash_main = f"Dakota Ca$h Lucky Numbers: {cash_num}"
    cash_draw = "Ticket price to play is $1. Drawings are held every Wed. & Sat."
    cash_add = "Available add on- EZ Match $1."
    cash_rules = "Official Rules and Play can be found- https://lottery.sd.gov/game/dakota-cash/ Good Luck!"
    return (cash_main, cash_draw, cash_add, cash_rules)


# summary for each game
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

def dakota_cash_summary():
    cash_num = sorted(random.sample(range(1, 36), 5))
    return ("Dakota Ca$h", f"Numbers: {cash_num}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "Dakota Ca$h": dakota_cash_summary
}

# South Dakota Draw Games
sd_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: dakota_cash,
    6: lambda: sd_lotto_draw_games[random.randint(1, 5)](),
    7: lambda: [func() for func in summary_lotto_draw_games.values()]         
}


#print the menu
def play_game():
    print("\nSouth Dakota Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. Dakota Ca$h")
    print("6. Can't Decide? Try Random Game!!!")
    print("7. How About Quick Pick All 5 Games")
    
    # waiter
    while True:
        try:
            sd_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if sd_lotto_game_choice in sd_lotto_draw_games:                        
                result = sd_lotto_draw_games[sd_lotto_game_choice]()

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

