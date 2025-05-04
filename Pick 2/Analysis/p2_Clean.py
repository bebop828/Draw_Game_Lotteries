#######################################################
############## PICK 2 with FIREBALL ###################
################## Clean File #########################
#######################################################

#######################################################
# last update- 2025/05/04 
#######################################################

import pandas as pd
import re

data = pd.read_csv('CSV/pick2.csv', header=None, dtype=str)
drop_pattern = r'PICK 2|E: Evening and M: Midday drawing results'
data = data[~data[0].str.contains(drop_pattern, na=False)]

def split_entries(row):    
    return re.findall(r'\d{2}/\d{2}/\d{2} [EM] \d+- \d+ FB \d+', row)

all_entries = []
for line in data[0]:
    all_entries.extend(split_entries(line))

data_clean = pd.DataFrame(all_entries, columns=['raw'])

pattern = r'(\d{2}/\d{2}/\d{2}) ([EM]) (\d+)- (\d+) FB (\d+)'
data_clean[['Date', 'Draw', '1st', '2nd', 'FB']] = data_clean['raw'].str.extract(pattern)
data_clean = data_clean.drop(columns=['raw']).dropna()

# Data type convertion 
data_clean['Date'] = pd.to_datetime(data_clean['Date'], format='%m/%d/%y')
data_clean['Day'] = data_clean['Date'].dt.day_name()
new_order = ['Date', 'Day', 'Draw','1st', '2nd', 'FB']
data_clean = data_clean[new_order]
to_convert = ['1st', '2nd', 'FB']
data_clean[to_convert] = data_clean[to_convert].astype(int)
data_clean = data_clean.sort_values(by='Date', ascending=False)

#cleaned data to csv
data_clean.to_csv('CSV/pick2_updated.csv', index=False) #this can be titled anything you want for the cleaned data


###############################################################################
############ CSV data start- 1/18/21 Start of the FIREBALL GAMEPLAY ###########
###############################################################################
