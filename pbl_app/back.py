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

mongodb+srv://ruhandave2003:admin@cluster0.0zjtugn.mongodb.net/

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
import random

#Global constants
#These are temporarily used for creation of artificial data, there can be more than 200 unique combinations based on the informations used.
AREA = ["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"]
STUDENT_NAME = ["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"]
YEAR_OF_STUDY = ["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"]
BRANCH = ["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"]
HOSTEL_NAME = ["A1 Hostel", "Edunest Hostel", "StudentHaven Dormitory", "CampusComfort Residency", "Scholar's Retreat", "LearningLodge Hostel"]
TYPE = ["Boys", "Girls", "All"]
MESSAGE = ["Hi", "Hello", "How are you?", "I'm fine", "Wassup", "How do you do?", "I'm doing great", "Are you planning to stay here?", "Yes", "No", "Just a regular conversation", "I'm behind you, don't look back"]
COLLEGE_NAME = ["DYPIEMR", "DYPCOE", "DYPIU", "PCCOE", "PCCOER", "COEP", "VJTI", "IITB", "IITH", "PICT", "MITWPU", "MITADT", "Harvard University", "Oxford university"]
GENDER = ["Male", "Female", "Transgender", "Other", "Prefer not to say"]
REVIEW = ["Very nice", "Very good", "Fine enough", "Need improvements", "Bad", "Very bad"]
OWNER_NAME = ["Felix", "Raith", "Proximity", "Ruhan"]

COLLECTION_NAME = ["login detail", "user profile", "hostel profile", "hostel rating", "owner detail"]


# Establish connection to MongoDB
client = pymongo.MongoClient("mongodb+srv://ruhandave2003:admin@cluster0.0zjtugn.mongodb.net/")
db = client["Cluster0"]  # Replace "mydatabase" with your database name

# Create collections
login_detail_col = db["login detail"]
user_profile_col = db["user profile"]
hostel_profile_col = db["hostel profile"]
hostel_rating_col = db["hostel rating"]
owner_detail_col = db["owner detail"]

#making of sample data
for i in range(10):
    name = random.choice(STUDENT_NAME)
    college = random.choice(COLLEGE_NAME)
    year = random.choice(YEAR_OF_STUDY)
    branch = random.choice(BRANCH)
    gender = random.choice(GENDER)
    hostel = random.choice(HOSTEL_NAME)
    area = random.choice(AREA)
    price = random.randint(100, 500)
    type_room = random.choice(TYPE)
    review = random.choice(REVIEW)
    wash = random.choice(["private", "common", "none"])
    owner = random.choice(OWNER_NAME)

    login_dict = {"user_id" : i+1, "user email" : f"{name}@gmail.com", "password" : f"{name}_{i+1}"}
    a = login_detail_col.insert_one(login_dict)
    user_dict = {"user_id" : i+1, "user_name" : name, "user_age" : random.randint(18,23), "college" : college, "year_of_study" : year, "branch" : branch, "phone_no" : random.randint(1000000000, 9999999999), "gender" : gender, "photo" : None, "about" : "Blah Blah Blah"}
    b = user_profile_col.insert_one(user_dict)
    hostel_profile_dict = {"hostel_id" : i+1, "owner_id" : i+1, "hostel_name" : hostel, "area" : area, "price" : price*50, "type" : type_room, "intake" : random.randint(1,4), "washroom_type" : wash, "elect_bill" : random.choice(["Self pay", "Owner pay"])}
    c = hostel_profile_col.insert_one(hostel_profile_dict)
    hostel_rating = {"hostel_id" : i+1, "owner_id" : i+1, "user_name" : name, "rating" : random.randint(0, 5), "review" : review}
    d = hostel_rating_col.insert_one(hostel_rating)
    owner_detail = {"owner_id" : i+1, "owner_name" : owner, "phone_no" : random.randint(1000000000, 9999999999), "email" : f"{owner}@gmail.com"}
    e = owner_detail_col.insert_one(owner_detail)



#checking existance of database and tables
def check_db():
    dblist = client.list_database_names()
    if "Cluster0" not in dblist:  # check if the specific database exists, if no then create it.
        print("Database does not exists")
    else: #this part is used to check tables, which in rare case wont be there
        print("Database exists, checking for collections")
        col_list = client.list_collection_names()
        for i in COLLECTION_NAME: 
            if i not in col_list:
                print(f"Collection '{i}' does not exist" )
            else:
                print(f"Collection '{i}' exists!")
        



