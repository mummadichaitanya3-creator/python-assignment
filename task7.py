rooms = [
    {"room": "101", "floor": 1, "electricity": 120, "water": 3000},
    {"room": "102", "floor": 1, "electricity": 190, "water": 2500},
    {"room": "201", "floor": 2, "electricity": 150, "water": 4200},
]

electricity_rate = 8
water_rate = 0.025
electricity_limit = 180
water_limit = 4000

floor_totals = {}

for room in rooms:
    electricity_charge = room["electricity"] * electricity_rate
    water_charge = room["water"] * water_rate

    print("Room:", room["room"])
    print("Electricity charge:", electricity_charge)
    print("Water charge:", water_charge)

    if room["electricity"] > electricity_limit:
        print("Electricity limit exceeded")
    if room["water"] > water_limit:
        print("Water limit exceeded")

    floor = room["floor"]
    if floor not in floor_totals:
        floor_totals[floor] = {"electricity": 0, "water": 0}

    floor_totals[floor]["electricity"] += room["electricity"]
    floor_totals[floor]["water"] += room["water"]

print("\nFloor totals:")
for floor, totals in floor_totals.items():
    print("Floor", floor,
          "- Electricity:", totals["electricity"], "kWh,",
          "Water:", totals["water"], "liters")