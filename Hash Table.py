# Declare a dictionary 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']", dict['Class'])

dict['Class']='New Class'
print ("dict['Class']", dict['Class'])

dict['school']='added school'
print ("dict['school']:", dict['school'])
del dict['Name']
print (dict)