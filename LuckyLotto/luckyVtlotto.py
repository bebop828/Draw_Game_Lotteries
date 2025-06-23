###################################################################
################ Vermont Draw Lotto Games #########################
###################################################################

###################################################################
# last file update- 2025/06/23
################################################################### 


import random
 
# Vermont Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Base ticket price $2. Drawings are held Mon. Wed. & Sat." 
    pb_add = "Powerplay add on $1."    
    pb_official = "Official Rules and Play can be found- https://vtlottery.com/games/powerball Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = "Ticket price $5. Drawings are held Tues. & Fri."
    mm_add = "Megaplier included with each Gameplay."
    mm_rules = "Official Rules and Play can be found- https://vtlottery.com/games/mega-millions Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_life():
    lucky_num = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.randint(1, 18)
    lucky_main = f"Lucky for Life Lucky Numbers: {lucky_num}, Lucky Ball: {lucky_ball}"
    lucky_draw = "Ticket price $2. Drawings held Daily."
    lucky_rules = "Official Rules and Gameplay can be found- https://vtlottery.com/games/lucky-life Good Luck!"
    return (lucky_main, lucky_draw, lucky_rules)


def mega_bucks():
    bucks_num = sorted(random.sample(range(1, 42), 5))
    bucks_mega = random.randint(1, 6)
    bucks_main = f"Lucky MegaBucks Numbers: {bucks_num}, Mega Number: {bucks_mega}"
    bucks_draw = "Ticket price to play $2. Drawings held Mon. Wed. & Sat."
    bucks_rules = "Official Rules and Play can be found- https://vtlottery.com/games/megabucks Good Luck!"
    return (bucks_main, bucks_draw, bucks_rules)

    
def gimme():
    gimme_num = sorted(random.sample(range(1, 40), 5))
    gimme_main = f"Gimme 5 Lucky Numbers: {gimme_num}"
    gimme_draw = "Ticket price to play $1. Drawings held Mon-Fri. 7pm ET"
    gimme_rules = "Official Rules and Play can be found- https://vtlottery.com/games/gimme-5"
    return (gimme_main, gimme_draw, gimme_rules)


def pick4():
    while True:
        print("Make a Game Time Selection: ")
        print("1. Day Draw 1:10pm")
        print("2. Evening Draw 6:55pm")
        
        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
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
    set_4 = random.randint(0, 9)
    p4_main = f"Lucky Pick 4 Numbers: {set_1}, {set_2}, {set_3}, {set_4}"
    p4_draw = "Drawings held 2x Daily. Bet amounts range $.50 - $5."
    p4_rules= "Official Rules and Play can be found https://vtlottery.com/games/pick-4 Good Luck!"
    return (p4_main, p4_draw, p4_rules)
    

def pick3():
    while True:
        print("Make a Game Time Selection: ")
        print("1. Day Draw 1:10pm")
        print("2. Evening Draw 6:59pm")
        
        try:
            choice = int(input("Make selection and enter either 1 or 2: ").strip())
        except ValueError:
            print("Invalid input. Please enter either 1 or 2")
            continue

        game_time_mapping = {
            1: 'Day Draw',
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
    set_4 = random.randint(0, 9)
    p4_main = f"Lucky Pick 4 Numbers: {set_1}, {set_2}, {set_3}, {set_4}"
    p4_draw = "Drawings held 2x Daily. Price to Play $1. Multiple ways to play and win!"
    p4_rules= "Official Rules and Play can be found https://vtlottery.com/games/pick-4 Good Luck!"
    return (p4_main, p4_draw, p4_rules)    


# Vermont Game Summaries
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def lucky_summary():
    life_num = sorted(random.sample(range(1, 49), 5))
    life_ball = random.randint(1, 18)
    return ("Lucky for Life", f"Numbers: {life_num}, Lucky Ball: {life_ball}")

def mega_bucks_summary():
    bucks_num = sorted(random.sample(range(1, 42), 5))
    bucks_mega = random.randint(1, 6)
    return ("MegaBucks", f"Numbers: {bucks_num}, Mega: {bucks_mega}")

def gimme_summary():
    gimme_num = sorted(random.sample(range(1, 40), 5))
    return ("Gimme 5", f"Numbers: {gimme_num}")

def pick4_summary():
    draw4 = random.choice(['Day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return ("Pick 4", f"{draw4}: Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def pick3_summary():
    draw3 = random.choice(['Day', 'Evening'])
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"{draw3}: Numbers: {set_1}, {set_2}, {set_3}")

#summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lucky for Life": lucky_summary,
    "MegaBucks": mega_bucks_summary,
    "Gimme 5": gimme_summary,
    "Pick 4": pick4_summary,
    "Pick 3": pick3_summary
}

# Vermont Game Choices
vt_lotto_draw_games = {
    1: powerball, 
    2: mega_millions,
    3: lucky_life,
    4: mega_bucks,
    5: gimme,
    6: pick4, 
    7: pick3,
    8: lambda: vt_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]    
}

# print the menu
def play_game():
    print("\nVermont Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky for Life")
    print("4. MegaBucks")
    print("5. Gimme 5")
    print("6. Pick 4")
    print("7. Pick 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")
    
    #waiter
    while True:
        try:
            vt_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if vt_lotto_game_choice in vt_lotto_draw_games:                        
                result = vt_lotto_draw_games[vt_lotto_game_choice]()

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



