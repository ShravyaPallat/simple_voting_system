# Input for nominees
nominees = []
nominee_count = int(input("Enter the number of nominees: "))
for i in range(nominee_count):
    nominee_name = input(f"Enter the name of nominee {i + 1}: ")
    nominees.append(nominee_name)

# Initialize vote counts for nominees
votes = {nominee: 0 for nominee in nominees}

# Voter ID list
voter_id = list(range(1, int(input("Enter the number of voters: ")) + 1))

# Start voting
while voter_id:
    print("\nAvailable Voter IDs:", voter_id)
    voter = int(input("Enter your voter ID: "))
    
    if voter in voter_id:
        voter_id.remove(voter)
        print("\nNominees:")
        for idx, nominee in enumerate(nominees, 1):
            print(f"{idx}. {nominee}")
        
        vote = int(input("Enter the number corresponding to your vote: "))
        
        if 1 <= vote <= len(nominees):
            votes[nominees[vote - 1]] += 1
            print(f"You have voted for {nominees[vote - 1]}")
        else:
            print("Invalid vote. Please try again.")
    else:
        print("You are not a voter or you have already voted.")

# Voting session results
if not voter_id:
    print("\nVoting session is over!")
    total_votes = sum(votes.values())
    winner = max(votes, key=votes.get)
    max_votes = votes[winner]

    # Check if there's a tie
    if list(votes.values()).count(max_votes) > 1:
        print("It's a tie between the following nominees:")
        for nominee, count in votes.items():
            if count == max_votes:
                print(f"{nominee} with {count} votes")
    else:
        percent = (max_votes / total_votes) * 100
        print(f"{winner} has won the election with {percent:.2f}% of votes.")
