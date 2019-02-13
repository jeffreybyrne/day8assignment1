# Define a function that accepts a percentage as an argument and returns a letter grade (A+, A, A-, B+, etc) for that
# percentage.
#
# Prompt your user to enter a percentage and display a message showing them the equivalent letter grade.
print('Please enter a percentage grade')
user_num = int(input())
# if type(user_num) != int:
#     print('Invalid input, try again')

def perc_to_letter(number):
    # if (type(user_num) != int) and (type(user_num) != float):
    #     print('{} is not a valid number')
    #First, validate that the number is in the right range, otherwise give an error message
    if (number > 100) or (number < 0):
        print('{} is not a valid input'.format(number))
    #Took this list of number-to-grades from Wikipedia, logic from here on is pretty straightforward
    elif (number >= 97 and number <= 100):
        print('{} as a letter grade is an A+'.format(number))
    elif (number >= 93 and number < 97):
        print('{} as a letter grade is an A'.format(number))
    elif (number >= 90 and number < 93):
        print('{} as a letter grade is an A-'.format(number))
    elif (number >= 87 and number < 90):
        print('{} as a letter grade is a B+'.format(number))
    elif (number >= 83 and number < 87):
        print('{} as a letter grade is a B'.format(number))
    elif (number >= 80 and number < 83):
        print('{} as a letter grade is a B-'.format(number))
    elif (number >= 77 and number < 80):
        print('{} as a letter grade is a C+'.format(number))
    elif (number >= 73 and number < 77):
        print('{} as a letter grade is a C'.format(number))
    elif (number >= 70 and number < 73):
        print('{} as a letter grade is a C-'.format(number))
    elif (number >= 67 and number < 70):
        print('{} as a letter grade is a D+'.format(number))
    elif (number >= 63 and number < 67):
        print('{} as a letter grade is a D'.format(number))
    elif (number >= 60 and number < 63):
        print('{} as a letter grade is a D-'.format(number))
    else:
        print('{} as a letter grade is an F'.format(number))

#Finally, call the function defined above with the input from the user
perc_to_letter(user_num)
