import os
import csv

#Path to collect data from PyBank folder
csvpath = os.path.join("budget_data.csv")

#Lists to store month data
month = [0]


#Read in the CSV file
with open(csvpath,'r') as csvfile:
    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip headerrow
    header = next(csvreader)
    #Determine first row for profit/loss value
    firstrow = next(csvreader)
   
    
    #Adding the variables to for change and greatest increase and decrease
    totalchange = 0
    changesum = 0
    maxinc = 0
    maxincmonth = 0
    mininc = 0
    minincmonth = 0
    #Defining the first row as a variable and total also as first row
    previousvalue = int(firstrow[1])
    total = previousvalue
    
   #Looping through the data to get values
    for row in csvreader:
        total = total + int(row[1])
        nextvalue = int(row[1])
        month.append(str(row[0]))
        length = len(month)
        #Defining change as O so that measures the difference between two rows rather than storing the value
        change = 0
        change = nextvalue - int(previousvalue)
        totalchange = totalchange + change
        #Defining previous value as the next row so that the next row is always the one row down in the matrix
        previousvalue = int(row[1])
        
        #Defining maximum and minimum increase
        #Getting the maximum of the change and getting the corresponding to motnh
        if change > maxinc:
            maxinc = change
            maxincmonth = row[0]
        #Getting the minimum of the change and getting the corresponding to motnh
        if change < mininc:
            mininc = change
            minincmonth = row[0]
        
    #Averaging the change over the period
    #Taking one away from the length as the first change is zero and this length accounts for the count of months
    avgchange = totalchange/(length-1)
  
#Creating a text file to print the final output result
output_file = os.path.join("final.txt")

with open(output_file, "w") as datafile:
    print("Financial Analysis", file=datafile)
    print("----------------------------", file=datafile)
    print("Total months: " + str(length), file=datafile)
    print("Total: " + "$" + str(total), file=datafile)
    print("Average Change: " + "$" + str(round(avgchange,2)))
    print("Greatest Increase in Profits: " +  str(maxincmonth) + " (" + "$" + str(maxinc) + ")", file=datafile)
    print("Greatest Decrease in Profits: " +  str(minincmonth) + " (" + "$" + str(mininc) + ")", file=datafile)

#Printing the analysis on to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(length))
print("Total: " + "$" + str(total))
print("Average Change: " + "$" + str(round(avgchange,2)))
print("Greatest Increase in Profits: " +  str(maxincmonth) + " (" + "$" + str(maxinc) + ")")
print("Greatest Decrease in Profits: " +  str(minincmonth) + " (" + "$" + str(mininc) + ")")

