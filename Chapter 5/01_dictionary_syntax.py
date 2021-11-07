
myDict = {
    "Fast":"Quickly",
    "Harry": "A coder",
    'sun':1,
    'Marks':[12,13,123,34],
    'anotherdict':{'harry':'Player'}
} 
 
#  Dictionaries are mutable.
myDict['Marks'] = [23,45]
print(myDict['Marks'])

print(myDict['anotherdict'])
print(myDict['anotherdict']['harry'])