from datetime import date
import getpass
import string
import random

######################################################################################
#                                                                                    #
#   Author: Sorochi Iwuji                                                            #
#   Date Written: 10/07/2021                                                         #
#   Purpose: This is a program that allows the user to create their own passwords    #
#                                                                                    #
######################################################################################

# This shows todays date and active user
print(str(getpass.getuser()) + '            ' + str(date.today()))

# Items involved in the random selection
ALPHABET = list(string.ascii_letters)
SPECIAL_CHARACTERS = list('!@#$%&*')
NUMBERS = list(string.digits)

lengthOfPassword = 0
useSpecialCharacters = False
useNumbers = False
password = ''
count = 0

while True:
    try:
        # Password length from user error message
        lengthOfPassword = int(input('Please enter a number from 8-16 for a password length: '))
        break
    except Exception as e:
        print(e)
        continue

# This allows the user to decide what length they would prefer to be in their password
tempInput = input('Error: Please enter a number from 8-16 for a password length: ')
lengthOfPassword = int(tempInput)

# This allows the user to decide if they want numbers to be in their password
tempInput = input('Would you like to use numbers (Yes/No): ')

if tempInput == 'Yes' or tempInput == 'yes':
    useNumbers = True
else:
	useNumbers = False

# This allows the user to decide if they want special charaters to be in their password
tempInput = input('Would you like to add special charaters to your password (Yes/No): ')

if tempInput == 'Yes' or tempInput == 'yes':
    useSpecialCharacters = True
else:
	useSpecialCharacters = False

#The use of the length choosen by the user
while count < lengthOfPassword:
    randomNumber = random.randrange(0,25,1)
    pwChar = ALPHABET[randomNumber]
    password = password + pwChar
    count = count + 1

#The randomization of special characters being created
if useSpecialCharacters:
   insertPosition = int(lengthOfPassword /3)
   randomNumber = random.randrange(0,6,1)
   pwChar = SPECIAL_CHARACTERS[randomNumber]
   tempChar = password[insertPosition]
   tempPassword = password.replace(tempChar, pwChar, 1)
   password = tempPassword

#The randomization of numbers being created
if useNumbers:
   insertPosition = int(lengthOfPassword /2)
   randomNumber = random.randrange(0,10,1)
   pwChar = NUMBERS[randomNumber]
   tempChar = password[insertPosition]
   tempPassword = password.replace(tempChar, pwChar, 1)
   password = tempPassword

#prints password
print(password)
print(len(password))
