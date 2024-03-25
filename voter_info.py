#2.3
def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    if voter_id in voter_info:
        voter_info[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}
        print(f"Voter {voter_id} information updated.")
    else:
        voter_info[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}
        print(f"New voter {voter_id} information added.")


#2.6
voters = {
    1: {"name": "Mnced", "registered": True},
    2: {"name": "Jane", "registered": False},
    3: {"name": "Jack", "registered": True}
}

registered_voters = list(filter(lambda voter: voter[1]["registered"], voters.items()))
print(registered_voters)