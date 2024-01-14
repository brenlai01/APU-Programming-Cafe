
def register_user(): 
    user_type = input('User type: ') #ask for user input
    username = input('Username: ')
    password = input('Password: ')
    
    with open('database.txt','r') as file: #open file read by line and makes a list
        lines = file.readlines()
        print(lines)
    for line in lines:
        stored_user_type, stored_username, stored_password = line.strip().split(':') #split ':' in database.txt & removes any whitespace
        # assigns elements from split(':') e.g. if line = trainer:trainer1:asdasd stored_user_type = trainer, stored_username = trainer1 stored_password = asdasd
        if username == stored_username:
            print(f'Error: Username "{username}" already exists. Please choose a different username.') #checks if username exists, if exist ask again.
            user_type = input('User type: ')
            username = input('Username: ')
            password = input('Password: ')

    with open('database.txt', 'a') as file:
        file.write(f'{user_type}:{username}:{password}\n')
                
    print(f'{user_type} {username} registered successfully.')
        
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
                print(f'Login successful! Welcome, {stored_username}.')
                if stored_user_type == 'admin':
                    admin_home()
                elif stored_user_type == 'trainer':
                    trainer_home()
                elif stored_user_type == 'lecturer':
                    lecturer_home()
                elif stored_user_type == 'student':
                    student_home()
                return

        login_attempts += 1

        if login_attempts < max_attempts:
            print(f'Login failed. Please check your username and password. Attempt {login_attempts} of {max_attempts}.')
        else:
            print('Account locked. Too many failed login attempts.')
            return

# login_status, user_type = login('admin1', 'admin123')

# if login_status:
#     print(f'Welcome, {user_type}!')
#     if user_type == 'administrator':
        
#     elif user_type == 'trainer':
       
#     elif user_type == 'lecturer':
        
#     elif user_type == 'student':
        
# else:
#     print('Invalid login attempt.')

# register_user()


def admin_home():
    print('you are admin')
    menu_admin()

def trainer_home():
    print('you are trainer')

def lecturer_home():
    print('you are lecturer')

def student_home():
    print('you are student')
    
def menu_admin(): #menu admin
    option = input('''
Operations:
1. Register/Delete trainer
2. Assign trainer to respective level
3. View monthly income
4. Update profile
Select a number: ''')
    
    if option == '1':
        choice = input('Register/Delete: ')
        if choice == 'Register' or 'register':
            register_user()
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