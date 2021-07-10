# Now that you have seen the dataset, you're going to sit down with Tom
# to go over the tasks that need to be completed for the election audit,
# and discuss the information needed by the Colorado Board of Elections.

#  In this project, our final Python script will need to be able to deliver
#  the following information when the script is run: 
    # # # Total number of votes cast
    # # # A complete list of candidates who received votes
    # # # Total number of votes each candidate received
    # # # Percentage of votes each candidate won
    # # # The winner of the election based on popular vote

# ---- pseudocode ----
        # 1 - Open the data file.
        # 2 - Write down the names of all the candidates.
        # 3 - Add a vote count for each candidate.
        # 4 - Get the total votes for each candidate.
        # 5 - Get the total votes cast for the election.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)