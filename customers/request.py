import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
      "email": "hotmale@hotmail.com",
      "password": "test",
      "name": "Test Testerson",
      "id": 1
    },
    {
      "email": "graham@chapman.com",
      "password": "graham",
      "name": "Graham Chapman",
      "id": 2
    }
  ]

def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.password,
            c.name
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['email'], row['password'],
                            row['name'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


# Function with a single parameter
def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.email,
            c.password,
            c.name
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['email'], data['password'],
                            data['name'])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
  customer_index = -1

  for i, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      customer_index = i

  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
  for i, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      CUSTOMERS[i] = new_customer
      break