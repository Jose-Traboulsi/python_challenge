# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..","python_challenge","PyBank","Resources","budget_data.csv")  # Input file path
file_to_output = os.path.join("..","python_challenge","PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
date_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = 1
    total_net = int(first_row[1])
    previous_net = int(first_row[1])
    

    # Process each row of data
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])
        current_net = int(row[1])
        date_list.append(row[0])
        
        # Track the net change         
        net_change_value = current_net - previous_net
        net_change_list.append(net_change_value)    
        previous_net = int(row[1]) #the current_net value becomes the previous_net for the next calculation

    # Calculate the greatest increase in profits (month and amount)
    max_value = max(net_change_list)
    max_index = net_change_list.index(max_value)
    
    # Calculate the greatest decrease in losses (month and amount)
    min_value = min(net_change_list)
    min_index = net_change_list.index(min_value)


# Calculate the average net change across the months
    def average_net_change(values):
        average = sum(values) / len(values)
        return average
    average_value = average_net_change(net_change_list)

# Generate the output summary
def output_summary():
    summary = (
        "Financial Analysis\n"
        "-------------------------------------\n"
        f"Total months: {total_months}\n"
        f"Total profits: ${total_net:,.2f}\n"
        f"Average net change: ${average_value:,.2f}\n"
        f"Greatest increase in profits: {date_list[max_index]}, ${max_value:,.2f}\n"
        f"Greatest decrease in profits: {date_list[min_index]}, ${min_value:,.2f}\n"
    )
    return summary

# Print the output
output_summary()

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(str(output_summary()))
