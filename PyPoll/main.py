import os
import csv

electioncsv = os.path.join('election_data.csv')

total = []
voterid = []
county = []
candidate = []

with open(electioncsv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
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
