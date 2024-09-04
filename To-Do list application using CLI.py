'''To do lists '''

#Importing necessary modules.

import time

to_do_list = dict()

#Prints to-do list for all dates.
def printtodoList():
    for to_do in to_do_list:
        print(to_do, ":", end = '\n')
        print("Tasks: ", to_do_list[to_do][0], end ='\n')
        print("Status: ", to_do_list[to_do][1], end = '\n')


#Prints to-do list for the given date.
def printtodoListfordate(Date):
    
    print(to_do_list[Date])

#To-do lists creation for the given date if not exists already.
def create(date):

    item_list = list(input('Enter the items seperated by a comma and a space: ').split(', '))

    status_list = ['Not finished' for i in range(len(item_list))]

    to_do_list [date] = [item_list, status_list]

#To-do list item updation.
def update(update_date):
    
    printtodoListfordate(update_date)
    update_item = int(input('Enter the item number to be updated: '))
    item_content = input('Enter the content to be replaced: ')
    to_do_list[update_date][0].pop(update_item - 1)
    to_do_list[update_date][0].insert(update_item, item_content)

#To-do list deletion for the specified date.
def delete(delete_date):
    
    to_do_list [delete_date].clear()
    print('To do list for the date ', delete_date, ' is deleted sucessfully.')

#Function for to-do list status tracking for the given date.
def track_status(Date):
    
    print('Status of the to_do_list')
    printtodoListfordate(Date)

#To-do list item status updating function.
def update_status(Date):
    update_task_status = int(input("Enter the item's number to be updated: "))
    to_do_list[Date][1][update_task_status-1] = 'Finished'


#Driver code
print('Welcome to To-do application')
print('Loading...')
time.sleep(3)

#Check if the to-do lists is already available on the given date.
#Infinite loop to simulate the feel of an application.
while True:
    date = input("Enter the date in the format(DD/MM/YYYY) format: ")
    for i in to_do_list:
        if i == date:
            print('To do list is already created.', end = '\n')
            printtodoListfordate(i)
        
            print("Do you wish to update or delete your to-do list?")
            choice = int(input("Enter the number 1 to Update or 2 to Delete or 3 to Track or 4 to Update status of task or 5 to Print the to-do list: "))

            if choice == 1:
                update(i)
            elif choice == 2:
                delete(i)
            elif choice == 3:
                track_status(i)
            elif choice == 4:
                update_status(i)
            elif choice == 5:
                printtodoList()

    else:
        print('Want to create a to-do list?')

        choice1 = int(input("Enter 1 for Yes 2 for No: "))
        if choice1 == 1:
            if date not in to_do_list:
                create(date)
        else:
            pass
        
    print('Do you want to continue?')

    app_choice = input("Enter Yes or yes to Continue else Enter No or no: ").lower()

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
                        
                            
        

