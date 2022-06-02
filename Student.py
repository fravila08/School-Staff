import csv
import os
import json

student=[]
with open(os.getcwd()+'/data/students.csv', newline='') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
        for row in spamreader:
            student.append(row)

student.pop(0)
student1=student[0][0].split(',')

class Student:
    def __init__ (self, name, age, role, school_id, password):
        self.name=name
        self.age=age
        self.role=role
        self.id=school_id
        self.password=password
    def __str__(self):
         return f"{self.name}, {self.age},{self.role},{self.id},{self.password}"
    def all_students(self):
        lisa=Student(*student1)        
        jessie=Student(*student[1][0].split(','))
        slater=Student(*student[2][0].split(','))
        kim=Student(*student[3][0].split(','))
        dave=Student(*student[4][0].split(','))
        doug=Student(*student[5][0].split(','))
        return(lisa, jessie, slater, kim, dave, doug)

     
     
#These are the students


