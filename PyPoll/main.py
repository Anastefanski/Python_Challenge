import os
import csv
#Load file path
csvpath = os.path.join('Resources','election.csv')
#Placeholders for votes and candidates
total_votes = 0
vote_total = []
candidates_name = []
each_vote = []
percent_of_vote = []

#open file and read in results
with open(csvpath) as election_csv:
    csvreader = csv.reader(election_csv, delimiter=',')

    csv_header =next(csvreader)
#add vote count
    for row in csvreader: 
        total_votes += 1
#if candidates name not found skip if it is found add to vote count        
        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            index = candidates_name.index(row[2])
            each_vote.append(1)
        else:
            index = candidates_name.index(row[2])
            each_vote[index] = each_vote[index] + 1 
#calculate vote percentage and format    
    for votes in each_vote:
        percentage = (votes/total_votes)
        percentage = "{:.3%}".format(percentage)
        percent_of_vote.append(percentage)
        
candidate = max(each_vote)
index = each_vote.index(candidate)
winning_candidate = candidates_name[index]
#show candidates results in output
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
for i in range(len(candidates_name)):
    print(candidates_name[i] + ": " + (str(percent_of_vote[i])) + " (" + (str(each_vote[i])) + ")")
print("--------------------------")
print("Winner: " + winning_candidate)
print("--------------------------")
#output election results to csv
output_path = os.path.join("analysis", "election_results.txt")

with open (output_path,"w") as file:
    
    file.write ("Election Results")
    file.write ("\n")
    file.write ("----------------------------")
    file.write ("\n")
    file.write (f"Total Votes: " + str(total_votes))
    file.write ("\n")
    file.write ("--------------------------")
    file.write ("\n")
    for i in range(len(candidates_name)):
        line = ((candidates_name[i] + ": " + (str(percent_of_vote[i])) + " (" + (str(each_vote[i])) + ")"))
        file.write('{}\n'.format(line))
    file.write ("--------------------------")
    file.write ("\n")
    file.write (f"Winner: " + winning_candidate)
    file.write ("\n")
    file.write ("--------------------------")

    