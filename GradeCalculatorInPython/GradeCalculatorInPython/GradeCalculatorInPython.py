from datetime import date
import getpass

######################################################################
#                                                                    #
#   Author: Sorochi Iwuji                                            #
#   Date Written: 09/30/2021                                         #
#   Purpose: This is a program that calculates and                   #
#   then displays the calculated final letter grade for a student    #
#                                                                    #
#######################################################################

#This shows todays date and active user
print(str(getpass.getuser()) + '            ' + str(date.today()))

#Varibles defined here for the scope needed
numberOfDaysMissed = 0
currentGrade = 0.0
attendancePercentage = 0.0
tempInput = ''

tempInput = input('Please enter the number of days missed: ')

#Confirming number of days missed and grade
if tempInput.isnumeric():
    numberOfDaysMissed = int(tempInput)
else:
    print('Number of days missed must be an integer')
    tempInput = input('Please enter the number of days missed: ')
    numberOfDaysMissed = int(tempInput)

tempInput = input('Please enter students numeric grade (ie 89.5)')

try:
    currentGrade = float(tempInput)
except:
    print('Current grade must be a number')
    tempInput = input('Please enter students numeric grade (ie 89.5): ')
    currentGrade = float(tempInput)

#For number of days missed and numeric grade
#If else for current grade and attendance to calculate the letter grade
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
    elif tempGrade <= 89.444 and tempGrade >= 79.445:
        letterGrade = 'B'
    elif tempGrade <= 79.444 and tempGrade >= 69.445:
        letterGrade = 'C'
    elif tempGrade <= 69.444 and tempGrade >= 59.445:
        letterGrade = 'D'
    else:
        letterGrade = 'F'

    print('Your grade is ' + letterGrade) #prints grade

#This exception class will find any errors in the code
# & give a sort of reasoning for it
except Exception as ex:
    print(ex.args)