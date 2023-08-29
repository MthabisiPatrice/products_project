import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename (str): the name of the CSV file to read.
        key_column_index (int): the index of the column
            to use as the keys in the dictionary.

    Return:
        dict: a compound dictionary that contains the contents
        of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    # Step 1: Read the products.csv file into a dictionary
    products_dict = read_dictionary('products.csv', 0)  # Assuming product number is in the first column (index 0)
    print(products_dict)

    # Step 2: Process the request.csv file
    with open('request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first line (column headings)
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])

            # Retrieve the product information from the products dictionary
            product_info = products_dict.get(product_number)
            if product_info:
                product_name = product_info[1]
                price = float(product_info[2])

                # Print the product name, requested quantity, and product price
                print(f"Product: {product_name}")
                print(f"Requested Quantity: {quantity}")
                print(f"Price: {price:.2f}\n")
            else:
                print(f"Product with number {product_number} not found.\n")

if __name__ == '__main__':
    main()
