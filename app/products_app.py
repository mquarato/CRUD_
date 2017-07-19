import csv

csv_file_path = "data/products.csv"

print("-----------------------------------")
print("PRODUCTS APPLICATION")
print("-----------------------------------")
print("Welcome @mquarato!")
print("\n")
print("There are 21 products in the database. Please select an operation:")
print("\n")
print("   operation | description")
print("   --------- | --------------------")
print("   'List'    | Display a list of product identifiers and names.")
print("   'Show'    | Show information about a product.")
print("   'Create'  | Add a new product.")
print("   'Update'  | Edit an existing product")
print("   'Destroy' | Delete an existing product.")


while True:
    product_operation = input("")
    print("This is your desired operation: " + product_operation)
    if product_operation == "List":
        with open(csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
            print("There are 20 products:")
            for row in reader:
                print(" + " + str(row))
    elif product_operation == "Show":
        product_id = input("OK. Please specify the product's identifier: ")
        print("SHOWING A PRODUCT HERE!")
        def lookup_product_by_id(product_id):
            matching_products = [product for product in products if row["id"] == product_id]
            return matching_products[0]
    elif product_operation == "Create":
        print("CREATING A NEW PRODUCT:")
    elif product_operation == "Update":
        print("UPDATING A PRODUCT:")
    elif product_operation == "Destroy":
        print("REMOVING A PRODUCT:")
    else:
        print("PLEASE CHOOSE ONE OF THE AVAILABLE OPERATIONS!")
        break
