import csv
from datetime import datetime

# Constants
STORE_NAME = "Inkom Emporium"
SALES_TAX_RATE = 0.06

# File paths
products_file = "products.csv"
requests_file = "requests.csv"

try:
    # Open and read the products catalog file
    with open(products_file, "r") as f:
        reader = csv.reader(f)
        products = {row[0]: row[1] for row in reader}

    # Open and read the customer's order file
    with open(requests_file, "r") as f:
        reader = csv.reader(f)
        order = list(reader)

    # Print the store name
    print(STORE_NAME + "\n")

    # Print the list of ordered items
    for item in order:
        product_id, quantity = item[0], int(item[1])
        if product_id in products:
            product_name = products[product_id]
            price = float(product_name.split(",")[1])
            print(f"{product_name}: {quantity} @ {price:.2f}")

    print()

    # Compute the number of ordered items
    num_items = sum(int(item[1]) for item in order)
    print("Number of Items:", num_items)

    # Compute the subtotal due
    subtotal = sum(float(products.get(item[0], "0").split(",")[1]) * int(item[1]) for item in order)
    print("Subtotal:", f"{subtotal:.2f}")

    # Compute and print the sales tax amount
    sales_tax = subtotal * SALES_TAX_RATE
    print("Sales Tax:", f"{sales_tax:.2f}")

    # Compute and print the total amount due
    total = subtotal + sales_tax
    print("Total:", f"{total:.2f}")

    # Print a thank you message
    print("\nThank you for shopping at the", STORE_NAME + ".")

    # Get the current date and time
    current_date_and_time = datetime.now()

    # Print the current date and time
    print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

except FileNotFoundError:
    print("Error: missing file\n[Errno 2] No such file or directory:", products_file)

except PermissionError:
    print("Error: permission denied to access the file:", products_file)

except KeyError as e:
    print("Error: unknown product ID in the", requests_file, "file")
    print(repr(e))
