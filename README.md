
# Election Analysis
## Overview of Project
A Colorado Board of Elections employee has requested the following tasks to complete the election audit of a local congressional election

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout.


### Purpose

To provide a solution to generate a vote count to certify the U.S. congressional race. Moreover, the solution may be be used in other districts and/or senatorial elections.

### Resources

 - Data Source: election_results.csv
 - Software: Python 3.9.6, Visual Studio Code, 1.58.2


## Election-Audit Results

The analysis of the election show that:

- There were __*369,711*__ votes cast in the election.
 
- The county votes distribution were:
	- __Jefferson__ with __*10.5%*__ of the vote and __*38,855*__ number of votes.
	- __Denver__ with __*82.8%*__  of the vote and __*306,055*__ number of votes.
	- __Arapahoe__ with  __*6.7%*__  of the vote and __*24,801*__ number of votes.

- The largest county turnout were: 
	- __Denver__, where __*306,055*__ of the votes came from, representing __*82,8%*__ of the total number of votes.

- The candidates were:
	- __Charles Casper Stockham__
	- __Diana DeGette__
	- __Raymon Anthony Doane__

- The candidates results were:
	- __Charles Casper Stockham__ received __*23.0%*__ of the vote and __*85,213*__ number of votes.
	- __Diana DeGette__ received __*73.8%*__ of the vote and __*272,892*__ number of votes.
	- __Raymon Anthony Doane__ received __*3.1%*__ of the vote and __*11,606*__ number of votes.

- The winner of the election was:
	- __Diana DeGette__, who receive __*73.8%*__ of the vote and __*272,892*__ number of votes.


## Summary

The code uses list and dictionary to be populated with all counties and candidates found in a provided dataset making it suitable to any election audition. However, two small changes are necessary to accommodate unpredictable specifications:

 1. __Change the path and CSV file name within the code below within__:
	 - Whatever is *after* comma may be the *CSV file name* to be informed within quotes. 
	 - Whatever is *before* comma may be the *path* to be informed within quotes. 
		 - It is important to know that Python always starts looking for a file in the same directory where the program is running. 

```Python 
   #Add a variable to load a file from a path.
   file_to_load = os.path.join( "Resources", "election_results.csv")
```

 2. __Adjust the number in the code below to indicate the column where candidates ```candidate_name = row[2] ``` and counties ```county_name = row[1] ``` will be found within the new CSV file__:
	 - This part of the code runs each raw in the informed column number to get the candidate name and county name. 
		 - However, it is important to know that the column number always start with zero meaning that the first column may be represented by the number 0, the second column may be represented by the number 1 and so forth.
```Python 
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
