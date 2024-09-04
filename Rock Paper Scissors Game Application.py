'''Rock Paper Scissors Game'''
#Importing necessary modules.
import time
import random
print('Welcome to Rock Paper Scissors Game')
print('Loading...')

time.sleep(5) #Simulating the application.

def main():
    user_score = 0
    while True:
        
        values = ['', 'Rock', 'Paper', 'Scissors']

        computer_choice = random.randint(1, 3)

        user_choice = int(input('Enter:\n1 for Rock\n2 for Paper\n3 for Scissors\nEnter your choice: '))

        print('Computer choice: ', values[computer_choice])
        print('Your choice: ', values[user_choice])
        
        if (computer_choice == 1 and user_choice == 2) or (computer_choice == 1 and user_choice == 3) or (computer_choice == 3 and user_choice == 2):
            print('Your score: ', user_score)
            print('You have lost the game.')
            user_score = 0
            print()
            
        elif computer_choice == user_choice:
            print('Match is drawn.')
            print()
        else:
            user_score += 1
            print('Won the game.')
            print()


        app_choice = input('Do you want to play the game again?\nEnter (Yes/No): ').lower()

        if app_choice == 'no':
            print('Thanks for using our application.')
            break
        

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
main()


    


        
