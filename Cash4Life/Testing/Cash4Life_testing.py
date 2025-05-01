############################
####### CASH 4 LIFE ########
############################

############################
# Python file for Multiple #
#### Game Play Drawings ####
############################

############################
# GamePlay Num Generation  #
### Based on Best/Worst  ###
####### Transitions ########
############################

#last update 2025/05/01

import pandas as pd
import random
import os
import csv
from datetime import datetime

#read the data
data = pd.read_csv('CSV/c4l_updated.csv')

#data splits
start_date = '02-20-2017'
data_complete = data[data['Date'] >= start_date]
data_mon = data[data['Day'] == "Monday"]
data_tues = data[data['Day'] == "Tuesday"]
data_wed = data[data['Day'] == "Wednesday"]
data_thur = data[data['Day'] == "Thursday"]
data_fri = data[data['Day'] == "Friday"]
data_sat = data[data['Day'] == "Saturday"]
data_sun = data[data['Day'] == "Sunday"]

#------------------------------------------#
#--- Best Transition Number Generation ----#
#------------------------------------------#
class LotteryAnalyzer:
    def __init__(self, data_complete, name):
        self.data_complete = data_complete
        self.name = name
        self.data_complete_hot_cold = None
        self.transition_probs = {}
        self.hot_cold_probs = {}
        self.number_columns = ['1st', '2nd', '3rd', '4th', '5th', 'CB']
        self.valid_ranges = {
            "1st": (1, 56),
            "2nd": (2, 57),
            "3rd": (3, 58),
            "4th": (4, 59),
            "5th": (5, 60),
            "CB": (1, 4)
        }  

    def best_assign_HC(self):
        self.data_complete_hot_cold = self.data_complete.copy()
        for col in self.number_columns:
            self.data_complete_hot_cold[f'{col}_H/C'] = self._best_assign_HC_column(self.data_complete_hot_cold[col])

    def _best_assign_HC_column(self, series):
        counts = series.value_counts()
        percentiles = counts.rank(pct=True)
        return series.map(lambda x: 'Hot' if percentiles[x] >= 0.80 else ('Cold' if percentiles[x] <= 0.35 else 'Mid'))

    def calculate_transition_probs(self):
        for column in self.number_columns:
            self.transition_probs[column] = self._calculate_transition_prob(self.data_complete_hot_cold, column)
            self.hot_cold_probs[column] = self._calculate_transition_prob(self.data_complete_hot_cold, f'{column}_H/C')

    def _calculate_transition_prob(self, data_complete, column):
        transitions = data_complete[column].shift().groupby(data_complete[column]).value_counts(normalize=True).unstack()
        return transitions.fillna(0)

    def generate_gameplay_numbers(self):
        gameplay_numbers = []
        previous_number = None
        for column in self.number_columns[:-1]:  # Exclude CB
            best_transition = self._get_best_transition(self.hot_cold_probs[column], previous_number)
            selected_number = self._select_number(column, best_transition, gameplay_numbers)
            gameplay_numbers.append(selected_number)
            previous_number = best_transition
        
        cash_ball = self._select_cash_ball()
        gameplay_numbers.append(cash_ball)
        return gameplay_numbers

    def generate_multiple_gameplay_numbers(self, rounds=20):
        """Generate multiple rounds of gameplay numbers."""
        return [self.generate_gameplay_numbers() for _ in range(rounds)]

    def _get_best_transition(self, transition_matrix, previous_number=None):
        if isinstance(transition_matrix, pd.Series):
            return transition_matrix.idxmax()
        elif previous_number is None:
            return transition_matrix.mean().idxmax()
        else:
            return transition_matrix.loc[previous_number].idxmax()

    def _select_number(self, column, best_transition, gameplay_numbers):
        available_numbers = self.data_complete_hot_cold[
            (self.data_complete_hot_cold[f'{column}_H/C'] == best_transition) & 
            (self.data_complete_hot_cold[column] >= self.valid_ranges[column][0]) & 
            (self.data_complete_hot_cold[column] <= self.valid_ranges[column][1])
        ][column].unique()

        if len(available_numbers) == 0:
            available_numbers = list(range(self.valid_ranges[column][0], self.valid_ranges[column][1] + 1))

        valid_numbers = [n for n in available_numbers if n > (gameplay_numbers[-1] if gameplay_numbers else 0)]
        return int(random.choice(valid_numbers if valid_numbers else available_numbers))  # Ensure int

    def _select_cash_ball(self):
        cash_ball_transition = self._get_best_transition(self.hot_cold_probs['CB'])
        cash_ball_numbers = self.data_complete_hot_cold[
            (self.data_complete_hot_cold['CB_H/C'] == cash_ball_transition) & 
            (self.data_complete_hot_cold['CB'] >= self.valid_ranges['CB'][0]) & 
            (self.data_complete_hot_cold['CB'] <= self.valid_ranges['CB'][1])
        ]['CB'].unique()

        if len(cash_ball_numbers) == 0:
            cash_ball_numbers = list(range(self.valid_ranges['CB'][0], self.valid_ranges['CB'][1] + 1))

        return int(random.choice(cash_ball_numbers))  # Ensure int

# --------------------------------------------------------------------------
# Main Processing
# --------------------------------------------------------------------------
analyzers = {}
for data_name, data in [
    ('Complete', data_complete),
    ('Monday', data_mon),
    ('Tuesday', data_tues),
    ('Wednesday', data_wed),
    ('Thursday', data_thur),
    ('Friday', data_fri),
    ('Saturday', data_sat),
    ('Sunday', data_sun)
]:
    analyzer = LotteryAnalyzer(data, data_name)
    analyzer.best_assign_HC()
    analyzer.calculate_transition_probs()
    analyzers[data_name] = analyzer

print("Best Transition Gameplay Numbers (20 Rounds)")
results = []
num_rounds = 20  # Number of rounds to generate

for name, analyzer in analyzers.items():
    gameplay_sets = analyzer.generate_multiple_gameplay_numbers(rounds=num_rounds)
    print(f"\n{name}:")
    for i, numbers in enumerate(gameplay_sets, 1):
        clean_numbers = [int(x) for x in numbers]
        print(f"  Round {i}: {clean_numbers}")
        # Each number in its own column (no brackets)
        results.append([i, name] + clean_numbers)

# Save to CSV
os.makedirs('Testing_Num', exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M')
filename = f'Testing_Num/best_c4l_num_{timestamp}.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Round', 'Dataset', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'CB'])  # Header
    writer.writerows(results)

print(f"\nSaved {num_rounds} rounds of predictions to {filename}")


#------------------------------------------#
#--- Worst Transition Number Generation ---#
#------------------------------------------#

class LotteryAnalyzer:
    def __init__(self, data_complete, name):
        self.data_complete = data_complete
        self.name = name
        self.data_complete_hot_cold = None
        self.transition_probs = {}
        self.hot_cold_probs = {}
        self.number_columns = ['1st', '2nd', '3rd', '4th', '5th', 'CB']
        self.valid_ranges = {
            "1st": (1, 56),
            "2nd": (2, 57),
            "3rd": (3, 58),
            "4th": (4, 59),
            "5th": (5, 60),
            "CB": (1, 4)
        }  

    def worst_assign_HC(self):
        self.data_complete_hot_cold = self.data_complete.copy()
        for col in self.number_columns:
            self.data_complete_hot_cold[f'{col}_H/C'] = self._worst_assign_HC_column(self.data_complete_hot_cold[col])

    def _worst_assign_HC_column(self, series):
        counts = series.value_counts()
        percentiles = counts.rank(pct=True)
        return series.map(lambda x: 'Hot' if percentiles[x] >= 0.80 else ('Cold' if percentiles[x] <= 0.35 else 'Mid'))

    def calculate_transition_probs(self):
        for column in self.number_columns:
            self.transition_probs[column] = self._calculate_transition_prob(self.data_complete_hot_cold, column)
            self.hot_cold_probs[column] = self._calculate_transition_prob(self.data_complete_hot_cold, f'{column}_H/C')

    def _calculate_transition_prob(self, data_complete, column):
        transitions = data_complete[column].shift().groupby(data_complete[column]).value_counts(normalize=True).unstack()
        return transitions.fillna(0)

    def generate_gameplay_numbers(self):
        gameplay_numbers = []
        previous_number = None
        for column in self.number_columns[:-1]:  # Exclude CB
            worst_transition = self._get_worst_transition(self.hot_cold_probs[column], previous_number)
            selected_number = self._select_number(column, worst_transition, gameplay_numbers)
            gameplay_numbers.append(selected_number)
            previous_number = worst_transition
        
        cash_ball = self._select_cash_ball()
        gameplay_numbers.append(cash_ball)
        return gameplay_numbers

    def generate_multiple_gameplay_numbers(self, rounds=20):
        """Generate multiple rounds of gameplay numbers."""
        return [self.generate_gameplay_numbers() for _ in range(rounds)]

    def _get_worst_transition(self, transition_matrix, previous_number=None):
        if isinstance(transition_matrix, pd.Series):
            return transition_matrix.idxmax()
        elif previous_number is None:
            return transition_matrix.mean().idxmax()
        else:
            return transition_matrix.loc[previous_number].idxmax()

    def _select_number(self, column, worst_transition, gameplay_numbers):
        available_numbers = self.data_complete_hot_cold[
            (self.data_complete_hot_cold[f'{column}_H/C'] == worst_transition) & 
            (self.data_complete_hot_cold[column] >= self.valid_ranges[column][0]) & 
            (self.data_complete_hot_cold[column] <= self.valid_ranges[column][1])
        ][column].unique()

        if len(available_numbers) == 0:
            available_numbers = list(range(self.valid_ranges[column][0], self.valid_ranges[column][1] + 1))

        valid_numbers = [n for n in available_numbers if n > (gameplay_numbers[-1] if gameplay_numbers else 0)]
        return int(random.choice(valid_numbers if valid_numbers else available_numbers))  # Ensure int

    def _select_cash_ball(self):
        cash_ball_transition = self._get_worst_transition(self.hot_cold_probs['CB'])
        cash_ball_numbers = self.data_complete_hot_cold[
            (self.data_complete_hot_cold['CB_H/C'] == cash_ball_transition) & 
            (self.data_complete_hot_cold['CB'] >= self.valid_ranges['CB'][0]) & 
            (self.data_complete_hot_cold['CB'] <= self.valid_ranges['CB'][1])
        ]['CB'].unique()

        if len(cash_ball_numbers) == 0:
            cash_ball_numbers = list(range(self.valid_ranges['CB'][0], self.valid_ranges['CB'][1] + 1))

        return int(random.choice(cash_ball_numbers))  # Ensure int

# --------------------------------------------------------------------------
# Main Processing
# --------------------------------------------------------------------------
analyzers = {}
for data_name, data in [
    ('Complete', data_complete),
    ('Monday', data_mon),
    ('Tuesday', data_tues),
    ('Wednesday', data_wed),
    ('Thursday', data_thur),
    ('Friday', data_fri),
    ('Saturday', data_sat),
    ('Sunday', data_sun)
]:
    analyzer = LotteryAnalyzer(data, data_name)
    analyzer.worst_assign_HC()
    analyzer.calculate_transition_probs()
    analyzers[data_name] = analyzer

print("Worst Transition Gameplay Numbers (20 Rounds)")
results = []
num_rounds = 20  # Number of rounds to generate

for name, analyzer in analyzers.items():
    gameplay_sets = analyzer.generate_multiple_gameplay_numbers(rounds=num_rounds)
    print(f"\n{name}:")
    for i, numbers in enumerate(gameplay_sets, 1):
        clean_numbers = [int(x) for x in numbers]
        print(f"  Round {i}: {clean_numbers}")
        # Each number in its own column (no brackets)
        results.append([i, name] + clean_numbers)

# Save to CSV
os.makedirs('Testing_Num', exist_ok=True)
timestamp = datetime.now().strftime('%Y%m%d_%H%M')
filename = f'Testing_Num/worst_c4l_num_{timestamp}.csv'

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Round', 'Dataset', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'CB'])  # Header
    writer.writerows(results)

print(f"\nSaved {num_rounds} rounds of predictions to {filename}")




