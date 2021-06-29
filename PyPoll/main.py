import os
import csv

csvpath = os.path.join('resources','election_data.csv')

total_votes = 0
vote_total = []
candidates_name = []
each_vote = []
percent_of_vote = []


with open(csvpath) as election_csv:
    csvreader = csv.reader(election_csv, delimiter=',')

    csv_header =next(csvreader)

    for row in csvreader: 
        total_votes += 1
        
        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            index = candidates_name.index(row[2])
            each_vote.append(1)
        else:
            index = candidates_name.index(row[2])
            each_vote[index] = each_vote[index] + 1 
    
    for votes in each_vote:
        percentage = (votes/total_votes)
        percentage = "{:.3%}".format(percentage)
        percent_of_vote.append(percentage)
        
candidate = max(each_vote)
index = each_vote.index(candidate)
winning_candidate = candidates_name[index]

print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
for i in range(len(candidates_name)):
    print(candidates_name[i] + ": " + (str(percent_of_vote[i])) + " (" + (str(each_vote[i])) + ")")
print("--------------------------")
print("Winner: " + winning_candidate)
print("--------------------------")

output_path = os.path.join("analysis", "election_results.txt")

with open (output_path,"w") as file:
    
    file.write ("Election Results")
    file.write ("\n")
    file.write ("----------------------------")
    file.write ("\n")
    file.write (f"Total Votes: " + str(total_votes))
    file.write ("\n")
    file.write ("--------------------------")
    for i in range(len(candidates_name)):
        line = ((candidates_name[i] + ": " + (str(percent_of_vote[i])) + " (" + (str(each_vote[i])) + ")"))
        file.write('{}\n'.format(line))
    file.write ("--------------------------")
    file.write ("\n")
    file.write (f"Winner: " + winning_candidate)
    file.write ("\n")
    file.write ("--------------------------")

    

