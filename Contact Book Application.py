''' Contact Book Application '''

import time

print('Welcome to our application')
print('Loading...')

time.sleep(3)

contact_book = dict()

def add_contact():
    name = input("Enter name: ").lower().capitalize()
    address = input("Enter address: ")
    email = input("Enter email address: ").lower()
    phone_number = input("Enter phone number: ")
    contact_book [name] = [phone_number, email, address]
    
def display_contact():
    print('Name\t\tPhone no.\t\tEmail Address\t\t\tResidential address')
    for name in contact_book:
        print(name, '\t', contact_book[name][0], '\t', contact_book[name][1], '\t', contact_book[name][2], end = '\n')

def search_contact(key = None):
    if key is None:
        key = input('Enter the name to search contact details: ').lower().capitalize()
    
    if key in contact_book:
        print('Name\t\tPhone no.\t\tEmail Address\t\t\tResidential address')
        print(key, '\t', contact_book[key][0], '\t', contact_book[key][1], '\t', contact_book[key][2], end = '\n')
    else:
        print('The contact is not found.')
        return -1
        
def update_contact():
    key = input('Enter the name of contact to be updated: ').lower().capitalize()
    if search_contact(key) == -1:
        print ('Name doesn\'t exists')
        return None
    
    field = int(input('Enter the field number to be updated\n1. Name\n2. Phone no.\n3. Email\n4. Address\n'))
    if field == 1:
        name = input('Enter the name replaced: ').lower().capitalize()
        contact_book[name] = contact_book.pop(key)
        
    elif field == 2:
        phone = input('Enter the phone number replaced: ')
        contact_book[key][0] = phone
        
    elif field == 3:
        email = input('Enter the mail id  replaced: ').lower()
        contact_book[key][1] = email
        
    elif field == 4:
        address = input('Enter the address: ')
        contact_book[key][2] = address
    
    else:
        print('Invalid choice.')
        
def delete_contact():
    name = input('Enter the name of the contact to be deleted: ').lower().capitalize()
    if name in contact_book:
        contact_book.pop(name)
        print('The contact has been deleted.')
        
    else:
        print('Contact doesn\'t exists')
        
while True:
    print("Select:\n1. Add a new contact\n2. View contact list\n3. Search a contact\n4. Update a contact\n5. Delete a contact")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_contact()
    elif choice == 2:
        display_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    else:
        print('Enter a valid choice.')
    
    print('Do you want to perform any other operation?')
    
    option = input("Enter (Yes/No): ").lower()
    if option == 'no':
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
