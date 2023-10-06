# BUDGET DATA

import os # Module used to find files in other folders
import csv # Module used for reading CSV files

# Title
print(f"PyBank Budget Data\n")
# Relative file path to the budget data csv
csvBudgetPath = os.path.join('Resources', 'budget_data.csv')

totalMonths = 0 # Initialize count of months
totalPL = 0 # Initialize total profit/loss of the entire period

with open(csvBudgetPath) as csvBudget:
    budgetReader = csv.reader(csvBudget, delimiter = ',') #Separates dates from profits/losses
    firstLine = next(budgetReader) # Skip the first line in the CSV
    for row in budgetReader: # For each row, increment the month counter
        totalMonths += 1
    print(f"Total Months: {totalMonths}\n") # Display the final number of months

with open(csvBudgetPath) as csvBudget:
    budgetReader = csv.reader(csvBudget, delimiter = ',') #Separates dates from profits/losses
    firstLine = next(budgetReader) # Skip the first line in the CSV 
    for row in budgetReader: # Add the profits and losses of each row
        totalPL += int(row[1])
    print(f"Total Profit: {totalPL}\n") # Display the net profit

    