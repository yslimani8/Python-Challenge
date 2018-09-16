import csv
import os

total_votes = 0
candidate_list = ""
votes = {}
percentage ={}
election_winner_votes = 0
election_winner = ""


filepath =  os.path.join("election_data.csv")
with open(filepath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_list = row[2]
        if candidate_list in votes:
            votes[candidate_list] = votes[candidate_list] + 1
        else:
            votes[candidate_list] = 1


for person, vote_count in votes.items():
    percentage[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > election_winner_votes:
        election_winner_votes = vote_count
        election_winner = person

dashbreak = "---------------------"


print("Election Results")
print(dashbreak)
print(f"Total Votes: {total_votes}")
print(dashbreak)
for person, vote_count in votes.items():
    print(f"{person}: {percentage[person]} ({vote_count})")
print(dashbreak)
print(f"election_winner: {election_winner}")
print(dashbreak)

with open("PyPollNote.txt","w") as txtfile:
   txtfile.write("Election Results" + "\n")
   
   txtfile.write("---------------------------" + "\n")
   txtfile.write(str(total_votes)  + "\n")
   txtfile.write("---------------------------" + "\n")

   for person, vote_count in votes.items():
       txtfile.write(str(person) + ": " + str( "{:2.3f}".format(vote_count/total_votes))  + "% (" + str(vote_count) + ")\n")

   txtfile.write("----------------------------" + "\n")
   txtfile.write(str(election_winner)  + "\n")
   txtfile.write("-----------------------------" + "\n")

   txtfile.close()
