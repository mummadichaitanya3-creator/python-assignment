# Hackathon Team Formation and Ranking

MIN_TEAM_SIZE = 2
MAX_TEAM_SIZE = 4

teams = {
    "Team A": {
        "members": ["Arun", "Bala", "Charan"],
        "round_scores": [80, 90, 85]
    },
    "Team B": {
        "members": ["Deepak", "Esha"],
        "round_scores": [85, 85, 85]
    },
    "Team C": {
        "members": ["Farhan", "Gita", "Hari", "Isha", "John"],
        "round_scores": [90, 80, 95]
    },
    "Team D": {
        "members": ["Kiran", "Latha", "Manu"],
        "round_scores": [80, 90, 85]
    }
}

valid_teams = []

# Validate team composition and scores
for team_name, details in teams.items():
    members = details["members"]
    scores = details["round_scores"]

    if not MIN_TEAM_SIZE <= len(members) <= MAX_TEAM_SIZE:
        print(f"{team_name}: Invalid team size ({len(members)} members)")
        continue

    if not scores or any(
        not isinstance(score, (int, float))
        or isinstance(score, bool)
        or score < 0
        for score in scores
    ):
        print(f"{team_name}: Invalid scores")
        continue

    total_score = sum(scores)

    valid_teams.append({
        "name": team_name,
        "members": members,
        "round_scores": scores,
        "total_score": total_score
    })

# Rank teams using predefined tie-breaking rules
valid_teams.sort(
    key=lambda team: (
        team["total_score"],
        team["round_scores"][-1],
        team["round_scores"][0]
    ),
    reverse=True
)

# Display results
print("\n===== HACKATHON TEAM RANKINGS =====")

for rank, team in enumerate(valid_teams, start=1):
    print(f"\nRank: {rank}")
    print(f"Team: {team['name']}")
    print(f"Members: {', '.join(team['members'])}")
    print(f"Round Scores: {team['round_scores']}")
    print(f"Total Score: {team['total_score']}")

print("\n===== SUMMARY =====")
print("Total teams:", len(teams))
print("Valid teams:", len(valid_teams))
print("Invalid teams:", len(teams) - len(valid_teams))

if valid_teams:
    print("Winner:", valid_teams[0]["name"])
    print("Winning Score:", valid_teams[0]["total_score"])