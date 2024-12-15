# Sender is responsible to save Employee objects to the file
from emp import *
import pickle

f = open('emp.ser', 'wb')

while True:
    eno = int(input('Enter Employee Number: '))
    ename = input('Enter Employee Name: ')
    esal = float(input('Enter Employee Salary: '))
    eaddr = input('Enter Employee Address: ')
    
    e = Employee(eno, ename, esal, eaddr)
    pickle.dump(e, f)
    
    option = input('Do you want to serialize one more Employee object [Yes|No]: ')
    if option.lower() == 'no':
        break

f.close()
