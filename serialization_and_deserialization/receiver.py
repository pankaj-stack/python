# Receiver is responsible to deserialize Employee objects
import pickle

f = open('emp.ser', 'rb')
print('Deserializing Employee objects and printing data...')
while True:
    try:
        e = pickle.load(f)
        e.display()
    except EOFError:
        break

print('Deserialization of All Employee Objects completed')
