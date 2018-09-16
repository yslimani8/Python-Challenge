import csv
import os

month_number = 0
total_revenue = 0
present_month_revenue = 0
past_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

filepath = os.path.join("budget_data.csv")

with open(filepath,'r', newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")

  header=next(csvreader)

  for row in csvreader:
     month_number = month_number + 1
     months.append(row[0])
     present_month_revenue = int(row[1])
     total_revenue = total_revenue + present_month_revenue

     if month_number > 1:
         revenue_change = present_month_revenue - past_month_revenue
         revenue_changes.append(revenue_change)

     past_month_revenue = present_month_revenue


sumofrevenue_changes = sum(revenue_changes)
averagechange = sumofrevenue_changes / (month_number - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_number}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${averagechange}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

with open("PyBanknote.txt","w") as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("------------------- \n")
    txtfile.write("Total Months: " + str(month_number) + "\n")
    txtfile.write("Total Revenue: $" + str(total_revenue) + "\n")
    txtfile.write("Average Revenue Change: $" + str(averagechange) + "\n")
    txtfile.write("Greatest Decrease in Revenue: " + min_month + " ($" + str(min_change) + ")" + "\n")