# ---------------------program-1-------------------------------------------
# from sys import argv 
# print(type(argv)) # argv is a list 
# # argv jo ki ek list hai uke 0 index pe file ka name aata hai uske baad jo bhi
# # argument me value hoti hai further index pe hote hain. 
# print(f'{argv} len of argv : {len(argv)}')
# for ind,val in enumerate(argv):
#     print(f'{ind} : {val}') 
    
# Hum jo bhi argument me pass krte hain vo as a string leta hai chahe vo int or float hi q na ho. 

# ---------------------program-2-to sum the all the arguments provided during the run of python file------------------------------------------
# from sys import argv 

# sum = 0 
# for comman_line_args in argv[1:]:
#     sum += float(comman_line_args) 
# print(f'sum of command line argv is : {sum}') # if we do not provide the any command line argument then sum will be zero.

# ----------------------program-3-------------------------
# agar hum string ko bina double quote ke pass krenge as a command line argument to space ke baad dura value maana jyaga
# aur agar hme pura string ek hi index pe chaghiye to hme usko double quoute/single quote me dena hoga. 

from sys import argv 
for ind,val in enumerate(argv[1:]):
    print(f'{ind} : {val}')