# Laboratory Chemical Inventory Validation

# Maximum allowed quantity for each storage category (in litres)
MAX_QUANTITY = {
    "flammable": 50,
    "corrosive": 40,
    "oxidizer": 20,
    "general": 100
}

# Incompatible chemical category combinations
INCOMPATIBLE = {
    ("flammable", "oxidizer"),
    ("corrosive", "oxidizer")
}

# Hypothetical laboratory inventory records
inventory = [
    {"name": "Chemical A", "category": "flammable",
     "quantity": 20, "storage": "Cabinet 1"},

    {"name": "Chemical B", "category": "oxidizer",
     "quantity": 10, "storage": "Cabinet 1"},

    {"name": "Chemical C", "category": "corrosive",
     "quantity": 45, "storage": "Cabinet 2"},

    {"name": "Chemical D", "category": "general",
     "quantity": 30, "storage": "Shelf 1"},

    {"name": "Chemical E", "category": "flammable",
     "quantity": 15, "storage": "Cabinet 3"}
]

def validate_inventory(inventory):
    errors = []
    storage_contents = {}

    for item in inventory:
        name = item["name"]
        category = item["category"].lower()
        quantity = item["quantity"]
        storage = item["storage"]

        # Validate storage category
        if category not in MAX_QUANTITY:
            errors.append(
                f"{name}: Invalid storage category '{category}'."
            )
            continue

        # Validate quantity
        if not isinstance(quantity, (int, float)) or isinstance(
            quantity, bool
        ) or quantity <= 0:
            errors.append(
                f"{name}: Quantity must be a positive number."
            )
            continue

        # Check maximum permitted quantity
        if quantity > MAX_QUANTITY[category]:
            errors.append(
                f"{name}: Quantity {quantity} L exceeds "
                f"the maximum of {MAX_QUANTITY[category]} L."
            )

        # Group chemicals by storage location
        storage_contents.setdefault(storage, []).append(item)

    # Check incompatible categories in the same storage location
    for storage, items in storage_contents.items():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                first = items[i]
                second = items[j]

                pair = (
                    first["category"].lower(),
                    second["category"].lower()
                )

                reverse_pair = (pair[1], pair[0])

                if (pair in INCOMPATIBLE or
                        reverse_pair in INCOMPATIBLE):
                    errors.append(
                        f"INCOMPATIBLE: {first['name']} "
                        f"({first['category']}) and "
                        f"{second['name']} ({second['category']}) "
                        f"are stored together in {storage}."
                    )

    # Display validation results
    print("LABORATORY CHEMICAL INVENTORY REPORT")
    print("-" * 45)

    if errors:
        print("Status: INVALID INVENTORY\n")
        for number, error in enumerate(errors, start=1):
            print(f"{number}. {error}")
    else:
        print("Status: VALID INVENTORY")
        print("All records pass the configured checks.")

# Run validation
validate_inventory(inventory)