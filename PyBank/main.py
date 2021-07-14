import os
import csv
#Load file path
csvpath = os.path.join('resources','budget_data.csv')
#Placeholders for months and profits
monthly_total = []
profit = []
monthly_change = []
#Open file path
with open(csvpath, encoding="utf-8") as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=',')
#Skip header row
    csv_header =next(csvreader)
#iterate over profit to add values
    for row in csvreader: 

        monthly_total.append(row[0])
        profit.append(int(row[1]))

    for i in range(len(monthly_total)-1):
         
        monthly_change.append(profit[i+1]-profit[i])
#determine the maximum and minimum profit change        
max_profit_increase = max(monthly_change)
max_profit_decrease = min(monthly_change)

max_profit_month = monthly_change.index(max(monthly_change)) +1
min_profit_month = monthly_change.index(min(monthly_change)) +1
#show profit change in terminal output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(monthly_total)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {monthly_total[max_profit_month]} (${(str(max_profit_decrease))})")
print(f"Greatest Decrease in Profits: {monthly_total[max_profit_month]} (${(str(min_profit_month))})")
#output financial analysis to csv
output_path = os.path.join("analysis", "Budget_Analysis.txt")

with open (output_path, "w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(monthly_total)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {monthly_total[max_profit_month]} (${(str(max_profit_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {monthly_total[min_profit_month]} (${(str(max_profit_decrease))})")






 
