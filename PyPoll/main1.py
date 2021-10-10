# Note to grader: I was really struggling with this section of the HW and was not able to correct error in time.
# If its possible can I redo the PyPoll of the assiagnment, I ran out of time on this section.  I was able to go to office hours and use tutoring for understanding PyBank.
# However, I wasn't able to understand PyPoll in time. 

import csv
with open ('Resources/election_data.csv') as open_csv:
    csv_reader = csv.reader(open_csv)

    votes = 0
    #Winner = 0
    candidate_name= []
    candidate_vote = []
    total_percentage = []  #candidate percentage
    top_value = []
    

    next (csv_reader)

    for row in csv_reader:
    
        #total votes in all 
        votes += 1 
        # list of candidates who recieved votes
        #if row[2] not in candidate_name:
           # candidate_vote.append(row[2])
            #candidate_vote.append(1)
        #else:
            #candidate_list = candidate_name.index(row[2])
            #candidate_vote[candidate_list] += 1
    
    
        
        #Winner = max(candidate_vote)



output = (f'''
Election Results
  -------------------------
  Total Votes: {votes}
  -------------------------
''')
print(output)