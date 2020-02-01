# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:28:37 2020

@author: CEC
"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def init(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

print ("Employee.doc:", Employee.__doc__)
print ("Employee.name:", Employee.__name__)
print ("Employee.module:", Employee.__module__)
print ("Employee.bases:", Employee.__bases__)
print ("Employee.dict:", Employee.__dict__)