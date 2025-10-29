'''Password Generator'''
#Importing necessary modules.
import time
import random

print('Welcome to Password Generator Application')
print('Loading...')

time.sleep(3) #Simulating application.

def main():
    while True:
        password = str()
        
        password_length = int(input('Enter the length of password (Recommended length:8): '))

        for i in range(password_length):
            password_picker = [chr(random.randint(48, 57)), chr(random.randint(65, 90)), chr(random.randint(97, 122))]

       
            password += password_picker[random.randint(0, 2)]

        print('Generated password is: ', password)
        
        choice = input('Do you want to continue?\nEnter (Yes/No): ').lower()

        if choice == 'no':
            break
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

#Driver code
if __name__ == '__main__':
    main()
