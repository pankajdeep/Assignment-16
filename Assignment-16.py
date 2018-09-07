#Q.1- Write a python script to create a databse of students named Students.
#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
#Q.4- Print the names of all the students who scored more than 80 marks.

#--------------------------------Creating Database--------------------------------------------
import pymongo
client=pymongo.MongoClient()
database=client['Students']

#--------------------------------Creating Collection-------------------------------------------

collection=database['student_collection']

#-------------------------------Taking Names and Marks-----------------------------------------

for i in range(0,10):
    name=input("Enter name")
    marks=int(input("Enter marks"))
    collection.insert_one({'Name':name,'Marks':marks})
    
#------------------------------Printing names of all the students who scored more than 80 marks---------------
    
data=collection.find({"Marks":{"$gt":80}})
for d in data:
    print(d)
