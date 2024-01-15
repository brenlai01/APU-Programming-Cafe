
def register_trainer(): 
    user_type = 'trainer' #ask for user input
    username = input('Username: ')
    password = input('Password: ')
    
    with open('database.txt','r') as file: #open file read by line and makes a list
        lines = file.readlines()
        
    for line in lines:
        stored_user_type, stored_username, stored_password = line.strip().split(':') 
        #split ':' in database.txt & removes any whitespace
        # assigns elements from split(':') e.g. if line = trainer:trainer1:asdasd stored_user_type = trainer, stored_username = trainer1 stored_password = asdasd
        if username == stored_username:
            print(f'Error: Username "{username}" already exists. Please choose a different username.') #checks if username exists, if exist ask again.
            user_type = 'trainer'
            username = input('Username: ')
            password = input('Password: ')

    with open('database.txt', 'a') as file:
        file.write(f'{user_type}:{username}:{password}\n')
                
    print(f'{user_type} {username} registered successfully.')

# def delete_trainer():
#     username = input('Enter the username of the trainer you would like to delete: ')
    
#     with open('database.exe','r') as file:
#         lines = file.readlines()
    
#     for line in lines:
#         stored_user_type, stored_username, stored_password = line.strip().split(':')
    
#         if username != stored_username:
#             print(f'Error: Username does not exist. Please choose another username.')
#             username = input('Enter the username of the trainer you would like to delete: ')
    
#         elif username == stored_username:
#             choice = input(f'Are you sure you want to delete trainer {username}?Y/N: ')
#             if choice == 'Y' or 'y':
#                 with open('database.txt','w') as file


        
def login():
    max_attempts = 3
    login_attempts = 0

    while max_attempts > login_attempts:
        username = input('Enter username: ')
        password = input('Enter password: ')

        with open('database.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            if username == stored_username and password == stored_password:
                print(f'Login successful! Welcome, {stored_user_type} {stored_username}.')
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
            print(f'Login failed. Please check your username and password. Attempt {login_attempts} of {max_attempts}.')
        else:
            print('Account locked. Too many failed login attempts. Please contact an admin.')
            return
    
def menu_admin(): #menu admin
    option = input('''
Operations:
1. Register/Delete trainer
2. Assign trainer to respective level
3. View monthly income
4. Update profile
Select a number: ''')
    
    if option == '1':
        choice = input('Register/Delete trainer: ')
        if choice == 'Register' or 'register':
            register_trainer()
            print('\nWhat else would you like to do today?')
            menu_admin()
        elif choice == 'Delete' or 'delete':
            delete_trainer()

    elif option == '2':
        assign_level()

    elif option == '3':
        monthly_inc()

    elif option == '4':
        update_profile()
    
    else:
        print('Please enter a valid number')
        menu_admin()

login()