import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data: 

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # print each row in the csv file
    #for row in file_reader:
     #   print(row)



# Close the file
# election_data.close( ) 

#Create a filename variable to a direct or indirect path to the file. 
# file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as text_file:
    # Write some data to the file 
    # text_file.write("Arapahoe, ")
    # text_file.write("Denver, ")
    # text_file.write("Jefferson")
    text_file.write("Arapahoe\nDenver\nJefferson")
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