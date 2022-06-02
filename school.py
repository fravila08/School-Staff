import csv
import os
import json
from Staff import Staff
from Student import Student


class School():
    def __init__(self, name):
        self.name=name
        self.students = Student.all_students(self) 
        self.staff = Staff.all_staff(self)
