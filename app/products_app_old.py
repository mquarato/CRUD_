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
print("\n")

while True:
    product_operation = input("\nInput your operation: ")
    product_operation = product_operation.title()
    print("This is your desired operation: " + product_operation)
    def list_products():
        with open(csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            print("There are 20 products:")
            for row in reader:
                print(" + ", dict(row))

    def show_products():
        print("SHOWING A PRODUCT HERE:")

    def create_products():
        print("CREATING A NEW PRODUCT:")

    def product_operation():
        print("UPDATING A PRODUCT:")

    def destroy_operation():
        print("REMOVING A PRODUCT:")

    if product_operation == "List":
        list_products()
        # with open(csv_file_path, "r") as csv_file:
        #     reader = csv.DictReader(csv_file)
        #     print("There are 20 products:")
        #     for row in reader:
        #         print(" + ", dict(row))
    elif product_operation == "Show":
        product_id = input("OK. Please specify the product's identifier: ")
        def lookup_product_by_id(product_id):
            matching_products = [product for product in products if row["id"] == product_id]
            return matching_products[0]
        #for product_ids in product_id:
        #    product = lookup_product_by_id(product_id)
        #    print(product)
    elif product_operation == "Create":
        create_products()
    elif product_operation == "Update":
        product_operation()
    elif product_operation == "Destroy":
        destroy_operation()
    else:
        print("PLEASE CHOOSE ONE OF THE AVAILABLE OPERATIONS!")
        break