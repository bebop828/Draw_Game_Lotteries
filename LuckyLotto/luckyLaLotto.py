###########################################################################
#################### Louisiana Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/07/20
###########################################################################


import random

# Louisiana Game Choices 
def powerball():
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.randint(1, 26)
    pb_luck = f"\nPowerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = "Ticket price to play $2. Drawings are held Mon. Wed. & Sat. 9:59 p.m CST." 
    pb_add = "Available add on- Power Play $1 extra."
    pb_official = "Official Rules and Play can be found- https://louisianalottery.com/draw-games/powerball/ Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)

def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.randint(1, 25)
    mm_numbers_main = f"\nMega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Ticket price to play $5."
    mm_drawings2 = "Mega Millions drawings are broadcast live from Atlanta, Georgia on Tues & Fri 10 p.m. CST. "
    mm_add = "Megaplier available with every play."
    mm_rules = "Official Rules and Play can be found- https://louisianalottery.com/draw-games/mega-millions/ Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_drawings2, mm_add, mm_rules)

def la_lotto():
    lott_main = sorted(random.sample(range(1, 43), 6))
    lott_numbers_main = f"\nLucky Louisiana Lotto Numbers: {lott_main}"
    lott_drawings = "Ticket price to play $1. Drawings are held Wed. & Sat. 9:59pm."
    lott_official = "Official Rules and Play can be found- https://louisianalottery.com/lotto/tab/how-to-play/how-to-play Good Luck!"
    return (lott_numbers_main, lott_drawings, lott_official)

def easy_5():
    easy_main = sorted(random.sample(range(1, 38), 5))
    easy_numbers_main = f"\nLucky Easy 5 Lotto Numbers: {easy_main}"
    easy_drawings = "Ticket price to play $1. Drawings are held Wed. & Sat."
    easy_add = "Available add on- EZMatch $1 extra"
    easy_rules = "Official Rules and Play can be found- https://louisianalottery.com/easy-5/tab/how-to-play Good Luck!"
    return (easy_numbers_main, easy_drawings, easy_add, easy_rules)

def la_pic_3():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    p3_main = f"\nPick 3 Lucky Numbers: {set_1, set_2, set_3}"
    p3_now = "Multiple ways to Play and Win!!!"
    p3_drawings = "Ticket prices to play are $.50 or $1. Drawings held Daily."      
    p3_rules = "Official Rules and Play can be found- https://louisianalottery.com/pick-3/tab/how-to-play Good Luck!"    
    return (p3_main, p3_now, p3_drawings, p3_rules)

def la_pic_4():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    p4_main = f"\nPick 4 Lucky Numbers: {set_1, set_2, set_3, set_4}"
    p4_now = "Multiple ways to Play and Win!!!"
    p4_drawings = "Ticket prices to play $.50 or $1. Drawings held Daily."      
    p4_rules = "Official Rules and Play can be found- https://louisianalottery.com/pick-4/tab/how-to-play Good Luck!"    
    return (p4_main, p4_now, p4_drawings, p4_rules)

def la_pic_5():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    p5_main = f"\nPick 5 Lucky Numbers: {set_1, set_2, set_3, set_4, set_5}"
    p5_now = "Multiple ways to Play and Win!!!"
    p5_drawings = "Ticket prices to play $.50 or $1. Drawings held Daily."      
    p5_rules = "Official Rules and Play can be found- https://louisianalottery.com/pick-5/tab/how-to-play Good Luck!"    
    return (p5_main, p5_now, p5_drawings, p5_rules)


# summary for each game
def powerball_summary():
    main = sorted(random.sample(range(1, 70), 5))
    rb = random.randint(1, 26)
    return ("Powerball", f"Numbers: {main}, Powerball: {rb}")

def mega_summary():
    main_mm = sorted(random.sample(range(1, 71), 5))
    mb = random.randint(1, 25)
    return ("Mega Millions", f"Numbers: {main_mm}, Mega Ball: {mb}")

def la_lotto_summary():
    lott_main = sorted(random.sample(range(1, 43), 6))
    return ("Louisiana Lotto", f"Numbers: {lott_main}")

def easy_5_summary():
    easy_main = sorted(random.sample(range(1, 38), 5))
    return ("Easy 5 with EZ Match", f"Numbers: {easy_main}")

def la_pic_5_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    set_5 = random.randint(0, 9)
    return (f"Pick 5 Lucky Numbers: {set_1}, {set_2}, {set_3}, {set_4}, {set_5}")

def la_pic_4_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    set_4 = random.randint(0, 9)
    return (f"Pick 4 Lucky Numbers: {set_1}, {set_2}, {set_3}, {set_4}")

def la_pic_3_summary():
    set_1 = random.randint(0, 9)
    set_2 = random.randint(0, 9)
    set_3 = random.randint(0, 9)
    return (f"Pick 3 Numbers: {set_1}, {set_2}, {set_3}")

# summaries
summary_lotto_draw_games = {
    "Powerball": powerball_summary,
    "Mega Millions": mega_summary,
    "Louisiana Lotto": la_lotto_summary,
    "Easy 5 with EZ Match": easy_5_summary,
    "Pick 5": la_pic_5_summary,
    "Pick 4": la_pic_4_summary,
    "Pick 3": la_pic_3_summary
}


# Louisiana Game Choices
la_lotto_draw_games = {
    1: powerball,
    2: mega_millions,
    3: la_lotto,
    4: easy_5,
    5: la_pic_5,
    6: la_pic_4,
    7: la_pic_3,
    8: lambda: la_lotto_draw_games[random.randint(1, 7)](),
    9: lambda: [func() for func in summary_lotto_draw_games.values()]    
}


# print the menu
def play_game():
    print("\nLouisiana Lotto Game Choices:")
    print("1. Powerball")
    print("2. Mega Millions")
    print("3. Lotto")
    print("4. Easy 5")
    print("5. Pick 5")
    print("6. Pick 4")
    print("7. Pick 3")
    print("8. Can't Decide? Try Random Game!!!")
    print("9. How About Quick Pick All 7 Games")

    #waiter
    while True:
        try:
            la_lotto_game_choice = int(input("\nWhich Lucky Game would you like to try: "))
            if la_lotto_game_choice in la_lotto_draw_games:                        
                result = la_lotto_draw_games[la_lotto_game_choice]()

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

print("Please note On-line purchase of lotto draw games are not prohibited in Louisiana.")
print("However, for purchases, please see an official lotto retailer.")

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