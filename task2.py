import math

print("====================================")
print("   ATTENDANCE RECOVERY CALCULATOR")
print("====================================")

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
target = float(input("Enter required attendance percentage: "))
missed = int(input("Enter future classes to miss first: "))

# Validate input
if (total <= 0 or attended < 0 or attended > total
        or not 0 < target <= 100 or missed < 0):
    print("Invalid input. Please enter valid values.")

else:
    # Calculate current attendance
    current = (attended / total) * 100

    # Calculate attendance after missing classes
    new_total = total + missed
    after_missing = (attended / new_total) * 100

    print("\n--------- ATTENDANCE REPORT ---------")
    print(f"Current Attendance: {current:.2f}%")
    print(f"Eligibility Target: {target:.2f}%")
    print(f"After Missing Classes: {after_missing:.2f}%")

    if attended / total >= target / 100:
        required = 0
    elif target == 100:
        required = None
    else:
        required = max(
            0,
            math.ceil(
                (target * new_total / 100 - attended)
                / (1 - target / 100)
            )
        )

    if required is None:
        print("Attend all future classes to maintain 100% attendance.")
    else:
        final_attended = attended + required
        final_total = new_total + required
        final_percentage = final_attended / final_total * 100

        print("Consecutive Classes Required:", required)
        print(f"Attendance After Recovery: {final_percentage:.2f}%")

        if required == 0:
            print("Status: You are already eligible.")
        else:
            print("Status: Attend the required classes continuously.")

    # Future attendance scenarios
    print("\n------ FUTURE SCENARIOS ------")
    for future in [5, 10, 15, 20]:
        percentage = (attended + future) / (new_total + future) * 100
        print(f"Attend next {future} classes: {percentage:.2f}%")