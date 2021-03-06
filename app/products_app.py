import csv

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

def valid_id(id):
    ids = []
    for product in products:
        ids.append(product["id"])
    while(id not in ids):
        id = input("Wrong identifier! Please insert a correct id: ")
    return id

username = input("Please insert your username: ")
print("-----------------------------------")
print("PRODUCTS APPLICATION")
print("-----------------------------------")
print("Welcome @" + username + "!")
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

product_operation = input("\nInput your operation: ")
product_operation = product_operation.title()
print("This is your desired operation: " + product_operation)

def list_products():
    for product in products:
        print(" + ", dict(product))

def show_products():
    product_id = input("OK. Please specify the product's identifier: ")
    product_id = valid_id(product_id)
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
    update_product_id = input("OK. Please specify the product's identifier: ")
    product = [product for product in products if product["id"] == update_product_id]
    if product:
        product = product[0]
        print("SHOWING A PRODUCT HERE: ", dict(product))
        update_product_name = input("name is: ")
        update_product_aisle = input("aisle is: ")
        update_product_department = input("department is: ")
        update_product_price = input("price is: ")
        updated_product = {
            "id": update_product_id,
            "name": update_product_name,
            "aisle": update_product_aisle,
            "department": update_product_department,
            "price": update_product_price,
        }
        print("UPDATED PRODUCT IS: ", updated_product)
        confirmation = input("Please type Y to confirm update: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            product["name"] = update_product_name
            product["aisle"] = update_product_aisle
            product["department"] = update_product_department
            product["price"] = update_product_price
            print("Product has been updated!")
        else:
            print("OK. We won't update")
    else:
        print("ERROR, Invalid product ID!")

def destroy_operation():
    destroy_product_id = input("Please specify the product's identifier: ")
    product = [p for p in products if p["id"] == destroy_product_id]
    if product:
        product = product[0]
        print("REMOVING A PRODUCT: ", dict(product))
        del products[products.index(product)]
        print("Product list has been updated!")
    else:
        print("ERROR, Invalid product ID!")

if product_operation == "List": list_products()
elif product_operation == "Show": show_products()
elif product_operation == "Create": create_product()
elif product_operation == "Update": update_product()
elif product_operation == "Destroy": destroy_operation()
else:
    print("PLEASE CHOOSE ONE OF THE AVAILABLE OPERATIONS!")


other_path = "data/other_products.csv"
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
