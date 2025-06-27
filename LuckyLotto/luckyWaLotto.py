###########################################################################
#################### Washington Draw Lotto Games ##########################
###########################################################################

###########################################################################
# last file update- 2025/06/26
########################################################################### 


import random

# Washington Game Choices
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Drawings are held Mon. Wed. & Sat. 7:59pm PT." 
    pb_add = f"Available add ons- Power Play and Double Play $1 extra each."
    pb_official = f"Official Rules and Play can be found- https://walottery.com/JackpotGames/Powerball.aspx Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $5. Drawings are held Tues. & Fri. 9pm PT."
    mm_add = f"Megaplier available with every play."
    mm_rules = f"Official Rules and Play can be found- https://walottery.com/JackpotGames/MegaMillions.aspx Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)

def lotto():
    lotto_num = sorted(random.sample(range(1, 50), 6))
    lotto_num2 = sorted(random.sample(range(1, 50), 6))
    lotto_main = f"Lotto Lucky Numbers: \nset 1-{lotto_num}\nset 2-{lotto_num2}"
    lotto_draw = "Ticket price to play $1 for 2 plays. Drawings held Mon. Wed. & Sat. 8pm PT"
    lotto_rules = "Official Rules and Play can be found- https://walottery.com/JackpotGames/Lotto.aspx Good Luck!"
    return (lotto_main, lotto_draw, lotto_rules)


def hit5():
    hit_num = sorted(random.sample(range(1, 43), 5))
    hit_main = f"Hit 5 Lucky Numbers: {hit_num}"
    hit_draw = "Ticket price to play $1. Drawings are held Daily 8pm PT."
    hit_rules = "Official Rules and Play can be found- https://walottery.com/JackpotGames/Hit5.aspx Good Luck!"
    return (hit_main, hit_draw, hit_rules)  


def cash_pop():    
    while True:
        try:
            num_choices = int(input("How many Lucky Cash Pop numbers do you wish to play? Choose 1-15: ").strip())
            if num_choices < 1 or num_choices > 15:
                print("Invalid selection. Please enter a number 1-15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number 1-15.")    
    
    pop = sorted(random.sample(range(1, 15), num_choices))   
    pop_main = f"Lucky Cash Pop Number(s): {pop}"
    pop_drawings = f"Ticket bet amount to play per number- $5" 
    pop_win = f"Winning amount for each number will appear on ticket beside number. If number is drawn you win the amount displayed. "  
    pop_rules = f"Official Rules and Play can be found- https://walottery.com/JackpotGames/CashPop.aspx Good Luck!"    
    return (pop_main, pop_drawings,pop_win, pop_rules) 


def match4():
    m4_num = sorted(random.sample(range(1, 25), 4))
    m4_main = f"Match 4 Lucky Numbers: {m4_num}"
    m4_draw = "Price to play $2. Drawings held Daily 8pm PT."
    mm4_rules = "Official Rules and Play can be found- https://walottery.com/JackpotGames/Match4.aspx Good Luck!"
    return (m4_main, m4_draw, mm4_rules)


def pick3():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    p3_main = f"Pick 3 Lucky Numbers: {set_1}, {set_2}, {set_3}"
    p3_now = f"Multiple ways to Bet, Play, and Win!!!"
    p3_drawings = f"Drawings held Daily 8pm PT."       
    p3_rules = f"Official Rules and Play can be found- https://walottery.com/JackpotGames/Pick3.aspx Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)


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
    lotto_num = sorted(random.sample(range(1, 50), 6))
    lotto_num2 = sorted(random.sample(range(1, 50), 6))
    return ("Washington Lotto", f"Numbers: \nset 1{lotto_num}\nset 2{lotto_num2}")

def hit5_summary():
    hit_num = sorted(random.sample(range(1, 43), 5))
    return ("Hit 5", f"Numbers: {hit_num}")

def pop_summary():
    pop = random.randint(1, 15)
    return ("Cash Pop", f"Number: {pop}")

def match4_summary():
    m4_num = sorted(random.sample(range(1, 25), 4))
    return ("Match 4", f"Numbers: {m4_num}")

def pick3_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)   
    set_3 = random.randint(0, 9)
    return ("Pick 3", f"Numbers: {set_1}, {set_2}, {set_3}")
    

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Lotto": lotto_summary,
    "Hit 5": hit5_summary,
    "Cash Pop": pop_summary,
    "Match 4": match4_summary,
    "Pick 3": pick3_summary
}

# Washington Game Choices
wa_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: lotto,
    4: hit5,
    5: cash_pop,
    6: match4,
    7: pick3,
    8: lambda: wa_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]    
}


# print the menu
def play_game():
    print("\nWashington Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto")
    print("4. Hit 5")
    print("5. Cash Pop")
    print("6. Match 4")
    print("7. Pick 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")
    
    #waiter
    while True:
        try:
            wa_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if wa_lotto_game_choice in wa_lotto_draw_games:                        
                result = wa_lotto_draw_games[wa_lotto_game_choice]()

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

