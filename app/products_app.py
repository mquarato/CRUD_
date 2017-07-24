import csv
import operator

csv_file_path = "data/products.csv"
other_path = "data/other_products.csv"

products = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    return matching_products[0]

products = sorted(products, key=operator.itemgetter("id"))

print("-----------------------------------")
print("PRODUCTS APPLICATION")
print("-----------------------------------")
print("Welcome @mquarato!")
print("\n")
print("There are " + str(len(products)) + " products in the database. Please select an operation:")
print("\n")
print("   operation | description")
print("   --------- | --------------------")
print("   'List'    | Display a list of product identifiers and names.")
print("   'Show'    | Show information about a product.")
print("   'Create'  | Add a new product.")
print("   'Update'  | Edit an existing product")
print("   'Destroy' | Delete an existing product.")
print("\n")

def list_products():
    for product in products:
        print(" + ", dict(product))

def show_products():
    product_id = input("OK. Please specify the product's identifier: ")
    for product in products:
        product_show = lookup_product_by_id(product_id)
    print("SHOWING A PRODUCT HERE: ", dict(product_show))

def create_product():
    print("CREATING A NEW PRODUCT:")
    product_name = input("name is: ")
    product_aisle = input("aisle is: ")
    product_department = input("department is: ")
    product_price = input("price is: ")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price,
    }
    print("NEW PRODUCT IS: ", new_product)
    products.append(new_product)

def update_product():
    print("Update a product ")
    product_id = input("OK. Please specify the product's identifier: ")
    if int(product_id) <= len(products):
        for product in products:
            product_show = lookup_product_by_id(product_id)
        print("SHOWING A PRODUCT HERE: ", dict(product_show))
        row = int(product_id)
        product_name = input("name is: ")
        product_aisle = input("aisle is: ")
        product_department = input("department is: ")
        product_price = input("price is: ")
        updated_product = {
            "id": product_id,
            "name": product_name,
            "aisle": product_aisle,
            "department": product_department,
            "price": product_price,
        }
        del products[row-1]
        products.append(updated_product)
        print("UPDATED PRODUCT IS: ", updated_product)
    else:
        print("ERROR, Invalid product ID!")


def destroy_operation():
    product_id = input("Please specify the product's identifier: ")
    if int(product_id) <= len(products):
        for product in products:
            product_show = lookup_product_by_id(product_id)
        print("REMOVING A PRODUCT: ", dict(product_show))
        row = int(product_id)
        del products[row-1]
    else:
        print("ERROR, Invalid product ID!")

#while True:
product_operation = input("\nInput your operation: ")

print("This is your desired operation: " + product_operation)

if product_operation == "List": list_products()
elif product_operation == "Show": show_products()
elif product_operation == "Create": create_product()
elif product_operation == "Update": update_product()
elif product_operation == "Destroy": destroy_operation()
else:
    print("PLEASE CHOOSE ONE OF THE AVAILABLE OPERATIONS!")


other_path = "data/other_products.csv"
with open(other_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
