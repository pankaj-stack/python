import os 
import time 

python_file_path = '/home/echelon/python_notes/python/common.py' 

for i in range(10):
    print(f'This is the {i+1} line from running_terminal_commands.py')
    time.sleep(0.5)
os.system(f'python {python_file_path}') # running the python file from this line of code 
print('after 7 seconds screen will be cleared...') 
time.sleep(7) 
os.system('clear')