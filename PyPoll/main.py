import os
import csv

#Lists to store data
candidate_name = []
candidate_votes = {}

#set the required variables
votes_count = 0
winner_count = 0
winner_cand = ""


#Set variable and path for input file
election_csv = r"PyPoll\Resources\election_data.csv"

#set variable and path for output file
pollanalysis_csv = r"PyPoll\Analysis\pollanalysis.csv"


# Open the CSV using the UTF-8 encoding
with open(election_csv, 'r', encoding = 'utf-8') as csvfile:
    
    #Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter = ",")
    
    #store the header row
    csv_header = csvreader
    
    
    #print title
    print("\n"+"Election Results"+"\n")
    print("----------------------------")
    
    # Read through each row of data after the header                
    for row in csvreader: 
         
        #Calculate the total vote count            
        votes_count += 1
    
        #assign a variable to store the candidate names  
        candidate = row["Candidate"]
        #Run an if statement to find names of all the canadidates and add it to the list candidate_name
        if row["Candidate"] not in candidate_name:
            candidate_name.append(row["Candidate"])
            candidate_votes[candidate] = 0
        
        #Add the votes for each of the candidates 
        candidate_votes[candidate] = candidate_votes[candidate] + 1
                      
    
    #print the total vote count
    print(f"\n Total Votes: {votes_count}\n")
    print("----------------------------\n")
    
    
#Open the output file
with open(pollanalysis_csv, "w", newline='') as pollanalysisfile:
    
    #Print output in pollanalysis File
    pollanalysisfile.write("Election Results\n")
    pollanalysisfile.write("----------------------------\n")
    pollanalysisfile.write("Total Votes:  " + str(votes_count)+"\n")
    pollanalysisfile.write("----------------------------\n")
    
    
    #Run a for loop to calculate the percent of votes for each of the candidate names based on their votes
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percent = float(votes)/float(votes_count)*100
        
        #create a variable to hold the cnadidate name, percent of their votes, and the number of votes
        candidate_list = (f"{candidate}: {vote_percent:.3f}% ({votes})\n")
        
        #print the above result on the terminal and pollanalysis file
        print(f"{candidate_list}")
        pollanalysisfile.write(f"{candidate_list}")
        
        
        #find the winner using an if statement 
        if (votes > winner_count):
            winner_count = votes
            winner_cand = candidate
        
    #print the winner on to the terminal and the pollanalysis file
    print("----------------------------\n")
    print(f"Winner: {winner_cand} \n")
    print("----------------------------")
    
    pollanalysisfile.write("----------------------------\n")
    pollanalysisfile.write(f"Winner: {winner_cand} \n")
    pollanalysisfile.write("----------------------------")
    
