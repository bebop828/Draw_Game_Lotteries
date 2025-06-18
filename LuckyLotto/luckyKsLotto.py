########################################################################### 
#################### Kansas Draw Lotto Games ##############################
###########################################################################

###########################################################################
# last file update- 2025/06/18
# Kansas has Keno. 
# Keno not currently included in file
########################################################################### 



import random

# Kansas Game Choices 
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 9:59pm CT" 
    pb_add = f"Powerplay add on $1 extra."    
    pb_official = f"Official Rules and Play can be found- https://www.kslottery.com/games/jackpot/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Drawings are held Tues. & Fri."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.kslottery.com/games/jackpot/megamillions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = f"Ticket price $1. Drawings are held Mon. Wed. & Sat. 9:15pm CT"
    lotto_add = f"Add on- All-Star Multiplier available for $1 extra"
    lotto_rules = f"Official Rules and Play can be found- https://www.kslottery.com/games/jackpot/lottoamerica/ Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"Lucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = f"Ticket price $2. Drawings held Daily 8:39pm CT"
    lucky_rules = f"Official Rules and Gameplay can be found- https://www.kslottery.com/games/jackpot/luckyforlife/ Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def super_k(): 
    super_num = sorted(random.sample(range(1, 33), 5))
    cash_ball = random.randint(1, 25)
    super_num2 = sorted(random.sample(range(1, 33), 5))
    cash_ball2 = random.randint(1, 25)
    super_main = f"Super Kansas Ca$h Lucky Board 1: {super_num}, Cash Ball: {cash_ball}"
    super_main2 = f"Super Kansas Ca$h Lucky Board 2: {super_num2}, Cash Ball: {cash_ball2}"
    super_draw = f"Ticket price to play $1 for 2 boards. Drawings held Mon. Wed. & Sat."
    super_rules = f"Official Rules and Play can be found- https://www.kslottery.com/games/jackpot/kansascash/ Good Luck!"
    return (super_main, super_main2, super_draw, super_rules)


def two_by_two(): 
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    two_main = f"2 by 2 Lucky Red and White Numbers: Red- {two_num_rd}, White- {two_num_wt}"
    two_draw = f"Ticket price $1. Drawings held Daily around 9:30pm CT"
    two_rules = f"Official Rules and Play cab be found- https://www.kslottery.com/games/dailydraw/twobytwo/"
    return (two_main, two_draw, two_rules)


def pick3():
    while True: 
        print("Select a game time to play:")
        print("1. Mid-day Draw 1:10pm CT")
        print("2. Evening Draw 9:10pm CT")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Mid-day Draw',
            2: 'Evening Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    p3_main = f"Pick 3 Lucky Numbers for {game_time}: {set_1, set_2, set_3}"
    p3_now = f"Play Types for Pick 3: Exact or Any Order"
    p3_drawings = f"Ticket price $1. Drawings held Daily."         
    p3_rules = f"Official Rules and Play can be found- https://www.kslottery.com/games/dailydraw/pick3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


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

def super_k_summary(): 
    super_num = sorted(random.sample(range(1, 33), 5))
    cash_ball = random.randint(1, 25)
    super_num2 = sorted(random.sample(range(1, 33), 5))
    cash_ball2 = random.randint(1, 25)
    return ("Super Kansas Ca$h", f"Board 1: {super_num}, CB: {cash_ball} Board 2: {super_num2}, CB: {cash_ball2}")

def two_by_two_summary():
    two_num_rd = sorted(random.sample(range(1, 27), 2))
    two_num_wt = sorted(random.sample(range(1, 27), 2))
    return(f"2 by 2: Red- {two_num_rd}, White- {two_num_wt}")

def pick3_summary():    
    draw_time = random.choice(["Mid-day", "Evening"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"{draw_time}: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "Super Kansas Ca$h": super_k_summary,
    "2 by 2": two_by_two_summary,
    "Pick 3": pick3_summary,
}


# Kansas Draw Games
ks_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: super_k,
    6: two_by_two,
    7: pick3,
    8: lambda: ks_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]    
}


# print the menu
def play_game():
    print("\nKansas Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. Super Kansas Ca$h")
    print("6. 2 by 2")
    print("7. Pick 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")
    
    #waiter
    while True:
        try:
            ks_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if ks_lotto_game_choice in ks_lotto_draw_games:                        
                result = ks_lotto_draw_games[ks_lotto_game_choice]()

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




