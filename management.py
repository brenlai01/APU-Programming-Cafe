
def register_trainer(): 
    user_type = 'trainer' #ask for user input
    username = input('Username: ')
    password = input('Password: ')
    
    with open('database.txt','r') as file: #open file read by line and makes a list
        lines = file.readlines()
        file.close()
        
    for line in lines:
        stored_user_type, stored_username, stored_password = line.strip().split(':') 
        #split ':' in database.txt & removes any whitespace
        # assigns elements from split(':') e.g. if line = trainer:trainer1:asdasd stored_user_type = trainer, stored_username = trainer1 stored_password = asdasd
        if username == stored_username:
            print(f'\nError: Username "{username}" already exists. Please choose a different username.') #checks if username exists, if exist ask again.
            user_type = 'trainer'
            username = input('Username: ')
            password = input('Password: ')

    with open('database.txt', 'a') as file:
        file.write(f'{user_type}:{username}:{password}\n')
        file.close()
                
    print(f'\n{user_type} {username} registered successfully.')

# def delete_trainer():
#     username = input('Enter the username of the trainer you would like to delete: ')
    
#     with open('database.txt','r') as file:
#         lines = file.readlines()
#         file.close()
    
#     with open('database.txt','w'):
#     for line in lines:
#         stored_user_type, stored_username, stored_password = line.strip().split(':')
#         # print(stored_user_type, stored_username, stored_password)
#         if username == stored_username:
#             line.lstrip()



    


        
def login():
    max_attempts = 3
    login_attempts = 0

    while max_attempts > login_attempts:
        username = input('Enter username: ')
        password = input('Enter password: ')

        with open('database.txt', 'r') as file:
            lines = file.readlines()
            file.close()

        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            if username == stored_username and password == stored_password:
                print(f'\nLogin successful! Welcome, {stored_user_type} {stored_username}.')
                if stored_user_type == 'admin':
                    menu_admin()
                elif stored_user_type == 'trainer':
                    menu_trainer()
                elif stored_user_type == 'lecturer':
                    menu_lecturer()
                elif stored_user_type == 'student':
                    menu_student()
                return

        login_attempts += 1

        if login_attempts < max_attempts:
            print(f'\nLogin failed. Please check your username and password. Attempt {login_attempts} of {max_attempts}.\n')
        else:
            print('\nAccount locked. Too many failed login attempts. Please contact an admin.')
            return
    
def menu_admin(): #menu admin
    option = input('''
Operations:
1. Register trainer
2. Delete trainer
3. Assign trainer to respective level
4. View monthly income
5. Update profile
6. Logout
Select a number: ''')
    
    if option == '1':
        register_trainer()
        print('\nWhat else would you like to do today?')
        menu_admin()
            
    elif option == '2':
        delete_trainer()
        menu_admin()

    elif option == '3':
        assign_level()
        menu_admin()

    elif option == '4':
        view_income()
        menu_admin()
    
    elif option == '5':
        update_profile()
        menu_admin()

    elif option == '6':
        logout()
    
    else:
        print('Please enter a valid number')
        menu_admin()
def logout():
    print('You have successfully logged out.')
    return

<<<<<<< Updated upstream
login()
print(123)
=======
def menu_trainer():
    print('you are a trainer.')
login()
    
# delete_trainer()
>>>>>>> Stashed changes
