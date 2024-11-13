# -*- coding: UTF-8 -*-
#"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("..", "python_challenge","PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("..", "python_challenge","PyPoll","analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winner_count = 0
winner_name = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes+=1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f'{total_votes:,}')

    # Write the total vote count to the text file
    def election_totals():
        summary = (
           "Election Results\n"
            "-------------------------------------\n"
            f"Total Votes = {total_votes:,}\n"
            "-------------------------------------\n"
        )
        return summary
    txt_file.write(election_totals())
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        
        # Get the vote count and calculate the percentage
        candidate_tally = candidate_votes[candidate]
        percent_vote = (candidate_tally/total_votes) * 100
    
        # Update the winning candidate if this one has more votes
        if candidate_tally > winner_count:
            winner_count = candidate_tally
            winner_name = candidate
    
        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {candidate_tally:,} ({percent_vote:.3f}%)")

        def total_tally():
            tally_summary = (
                f"{candidate}: {candidate_tally:,} ({percent_vote:.3f}%)\n"
            )
            return tally_summary
        txt_file.write(total_tally())

    # Generate and print the winning candidate summary
    def win_summary():
        winning_summary = (
            "-------------------------------------\n"
            f"WINNER: {winner_name}!\n"
            f"Congratulations!\n"
        )
        return winning_summary

    # Save the winning candidate summary to the text file
    txt_file.write(win_summary())