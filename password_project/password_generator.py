import random # imports the 'random' module, provides functions for generating random numbers 
print('Your password: ') # field informing the user of generated password
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?' # initializes string variable containing characters to be used in composing new password
password = '' # initializes an empty string variable to store generated password
for x in range(16): # for loop that will iterate 16 times to generate each character for password
    password += random.choice(chars) # inside loop, this line selects random character from chars string and adds it to the password string

print(password) # after the loop completes, print generated password to console 
