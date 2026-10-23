# Text-Based Invoice Data Extraction

invoices = [
    "P101,2,500.00",
    "P102,5,1200.50",
    "P103,3,750.00",
    "P104,abc,400.00",
    "P105,2,invalid",
    "P106,4"
]

print("INVOICE DATA EXTRACTION")
print("-" * 65)
print(f"{'Product Code':<15}{'Quantity':<12}{'Amount':<15}{'Status'}")
print("-" * 65)

for record in invoices:
    try:
        # Split the invoice string into fields
        fields = record.split(",")

        # Validate the number of fields
        if len(fields) != 3:
            raise ValueError("Incorrect number of fields")

        product_code = fields[0].strip()
        quantity_text = fields[1].strip()
        amount_text = fields[2].strip()

        # Validate empty fields
        if not product_code or not quantity_text or not amount_text:
            raise ValueError("Empty field")

        # Extract and validate quantity and amount
        quantity = int(quantity_text)
        amount = float(amount_text)

        if quantity <= 0 or amount < 0:
            raise ValueError("Invalid quantity or amount")

        # Display valid invoice data
        print(f"{product_code:<15}{quantity:<12}"
              f"{amount:<15.2f}Valid")

    except ValueError as error:
        print(f"{record:<42}Malformed: {error}")

print("-" * 65)