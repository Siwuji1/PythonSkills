import datetime #Todays Date
import getpass #Your Name

#############################################################################
#                                                                           #
#   Author: Sorochi Iwuji                                                   #
#   Date Written: 09/20/2021                                                #
#   Purpose: This is a program that displays converted temperature          #
#                                                                           #
#############################################################################


print(datetime.datetime.now()) #Displays users name
print(getpass.getuser()) #Displays todays date
print()

name = input('Enter Your Name Here:') #Declares the variable name

print('Hello ' + name + ', Welcome to the world of Python') #Displays name and message
print()
print(type(name)) #Displays variable type
print()
fahrenheit = float(input("Enter a temperature in fahrenheit:")) #Allows for temperature input
print()
celsius = (fahrenheit - 32) * (5/9) #Calculates conversion
display_celsius = round(celsius,2) #Allows for rounding of the number outputed
print('Your temp in celsius is ' + str(display_celsius) + ' and it is type ' + str(type(display_celsius))) #Displays conversion
print()

Score = float(input("Enter in a your test grade:")) #Allows for grade input
print()
fail = (Score + 30) #Calculates grade
display_fail = round(fail,2) #Allows for rounding of the number outputed
print('Your curved grade on the exam is ' + str(display_fail) + ' and it is ' + str(type(display_fail))) #Displays conversion
