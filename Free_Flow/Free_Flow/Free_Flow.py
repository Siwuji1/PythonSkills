from datetime import date #import this for date
import getpass            #import this for username
import random             #import this to use random

################################################################
#                                                              #
# Author: Sorochi Iwuji                                        #
# Date: 07/22/2022                                             #
# Purpose: To practice Python with Fahrenheit conversion to    #
# celcius, as well as practice with elif and if right after    #
# with the grade calculator, finish off with a password        #
# generator and a little more if and elif practice             #
#                                                              #
################################################################

print (getpass.getuser()) #This displays your windows username
print (date.today())      #This displays the current systems date
print ()                  #This provides us space between the two sequence lines
name = input ('Enter your name here: ') #This displays the instruction for recieving the name of user
print ('Hello ' + name + ', Welcome to the world of Python, this is your Free Flow')

print()
print(type(name))

print()
fahrenheit = float(input ('Enter a temperature in Farenheit, as the first part of our Free Flow: '))

print()
celsius = (fahrenheit - 32) * (5/9)
display_celsius = round(celsius,2)
print('Your temp is celsius is ' + str (display_celsius) + ' and it is type ' + str (type (display_celsius)))

print()
numberOfDaysMissed = 0
currentGrade = 0.0
attendancePercentage = 0.0
tempInput = ''

tempInput = input('Please enter the number of days you have missed in school: ')

if tempInput.isnumeric():
    numberOfDaysMissed = int(tempInput)
else:
    print('Number of school days missed must be an integer')
    tempInput = input('Please enter the number of days you have missed in school: ')
    numberOfDaysMissed = int(tempInput)

tempInput = input('Please enter your numeric grade (ie 89.5) ')

try: #try to get this to be a loop after error
    currentGrade = float(tempInput)
except:
    print('Current grade must be a number')
    tempInput = input('Please enter your numeric grade (ie 89.5) ')
    currentGrade = float(tempInput)

try:
    if numberOfDaysMissed == 0:
        attendancePercentage = 1.02
    elif numberOfDaysMissed == 1 or numberOfDaysMissed == 2:
        attendancePercentage = 1.00
    elif numberOfDaysMissed == 3:
        attendancePercentage = 0.98
    elif numberOfDaysMissed == 4:
        attendancePercentage = 0.96
    elif numberOfDaysMissed == 5:
        attendancePercentage = 0.94
    elif numberOfDaysMissed == 6:
        attendancePercentage = 0.92
    else:
        attendancePercentage = 0.90

    tempGrade = 0.0
    letterGrade = ''

    tempGrade = round(currentGrade * attendancePercentage,3)

    if tempGrade >= 89.445:
        letterGrade = 'A'
    elif tempGrade <= 89.444 and tempGrade > 79.445:
        letterGrade = 'B'
    elif tempGrade <= 79.444 and tempGrade > 69.445:
        letterGrade = 'C'
    elif tempGrade <= 69.444 and tempGrade > 59.445:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
    print( 'Your grade calculated is a ' + letterGrade)

except Exception as ex:
    print(ex.args)

print()
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SPECIAL_CHARACTERS = '!@#$%&*'
NUMBERS = '1234567890'

lengthOfPassword = 0
useSpecialCharacters = False
useNumbers = False
password = ''
count = 0

tempInput = input('Enter your password length of choice ( 8 to 16 in length) ')
lengthOfPassword = int(tempInput)
tempInput = input('Do you want to use numbers? Yes/ No ')

if tempInput == 'yes' or tempInput =='yes':
    useNumbers = True
else:
    useNumbers = False

tempInput = input('Do you want to use special characters? Yes/ No ')

if tempInput == 'yes' or tempInput =='yes':
    useSpecialCharacters = True
else:
    useSpecialCharacters = False

while count < lengthOfPassword:
    randomNumber = random.randrange(0,25,1)
    pwChar = ALPHABET[randomNumber]
    password = password + pwChar
    count = count + 1

if useSpecialCharacters:
    insertPosition = int(lengthOfPassword /3)
    randomNumber = random.randrange(0,6,1)
    pwChar = SPECIAL_CHARACTERS[randomNumber]
    tempChar = password[insertPosition]
    tempPassword = password.replace(tempChar, pwChar,1);
    password = tempPassword

if useNumbers:
    insertPosition = int(lengthOfPassword /2)
    randomNumber = random.randrange(0,9,1)
    pwChar = NUMBERS[randomNumber]
    tempChar = password[insertPosition]
    tempPassword = password.replace(tempChar, pwChar,1);
    password = tempPassword

print(password)
print(len(password))

print()
x = 0
if x < 2:
    print ('Small')
elif x < 10:
    print ('Medium')
else:
    print ('LARGE')
print ('All Done')

print()
x = 0
if x < 2:
    print ('Small')
if x < 10:
    print ('Medium')
else:
    print ('LARGE')
print ('All Done')

