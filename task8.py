candidates = [
    {"name": "Asha", "marks": 85, "assessment": 90, "attendance": 92},
    {"name": "Ravi", "marks": 78, "assessment": 88, "attendance": 95},
    {"name": "Mina", "marks": 92, "assessment": 80, "attendance": 89},
]

# Minimum requirements
minimum_marks = 60
minimum_assessment = 50
minimum_attendance = 75

qualified = []

for candidate in candidates:
    if (candidate["marks"] >= minimum_marks
            and candidate["assessment"] >= minimum_assessment
            and candidate["attendance"] >= minimum_attendance):

        # Simple total score used for ranking
        candidate["score"] = (
            candidate["marks"]
            + candidate["assessment"]
            + candidate["attendance"]
        )
        qualified.append(candidate)

# Rank by total score. If tied, prefer higher marks,
# then higher assessment score, then name alphabetically.
qualified.sort(
    key=lambda c: (
        -c["score"],
        -c["marks"],
        -c["assessment"],
        c["name"]
    )
)

print("Qualified candidates ranked:")
for rank, candidate in enumerate(qualified, start=1):
    print(rank, candidate["name"], "- Score:", candidate["score"])