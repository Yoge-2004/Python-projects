'''Calculator Application'''
#Importing necessary modules.
import time

print('Welcome to calculator application')
print('Loading...')

#Simulating the feel of application.
time.sleep(3)
def help():
    print('Press \n+ for Addition\n- for Subtraction\n* for Multiplication\n/ for Division\n// for floor division (integer division)\n** for Exponentiation\n')

help()
while True: #Application runs until an error occured or user needs to stop it.
    #User input snippet.
    number1 = int(input('Enter a number: '))
    number2 = int(input('Enter another number: '))

    operator = input('Enter the operator: ')

    #Checking for the operation to be performed.
    if operator == '+':
        print(number1 + number2)

    elif operator == '-':
        print(number1 - number2)

    elif operator == '*':
        print(number1 * number2)

    elif operator == '/':
        print(number1 / number2)

    elif operator == '//':
        print(number1 // number2)

    elif operator == '%':
        print(number1 % number2)

    elif operator == '**':
        print(number1 ** number2)

    else: #If no operators specified by the user is found.
        print('Invalid operator.')

    #Asking to the user whether they need to perform any other calculations.
    print('Do you want to perform any other calculation?')

    choice = input('Enter (Yes/No): ').lower()
    print()
    
    if choice == 'no':
        break
    
    help_choice = input('Enter Yes if you need help to use the application else enter No: ').lower()

    if help_choice == 'yes':
        help()
    else:
        pass
    

#Application terminated by the user or any unexpected error occured.
print('Thanks for using my application.')

#Asking for feedback from the user.
print('If you give feedback on the application, then it would be useful for us to improve our application further.\nDo you want to give rating? ')

feedback_choice = input('Enter (Yes/No): ').lower()

if feedback_choice == 'yes':
    print('Give the rating on the scale of 1(poor) to 5(best)')

    rating = int(input('Enter the rating: '))
    if rating > 0 and rating <= 5:
        print('Thanks for your valuable rating.')
    else:
        print('Invalid rating.')

else:
    pass
