# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# Declare empty dictionary 
candidate_votes = {}

# Winnding Candidte and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data: 

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
   
    # print each row in the csv file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes +=1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list
        # candidate_options.append(candidate_name)

        # If the candidate does not math any existing candidate...
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal. 
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    #candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print(candidate_results)
    print(election_results, end = "")
    # Save the final vote count to the text file    
    txt_file.write(election_results)
     
        #Determin the percentage of votes for each candidate by looping through the counts
        # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the % of vote
        vote_percentage = float(votes) /float(total_votes)*100
         # Print the candidate name and percentage of voates
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #candidate_votes[candidate_name] +=1

        # Determin winning vote count and candidate
        # Determin if the votes are greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"--------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

# 3. Print the candidate list
# print(candidate_votes)

#Create a filename variable to a direct or indirect path to the file. 
# file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as text_file:
    # Write some data to the file 
    # text_file.write("Arapahoe, ")
    # text_file.write("Denver, ")
    # text_file.write("Jefferson")
    #text_file.write("Arapahoe\nDenver\nJefferson")
# Write some data to the file. 
# outfile.write("Hello World")

#Close the file
# outfile.close()


# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidtes who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote