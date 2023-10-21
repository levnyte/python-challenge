# PYBANK


# Imported modules
import os # Module used to find files in other folders
import csv # Module used for reading CSV files

# Relative file path to the budget data csv
csvBudgetPath = os.path.join('Resources', 'budget_data.csv')

# Create text file path for holding the financial analysis
pyBankAnalysisPath = os.path.join('analysis', 'budget_analysis.txt')

# Initializations of variables for totals and average monthly change 
totalMonths = 0 # Count of months
totalRevenue = 0 # Total revenue of the given period
previousPL = 0.0 # Initial previous revenue
monthlyChanges = [] # List of  P/L change from month to month 
dates = [] # List of dates

# Loop for totals and average monthly changes
with open(csvBudgetPath) as csvBudget:
    budgetReader = csv.reader(csvBudget, delimiter = ',') #Separates dates from profits/losses
    header = next(budgetReader) # Skip the header line in the CSV
    for row in budgetReader: 
        totalMonths += 1 # For each row, increment the month counter
        totalRevenue += float(row[1]) # Add up the revenue in index 1 of each row
        netChange = float(row[1]) - previousPL # Revenue change from month to month
        monthlyChanges.append(netChange) # Add to the list of montly changes
        dates.append(row[0]) # Add to the list of dates
        previousPL = float(row[1]) # Update the previous revenue
    del monthlyChanges[0] # Delete the first monthly change because it is only the first monthly revenue
    averageMonthlyChange = sum(monthlyChanges) / len(monthlyChanges) # Average change per month  

# Initialization of Greatest increase and decrease variables
greatestIncrease = [dates[0], monthlyChanges[0]] # Holds the date and value of the greatest increase
greatestDecrease = [dates[0], monthlyChanges[0]] # Holds the date and value of the greatest decrease

# Loop to calculate the greatest monthly increase and decrease
for m in range(len(monthlyChanges)):
    if(monthlyChanges[m] > greatestIncrease[1]): # If the value is greater than the greatest increase, 
        greatestIncrease[1] = monthlyChanges[m]     # it becomes the new greatest increase
        greatestIncrease[0] = dates[m] # Update the date of the greatest increase
    
    if(monthlyChanges[m] < greatestDecrease[1]): # If the value is less than the greatest decrease, 
        greatestDecrease[1] = monthlyChanges[m]     # it becomes the new greatest decrease
        greatestDecrease[0] = dates[m] # Update the date of the greatest decrease

# Output statements
financialAnalysis = (
    f"\nPyBank Financial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total Revenue: ${totalRevenue:,.2f}\n"
    f"Average Monthly Change: ${averageMonthlyChange:,.2f}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:,.2f})\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:,.2f})\n"
    )   

# Display the output to the terminal
print(financialAnalysis)

# Export analysis to a text file
with open(pyBankAnalysisPath, "w") as txtBudget:
    txtBudget.write(financialAnalysis)