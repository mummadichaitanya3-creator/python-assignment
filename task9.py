# Each event is a tuple: (event name, time, team)
events = [
    ("Football", "10:00", "Tigers"),
    ("Basketball", "10:00", "Eagles"),
    ("Volleyball", "11:00", "Tigers"),
    ("Football", "11:00", "Eagles"),
]

# Each score is a tuple: (team, points)
scores = [
    ("Tigers", 3),
    ("Eagles", 2),
    ("Tigers", 1),
    ("Eagles", 3),
]

# Check for scheduling conflicts
print("Scheduling conflicts:")
conflict_found = False

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        if events[i][1] == events[j][1] and events[i][2] == events[j][2]:
            print(events[i][2], "has two events at", events[i][1])
            conflict_found = True

if not conflict_found:
    print("No conflicts found.")

# Add up each team's points
team_points = {}

for team, points in scores:
    if team not in team_points:
        team_points[team] = 0
    team_points[team] += points

# Sort teams by points and show final rankings
rankings = sorted(team_points.items(), key=lambda item: item[1], reverse=True)

print("\nFinal rankings:")
for rank, (team, points) in enumerate(rankings, start=1):
    print(rank, team, "-", points, "points")