###########################################################################
##################### Colorado Draw Lotto Games ###########################
###########################################################################

###########################################################################
# last file update- 2025/05/06
###########################################################################

import random

# Colorado Game Choices
def powerballl(): 
    pb_main = sorted(random.sample(range(1, 70), 5))
    pb_rb = random.sample(range(1, 27), 1)[0]
    pb_luck = f"Powerball Lucky Numbers: {pb_main}, Powerball: {pb_rb}." 
    pb_draw = f"Base ticket price $2. Cut-off time to play is 8:00pm MT night of drawings. Drawings are held Mon. Wed. & Sat. 8:59pm ET." 
    pb_add = f"Available add ons- Power Play and Double Play each for $1 extra."
    pb_official = f"Official Rules and Play can be found- https://www.powerball.com Good Luck!"    
    return (pb_luck, pb_draw, pb_add, pb_official)


def mega_millions():
    main_num = sorted(random.sample(range(1, 71), 5))
    megaball = random.sample(range(1, 26), 1)[0]
    mm_numbers_main = f"Mega Millions Lucky Numbers: {main_num}, Mega Ball: {megaball}"
    mm_drawings = f"Base ticket price $2. Cut-off time to play is 8pm MT night of drawings. Drawings are held Tues. Fri. 9pm MT."
    mm_add = f"Available add on- Megaplier $1 extra."
    mm_rules = f"Official Rules and Play can be found- https://www.megamillions.com Good Luck!"    
    return (mm_numbers_main, mm_drawings, mm_add, mm_rules)


def lucky_for_life_co():
    life_main = sorted(random.sample(range(1, 49), 5))
    lucky_ball = random.sample(range(1, 19), 1)[0]
    life_return = f"Lucky For Life Lucky Numbers: {life_main}, Lucky Ball: {lucky_ball}."
    life_drawings = f"Base ticket price $2. Cut-off time to play is 7:30pm MT each night. Drawings are held Nightly 8:30pm MT."    
    life_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/luckyforlife/ Good Luck!"    
    return (life_return, life_drawings, life_rules)


def co_lotto():
    co_main = sorted(random.sample(range(1, 41), 6))
    co_return = f"Colorado Lotto+ Lucky Numbers: {co_main}."
    co_draw = f"Base ticket cost $2. Top Prize up to $250,000. Drawings held Mon, Wed, Sat."
    co_add = f"Available add-on- Play Plus $1"
    co_rules = f"Official Rules and Play can be found- https://www.coloradolottery.com/en/games/lotto/ Good Luck!"
    return(co_return, co_draw, co_add, co_rules)










