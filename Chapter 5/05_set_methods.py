b = set()
print(type(b))

#SETS METHODS.


b.add(6) # adding values to empyt sets. 
b.add(7)

# b.add([2,3,4])  # cannot add list in set Since, it's mutable
# b.add({1:2}) # cannot add dictionary as well.
b.add((2,3,4)) # tuples can be added

print(len(b))

b.remove(6)


print(b) 
print(b.pop())