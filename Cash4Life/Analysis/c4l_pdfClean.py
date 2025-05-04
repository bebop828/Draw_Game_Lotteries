##################################################
######### Cash4Life Data Clean File ##############
##################################################

##################################################
# last updated 2025/05/04
##################################################

import pandas as pd 
import re   

data = pd.read_csv('CSV/c4l_5-3.csv', header=None, dtype=str) #just replace the csv file name if download an updated PDF version

#clean and organize data
data = data[~data[0].str.contains('CASH4LIFE', na=False)]

def split_entries(row):
    # This regex matches the pattern ending with 'CB <number>'
    entries = re.findall(r'\d{2}/\d{2}/\d{2}.*?CB \d+', row)
    return entries

# flatten all entries 
all_entries = []
for line in data[0]:
    all_entries.extend(split_entries(line))

#single-column, one entry per row
data = pd.DataFrame(all_entries, columns=['raw'])
pattern = r'(\d{2}/\d{2}/\d{2})\s+(\d+)-\s+(\d+)-\s+(\d+)-\s+(\d+)-\s+(\d+)\s+CB\s+(\d+)'

# str.extract
data[['Date', '1st', '2nd', '3rd', '4th', '5th', 'CB']] = data['raw'].str.extract(pattern)

# Drop 'raw' and any missing values
data = data.drop(columns=['raw'])
data = data.dropna()

#convert datatypes
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')
data = data.sort_values(by='Date', ascending=False)
data = data.reset_index(drop=True)
data['Day'] = data['Date'].dt.day_name()
new_order = ['Date', 'Day', '1st', '2nd', '3rd', '4th', '5th', 'CB']
data = data[new_order]
to_convert = ['1st', '2nd', '3rd', '4th', '5th', 'CB']
data[to_convert] = data[to_convert].astype(int)

#cleaned data to csv
data.to_csv('CSV/c4l_updated.csv', index=False, date_format='%m/%d/%Y') #this can be titled anything you want for the cleaned data
