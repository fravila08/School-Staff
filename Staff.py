import csv
import os
import json

staff=[]
with open(os.getcwd()+'/data/staff.csv', newline='') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
        for row in spamreader:
            staff.append(row)

staff.pop(0)

class Staff:
    def __init__ (self, name, age, role, employee_id, password):
        self.name=name
        self.age=age
        self.role=role
        self.id=employee_id
        self.password=password
    def __str__(self):
         return f"{self.name}, {self.age},{self.role},{self.id},{self.password}"
    def all_staff(self):
        culpepper=Staff(*staff[0][0].split(','))
        dewey=Staff(*staff[1][0].split(','))
        mertz=Staff(*staff[2][0].split(','))
        dickerson=Staff(*staff[3][0].split(','))
        Heimlich=Staff(*staff[4][0].split(','))
        xx=Staff(*staff[5][0].split(','))
        return(culpepper, dewey, mertz, dickerson, Heimlich, xx)
#These are the staff


