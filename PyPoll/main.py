import os
import csv

#Path to collect data from PyPoll folder
electioncsv = os.path.join('election_data.csv')

#Lists to store data
total = []
voterid = []
county = []
candidate = []

#Read in the CSV file
with open(electioncsv,'r') as csvfile:
    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip headerrow
    header = next(csvreader)
    
    #Loop through the data to get count of each candidate and percentage of votes and winner of the most popular votes
    total = 0
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    winner = 0
    for row in csvreader:
        voterid.append(int(row[0]))
        length = len(voterid)
        candidate.append(str(row[2]))
        if row[2] == "Khan":
            count = count + 1
        if row[2] == "Correy":
            count1 = count1 + 1
        if row[2] == "Li":
            count2 = count2 + 1
        if row[2] == "O'Tooley":
            count3 = count3 + 1
    percent = count/length * 100
    percent1 = count1/length * 100
    percent2 = count2/length * 100
    percent3 = count3/length * 100
    winner = max(set(candidate), key = candidate.count)

#Printing the analysis on to the terminal
print("Election Results")
print("---------------------------")
print("Total Votes: " + str(length))
print("---------------------------")
print("Khan: " + str(round(percent,4)) + "%  " + "(" + str(count) + ")")
print("Correy: " + str(round(percent1,4)) + "%  " + "(" + str(count1) + ")")
print("Li: " + str(round(percent2,4)) + "%  " + "(" + str(count2) + ")")
print("O'Tooley: " + str(round(percent3,4)) + "%  " + "(" + str(count3) + ")")
print("---------------------------")
print("Winner: " + winner)
print("---------------------------")

#Creating a text file to print the final output result
output_file = os.path.join("final.txt")

with open(output_file, "w") as datafile:
    print("Election Results", file=datafile)
    print("---------------------------", file=datafile)
    print("Total Votes: " + str(length), file=datafile)
    print("---------------------------", file=datafile)
    print("Khan: " + str(round(percent,4)) + "%  " + "(" + str(count) + ")", file=datafile)
    print("Correy: " + str(round(percent1,4)) + "%  " + "(" + str(count1) + ")", file=datafile)
    print("Li: " + str(round(percent2,4)) + "%  " + "(" + str(count2) + ")", file=datafile)
    print("O'Tooley: " + str(round(percent3,4)) + "%  " + "(" + str(count3) + ")", file=datafile)
    print("---------------------------", file=datafile)
    print("Winner: " + winner, file=datafile)
    print("---------------------------", file=datafile)
