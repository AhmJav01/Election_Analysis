# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
#1. Decclare the mepty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

county_list = []
county_votes = {}
highest_county = ""
highestcounty_count = 0
highestcounty_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        county_name = row[1]
        
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    county_vote = (
        f"County Votes\n")

    print(county_vote, end="")
    txt_file.write(county_vote)

    for county_name in county_votes:
        countyvotes = county_votes[county_name]
        countyvote_percentage = float(countyvotes) / float(total_votes) * 100
        county_results = (f"{county_name}: {countyvote_percentage:.1f}% ({countyvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        
        if (countyvotes > highestcounty_count) and (countyvote_percentage > highestcounty_percentage):
            highestcounty_count = countyvotes
            highestcounty_percentage = countyvote_percentage
            highest_county = county_name

    county_candidate_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"-------------------------\n")
    print(county_candidate_summary)
    txt_file.write(county_candidate_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.    
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    