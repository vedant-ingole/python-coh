greeting = "Good Morning"
name = "Harry"

# print(greeting + name)

#indices of strings
# print(name[1])
# name[4] = "d" -->replacing any index of string is not allowed 


# print(name[0:3]) # from 0 till 3{3 excluded}.
# print(name[:3])
# print(name[3:])

#Negative index_ starts from behind
c = name[-4:-1] #is same as[1:4]
c = name[-2:-4] #is same as[1:4]
# print(c)


#Slicing with skipping- as third argument.
d = name[1:4:1]
print(d)

name1 = "HarryIsGood"
print(name1[0::2]) #Skips every second index.

print(name1[:0:-1])


