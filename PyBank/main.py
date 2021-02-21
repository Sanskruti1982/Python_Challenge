import os
import csv

#Path to collect data from PyBank folder
csvpath = os.path.join("budget_data.csv")


total = []
profitloss = []
month = []
change = [0]

#Read in the CSV file
with open(csvpath,'r') as csvfile:
    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip headerrow
    header = next(csvreader)
    
    #Loop the data and adding the total of profit and loss in total variable
    total = 0
    
    for row in csvreader:
        total = total + int(row[1])
        profitloss.append(int(row[1]))
        month.append(str(row[0]))
        length = len(profitloss)
        
    #Looping through rows to find the difference between the two rows
    for x, y, in zip(profitloss[0::], profitloss[1::]):
        change.append(y-x)
    #Creating dictionary to print the month and change together
    dictionary = dict(zip(month, change))
    
    
    #Creating a function to average the change
    def average(numbers):
        length = len(numbers)
        total1 = 0.0
        for number in numbers:
            total1 += number
        return total1 / (length -1)
        
#Creating a text file to print the final output result
output_file = os.path.join("final.txt")

with open(output_file, "w") as datafile:
   
    print("Financial Analysis", file=datafile)
    print("----------------------------", file=datafile)
    print("Total months: " + str(length), file=datafile)
    print("Total: " + "$" + str(total), file=datafile)
    print("Average Change: " + "$" + str(round(average(change),2)), file=datafile)
    print("Greatest Increase in Profits: " +  str(max(dictionary.items(), key=lambda k: k[1])), file=datafile)
    print("Greatest Decrease in Profits: " + str(min(dictionary.items(), key=lambda k: k[1])), file=datafile)

#Printing the analysis on to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total months: " + str(length))
print("Total: " + "$" + str(total))
print("Average Change: " + "$" + str(round(average(change),2)))
print("Greatest Increase in Profits: " +  str(max(dictionary.items(), key=lambda k: k[1])))
print("Greatest Decrease in Profits: " + str(min(dictionary.items(), key=lambda k: k[1])))
