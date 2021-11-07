letter = '''   Dear <|NAME> ,
Your Selected.
Date: <|DATE>.'''

name = input("Enter name:")
date = input("Date:")
letter = letter.replace("<|NAME>",name)
letter = letter.replace("<|DATE>",date)

print(letter)                

