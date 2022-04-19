from hashlib import sha256


import random
import string

def RandString(length): # define the function and pass the length as argument
    # Print the string in Lowercase
    result = ''.join((random.choice(string.ascii_letters) for x in range(length))) # run loop until the define length

    return result

letterstring = RandString(20)

print("Str  is: ", letterstring)

print("Hash is: ", sha256(letterstring.encode("ascii")).hexdigest())

# Open the file in read mode
with open('linux.txt', "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    word = random.choice(words)

# print random string
print("Word is: ", word)

print("Hash is: ", sha256(word.encode("ascii")).hexdigest())


mymessage = input('Enter Your Own string or message to print hash: ')

print("Your Message:", mymessage)
print("Your Hash is: ", sha256(mymessage.encode("ascii")).hexdigest())
