"""
This file is the backend part of the project
It takes in data from the GUI, process it and return it back to the GUI
Needs database(MongoDB)

First creat the requirements to connect and make databases on MongoDb, further instructions for data processing will be given soon.
Functions required:
- Create table and insert data
- Update or delete data
- Display data with some conditions.
- Retrieve the data and store it in a python variable.

Make sure to leave comments to explain code.
"""

#Create a function that takes in type(hostel/flat/roommate) and area, and return whatever details the database gives. 
#This function will be used to display all the relevant hostel/flat/roommate according to the user choice. if no area is mentioned, show all.

#Create a function that takes in user name, place, phone no, email, gender, age, year of study, branch. and save these on the database. this is used in edit profile section.

#Create a function that takes in a list of preferences of user(studious, nigth owl, gamer etc), and return all the roommates who has ATLEAST 3 similarities

#create a function that takes in email and password to check if such user exists. this will be used in login section.

#Create a function that takes in email and new pasword to change the password. otp and all will be taken care by front end.

#Create a funtion that takes in username, email, phone number, password. and save in database. this is used to create a new account.

#More functions to create are coming soon.


import pymongo

# Establish connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Replace "mydatabase" with your database name

# Create collections
hostel_col = db["hostel"]
student_col = db["student"]

# Define sample data
hostel_data = [
    {"hostel_id": 1, "hostel_name": "Hostel A", "price": 5000},
    {"hostel_id": 2, "hostel_name": "Hostel B", "price": 6000},
    {"hostel_id": 3, "hostel_name": "Hostel C", "price": 5500},
    {"hostel_id": 4, "hostel_name": "Hostel D", "price": 7000},
    {"hostel_id": 5, "hostel_name": "Hostel E", "price": 6500}
]

student_data = [
    {"stu_id": 1, "stu_name": "John", "college_name": "ABC College"},
    {"stu_id": 2, "stu_name": "Alice", "college_name": "XYZ University"},
    {"stu_id": 3, "stu_name": "Bob", "college_name": "DEF Institute"},
    {"stu_id": 4, "stu_name": "Emma", "college_name": "GHI School"},
    {"stu_id": 5, "stu_name": "Michael", "college_name": "JKL Academy"}
]

# Insert data into collections
hostel_col.insert_many(hostel_data)
student_col.insert_many(student_data)

print("Data inserted successfully.")
