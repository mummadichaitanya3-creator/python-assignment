students = [
    {
        "name": "Anu",
        "subjects": {
            "Math": {"mark": 65, "attendance": 80, "prerequisite_done": True},
            "Physics": {"mark": 42, "attendance": 75, "prerequisite_done": True},
        },
    },
    {
        "name": "Ravi",
        "subjects": {
            "Math": {"mark": 35, "attendance": 60, "prerequisite_done": False},
            "Physics": {"mark": 70, "attendance": 90, "prerequisite_done": True},
        },
    },
]

pass_mark = 40
minimum_attendance = 75

for student in students:
    outstanding = []

    for subject, details in student["subjects"].items():
        if details["mark"] < pass_mark:
            outstanding.append(subject + ": marks below pass mark")

        if details["attendance"] < minimum_attendance:
            outstanding.append(subject + ": attendance too low")

        if not details["prerequisite_done"]:
            outstanding.append(subject + ": prerequisite not completed")

    print("\nStudent:", student["name"])

    if outstanding:
        print("Progression: Not eligible")
        print("Outstanding requirements:")
        for item in outstanding:
            print("-", item)
    else:
        print("Progression: Eligible")