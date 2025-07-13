import json
from database import database

print("Name of the file: ")
file = input()

# Read file and save it in a variable
try:
    with open(file, "r") as f:
        data = json.load(f)
        # print(data)
except Exception as e:
    print("There was an error opening the file: ", e)

print("Type the query:")
query = input()

# Call the function to connect, write and read the database
try:
    database(data, query)
except Exception as e:
    print(e)