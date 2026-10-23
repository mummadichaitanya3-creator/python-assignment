# Progressive Electricity Billing

units = int(input("Enter electricity units consumed: "))

# Energy charge calculation
if units <= 100:
    energy_charge = units * 2
elif units <= 200:
    energy_charge = (100 * 2) + (units - 100) * 3
else:
    energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

fixed_charge = 50
surcharge = energy_charge * 0.05

# Rebate calculation
if units < 100:
    rebate = 20
else:
    rebate = 0

total_bill = energy_charge + fixed_charge + surcharge - rebate

print("\n--- Electricity Bill ---")
print("Units Consumed:", units)
print("Energy Charge:", energy_charge)
print("Fixed Charge:", fixed_charge)
print("Surcharge:", surcharge)
print("Rebate:", rebate)
print("Final Bill:", total_bill)