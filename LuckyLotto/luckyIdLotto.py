###################################################################
################## Idaho Draw Lotto Games #########################
###################################################################

###################################################################
# last file update- 2025/05/25
################################################################### 


import random
 
#Idaho Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $3. Drawings are held Mon. Wed. & Sat." 
    pb_add = f"Powerplay option available with every play."
    pb_add2 = f"Double Play add on $1 extra"
    pb_official = f"Official Rules and Play can be found- https://www.idaholottery.com/games/draw/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_add2, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price $5. Drawings are held Tues. Fri."
    mm_add = f"Megaplier included with each Gameplay."
    mm_rules = f"Official Rules and Play can be found- https://www.idaholottery.com/games/draw/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lotto_america():
    lotto_num = sorted(random.sample(range(1, 53), 5))
    star_ball = random.randint(1, 10)
    lotto_main = f"Lotto America with All-Star Ball Lucky Numbers: {lotto_num}, Star Ball: {star_ball}"
    lotto_draw = f"Ticket price $1. Drawings are held Mon, Wed, Sat 9pm MT"
    lotto_add = f"Add on- All-Star Multiplier available for $1 extra"
    lotto_rules = f"Official Rules and Play can be found- https://www.idaholottery.com/games/draw/lotto-america Good Luck!"
    return (lotto_main, lotto_draw, lotto_add, lotto_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"Lucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = f"Ticket price $2. Drawings held Everyday at 8:35pm MT"
    lucky_rules = f"Official Rules and Gameplay can be found- https://www.idaholottery.com/games/draw/lucky-for-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def idaho_cash(): 
    cash_num = sorted(random.sample(range(1, 46), 5))
    cash_main = f"Idaho Cash Lucky Numbers: {cash_num}"
    cash_draw = f"Ticket price $1. Drawings held Nightly at 8pm MT."
    cash_rules = f"Official Rules and Gameplay can be found- https://www.idaholottery.com/games/draw/idaho-cash Good Luck!"
    return (cash_main, cash_draw, cash_rules)


def pick3():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm MT Draw")
        print("2. Night 7:59pm MT Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
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
    p3_now = f"Multiple ways to Play and WIN!!! Check official site for Gameplay."
    p3_drawings = f"Ticket price $1. Drawings held Daily: Day 1:59pm MT and Night 7:59pm MT." 
    p3_add = f'Available Add-on is "Sum it Up" for $1 extra.'     
    p3_rules = f"Official Rules and Play can be found- https://www.idaholottery.com/games/draw/pick-3 Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_add, p3_rules)



def pick4():
    while True: 
        print("Select a game time to play:")
        print("1. Day 1:59pm MT Draw")
        print("2. Night 7:59pm MT Draw")

        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
            2: 'Night Draw'
        }    

        if choice not in game_time_mapping:
            print("Invalid selection. Please choose 1 or 2")
            continue

        game_time = game_time_mapping[choice]
        break
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    p4_main = f"Pick 4 Lucky Numbers for {game_time}: {set_1, set_2, set_3, set_4}"
    p4_now = f"Multiple ways to Play and WIN!!! Check official site for Gameplay."
    p4_drawings = f"Ticket price $1 Drawings held Daily: Day 1:59pm MT and Night 7:59pm MT." 
    p4_add = f'Available Add-on is "Sum it Up" for $1 extra.'     
    p4_rules = f"Official Rules and Play can be found- https://www.idaholottery.com/games/draw/pick-4 Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_add, p4_rules)


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

def idaho_summary(): 
    cashId_num = sorted(random.sample(range(1, 46), 5))
    return ("Idaho Cash", f"Numbers: {cashId_num}")

def pick3_summary():    
    draw_time = random.choice(["Day 1:59pm MT", "Night 7:59pm MT"])    
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"{draw_time}: Numbers: ({set_1}, {set_2}, {set_3})")

def pick4_summary(): 
    draw_time4 = random.choice(["Day 1:59pm MT", "Night 7:59pm MT"])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4", f"{draw_time4}: Numbers: ({set_1}, {set_2}, {set_3}, {set_4})")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto America": lotto_summary,
    "Lucky for Life": lucky_summary,
    "Idaho Cash": idaho_summary,
    "Pick 3": pick3_summary,
    "Pick 4": pick4_summary
}

#draw games
id_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto_america,
    4: lucky_life,
    5: idaho_cash,
    6: pick3,
    7: pick4,
    8: lambda: id_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]    
}


#print the menu
def play_game():
    print("Idaho Lotto Game Choices")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto America")
    print("4. Lucky for Life")
    print("5. Idaho Cash")
    print("6. Pick 3")
    print("7. Pick 4")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")    
    
    #waiter
    while True:
        try:
            id_lotto_game_choice = int(input("Which Lucky Game would you like to try: "))
            if id_lotto_game_choice in id_lotto_draw_games:                        
                result = id_lotto_draw_games[id_lotto_game_choice]()

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
