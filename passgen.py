import string
import random

def generatePassword():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

# Creating empty list and adding all the above strings in a single list
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)   #elements ki shuffling so that har baar random alphabets aaye
    passlen = int(input("Enter the password length: "))
    pasInitial = ""
    pas = pasInitial.join(s[0:passlen])
    print(pas)

generatePassword()