# PYPOLL


# Imported modules
import os # Module used to find files in other folders
import csv # Module used for reading CSV files

# Relative file path to the budget data csv
csvElectionPath = os.path.join('Resources', 'election_data.csv')

# Create text file path for holding the financial analysis
pyPollResultsPath = os.path.join('analysis', 'election_results.txt')

# Initialization of variables for total vote count
totalVotes = 0 # Stores total number of votes
candidates = [] # List of candidates
candidateVotes = {} # Dictionary of votes each candidate receives

# Loop for total vote count
with open(csvElectionPath) as csvElection:
    electionReader = csv.reader(csvElection) # Create the CSV reader
    header =next(electionReader) # Skip the header line in the CSV
    for row in electionReader:
        totalVotes += 1 # For each row, increment the vote counter
        if row[2] not in candidates: # If the candidate is not on the list, add the candidate to the list
            candidates.append(row[2])
            candidateVotes[row[2]] = 1 # Add the first vote for the candidate to the dictionary
        else:
            candidateVotes[row[2]] += 1 # Otherwise, add a vote to the candidate's count

# Initialization of a variable for vote percentages
voterOutput = "" # String for the output for each candidate
winningCount = 0 # Variable for the winning tally
winningCandidate = "" # String for the winning candidate

# Loop for vote percentages
for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100
    voterOutput += f"{candidate}: {votePct:.3f}% ({votes})\n"
    if votes > winningCount:  # Compare votes to the winning count
        winningCount = votes # Update the winning count
        winningCandidate = candidate # Update the winning candidate to the current candidate in the loop

# Output statements
electionResults = (
    f"\nPyPoll Election Results\n"
    f"------------------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"------------------------------\n"
    f"{voterOutput}"
    f"------------------------------\n"
    f"Winner: {winningCandidate}\n"
    )   

# Display the output to the terminal
print(electionResults)

# Export results to a text file
with open(pyPollResultsPath, "w") as txtElection:
    txtElection.write(electionResults)