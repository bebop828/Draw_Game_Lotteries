###################################################################
################ Nebraska Draw Lotto Games ########################
###################################################################

###################################################################
# last file update- 2025/08/14
################################################################### 


import random
import datetime
 
#Nebraska Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Available add on- Powerplay $1. extra"    
    pb_official = "Official Rules and Play can be found- https://nelottery.com/homeapp/lotto/28/gamedetail Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price to play $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://nelottery.com/homeapp/lotto/30/gamedetail Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"\nLotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = "Ticket price to play $1. Drawings are held Mon. Wed. & Sat."
    lotto_add = "Add on- All-Star Multiplier available for $1 extra"
    lotto_rules = "Official Rules and Play can be found- https://nelottery.com/homeapp/lotto/40/gamedetail Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"\nLucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price to play $2. Drawings held Daily."
    lucky_rules = "Official Rules and Gameplay can be found- https://nelottery.com/homeapp/lotto/37/gamedetail Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def myday():
    while True:        
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        year1 = random.randint(0, 9)
        year2 = random.randint(0, 9)
        year_last_two = int(f"{year1}{year2}")

        try:
            # Construct a date string to validate
            date_str = f"{month:02d}/{day:02d}/{year_last_two:02d}"
            
            # Check for leap year rules manually if February 29
            if month == 2 and day == 29:
                if year_last_two % 4 != 0:
                    continue  # not a leap year
            # Try creating a date with dummy century
            datetime.datetime.strptime(f"{month:02d}/{day:02d}/2000", "%m/%d/%Y").replace(day=day)
        except ValueError:
            continue  # invalid date like April 31
        
        # Format the result
        myday_num = f"\nMyDaY Lucky Numbers: Month: {month:02d}, Day: {day:02d}, Year: {year1}{year2}"
        myday_draw = "Ticket price to play $1. Drawings are held Daily."
        myday_rules = "Official Rules and Play: https://nelottery.com/homeapp/lotto/33/gamedetail Good Luck!"
        return (myday_num, myday_draw, myday_rules)


def two_by_two(): 
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    two_main = f"\n2 by 2 Lucky Red and White Numbers: Red- {two_num_rd}, White- {two_num_wt}"
    two_draw = "Ticket price to play $1. Drawings held Daily."
    two_rules = "Official Rules and Play cab be found- https://nelottery.com/homeapp/lotto/34/gamedetail Good Luck!"
    return (two_main, two_draw, two_rules)


def pick5():
    pick5_num = sorted(random.sample(range(1, 41), 5))
    pick5_main = f"\nPick 5 Lucky Numbers: {pick5_num}"
    pick5_draw = "Ticket prices to play $1. Drawings held Daily."
    pick5_rules = "Official Rules and Play can be found- https://nelottery.com/homeapp/lotto/31/gamedetail Good Luck!"
    return (pick5_main, pick5_draw, pick5_rules)


def pick3(): 
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    pick3_main = f"\nPick 3 Lucky Numbers: {set_1}, {set_2}, {set_3}"
    pick3_draw = "Ticket price to Play $1. Drawings held Daily."
    pick3_win = "Multiple ways to Play and Win!!!"
    pick3_rules = "Official Rules and Play can be found- https://nelottery.com/homeapp/lotto/32/gamedetail Good Luck!"
    return (pick3_main, pick3_draw, pick3_win, pick3_rules)


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

def myday_summary():
    while True:        
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        year1 = random.randint(0, 9)
        year2 = random.randint(0, 9)
        year_last_two = int(f"{year1}{year2}")

        try:            
            date_str = f"{month:02d}/{day:02d}/{year_last_two:02d}"            
            
            if month == 2 and day == 29:
                if year_last_two % 4 != 0:
                    continue  
                
            datetime.datetime.strptime(f"{month:02d}/{day:02d}/2000", "%m/%d/%Y").replace(day=day)
        except ValueError:
            continue         
        
        myday_num = f"MyDaY: Month: {month:02d}, Day: {day:02d}, Year: {year1}{year2}"
        return (myday_num)
    
def two_by_two_summary():
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    return("2 by 2", f"Red- {two_num_rd}, White- {two_num_wt}")

def pick5_summmary():
    pick5_num = sorted(random.sample(range(1, 41), 5))
    return ("Pick 5", f"Numbers: {pick5_num}")

def pick3_summary(): 
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "MyDaY": myday_summary,
    "2 by 2": two_by_two_summary,
    "Pick 5": pick5_summmary,
    "Pick 3": pick3_summary
}


#Nebraska Draw Games
ne_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: myday,
    6: two_by_two,
    7: pick5,
    8: pick3,
    9: lambda: ne_lotto_draw_games[random.randint(1, 11)](),
    10: lambda: [func() for func in summary_lotto_draw_games.values()] 
}


# print the menu
def play_game():
    print("\nNebraska Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. MyDaY")
    print("6. 2 by 2")
    print("7. Pick 5")
    print("8. Pick 3")
    print("9. Can't Decide? Try Random Game!!!")
    print("10. How About Quick Pick All 8 Games") 
    
    #waiter
    while True:
        try:
            ne_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ne_lotto_game_choice in ne_lotto_draw_games:                        
                result = ne_lotto_draw_games[ne_lotto_game_choice]()

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
    
 