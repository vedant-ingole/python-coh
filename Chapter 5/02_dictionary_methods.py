myDict = {
    "fast":"Quickly",
    "harry": "A coder",
    'sun':1,
    'marks':[12,13,123,34],
    'anotherdict':{'harry':'Player'},
    1:2
} 

#DICTIONARY METHODS!!

print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))

print(myDict.values()) #Prints the values of the dictionary.
print(myDict.items()) # Returns TUPLE(we can itrate init).

updateDict = {
    'Moon':1,
    'harry':'Dancer'
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry2")) #returns none
print(myDict["harry2"]) # throws an error

