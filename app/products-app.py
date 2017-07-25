#from IPython import embed
import csv

products = []

csv_file_path = "data/products.csv"
headers = ["id", "name", "aisle", "department", "price"] # for "Further Exploration" use: ["product_id", "product_name", "aisle_id", "aisle_name", "department_id", "department_name", "price"]
user_input_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

#
# READ PRODUCTS FROM FILE
#

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

#
# HANDLE USER INPUT
#

def list_products():
    print("LISTING PRODUCTS")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("READING PRODUCT", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT", product)

def update_product():
    product_id = input("WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def destroy_product():
    product_id = input("WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

menu = """
-----------------------------------
PRODUCTS APPLICATION
-----------------------------------
    Hi.

    Welcome {0} to the Products App!

    There are {1} products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format("@jascharf", len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

#
# WRITE PRODUCTS TO FILE
#

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()

    for product in products:
        writer.writerow(product)

#Thank you Professor Rossetti for assistance with the code via slack
