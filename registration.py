print("Register to vote, your vote is your power to make a change")

def register_party(parties):
    for party in parties:
        party_name = party.get("party_name")
        member_count = party.get("member_count")
        if member_count >= 1000:
            print(f"The party '{party_name}' is eligible for registration with {member_count} members.")
        else:
            print(f"The party '{party_name}' does not meet the minimum membership requirement for registration.")


parties = [
    {"party_name": "ANC", "reg_number": 1, "member_count": 1500},
    {"party_name": "EFF", "reg_number": 2, "member_count": 800},
    {"party_name": "IFP", "reg_number": 3, "member_count": 1200}
]

register_party(parties)

last_registered_party_number = 13318

new_party_registration_number = last_registered_party_number + 1
new_party = {"party_name": "MK", "reg_number": new_party_registration_number, "member_count": 5300}

register_party([new_party])