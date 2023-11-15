import os
import csv

from numpy import mean

#Lists to store data
date = []
profit_losses = []
greatest_decrease = ["", 0]
greatest_increase = ["", 0]
change_value_list = []

#set the required variables
previous_value = 0
change_in_value = 0

#Set variable and path for input file
budget_csv = r"PyBank\Resources\budget_data.csv"


#set variable and path for output file
bankanalysis_csv = r"PyBank\Analysis\bankanalysis.csv"


#Open the CSV using the UTF-8 encoding
with open(budget_csv, 'r', encoding = 'utf-8') as csvfile:
    
     #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #store the header row
    csv_header = next(csvreader)
    
    
    #print title 
    print("\n"+"Financial Analysis")
    print("----------------------------")
    
    
    # Read through each row of data after the header      
    for row in csvreader:
                          
        #Add Date
        date.append(row[0])
                 
        #Add Profit/Losses
        profit_losses.append(int(row[1]))
       
        #Calculate the average change in value between each consecutive months over the entire period
        change_in_value = float(row[1]) - previous_value    
        previous_value = float(row[1])
        change_value_list = change_value_list + [change_in_value]
        
        #check for the greatest increase in value (date and amount) over the entire period
        if change_in_value>greatest_increase[1]:
            greatest_increase[1]= int(change_in_value)
            greatest_increase[0] = row[0]
                    
        #check for the greatest decrease in value (date and amount) over the entire period
        if change_in_value<greatest_decrease[1]:
            greatest_decrease[1]= int(change_in_value)
            greatest_decrease[0] = row[0]
            
        
    #Calculate and print the total months                      
    month_count = len(date)
    print(f"Total Months: {month_count}"+"\n")
    
    #Calculate and print the total value of Profits/Losses 
    net_total = sum(profit_losses)
    print(f"Total: ${net_total}"+"\n")
    
    #Calculate and print the Average Change 
    change_value_list.pop(0)
    avg_change = round(mean(change_value_list),2)
    print(f"Average Change: ${avg_change}"+"\n")
   
    #print the greatest increse in profits 
    increase = print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " " + "($" + str(greatest_increase[1]) + ")" +"\n")
    
    #print the greatest decrese in profits
    decrease = print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " " + "($" + str(greatest_decrease[1]) + ")" +"\n")
    
              
#Open the output file
with open(bankanalysis_csv, "w", newline='') as bankanalysisfile:
    
    #Print output in the bankanalysis File
    bankanalysisfile.write("Financial Analysis\n")
    bankanalysisfile.write("----------------------------\n")
    bankanalysisfile.write("Total Months: " + str(month_count)+"\n")
    bankanalysisfile.write("Total: $" + str(net_total)+"\n")
    bankanalysisfile.write("Average Change: $" + str(avg_change)+"\n")
    bankanalysisfile.write("Greatest Increase in Profits: " + str(greatest_increase[0]) + " " + "($" + str(greatest_increase[1]) + ")" +"\n")
    bankanalysisfile.write("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " " + "($" + str(greatest_decrease[1]) + ")" +"\n")
