#2.1
print("Register to vote, your vote is your power to make a change")

def register_party(parties):
    for party in parties:
        party_name = party.get("party_name")
        member_count = party.get("member_count")
        if member_count >= 1000:
            print(f"The party '{party_name}' is eligible for registration with {member_count} members.")
        else:
            print(f"The party '{party_name}' does not meet the minimum membership requirement for registration.")

register_party(parties)