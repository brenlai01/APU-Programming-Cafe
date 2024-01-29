
def login():
    # max_attempts = 3
    # login_attempts = 0

    # while max_attempts > login_attempts:
        # username = input('Enter username: ')
        # password = input('Enter password: ')

        with open('database.txt', 'r') as file:
            lines = file.readlines()
            print(lines)
            file.close()

        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            print(stored_user_type, stored_username, stored_password)
        #     if username == stored_username and password == stored_password:
        #         print(f'\nLogin successful! Welcome, {stored_user_type} {stored_username}.')
        #         if stored_user_type == 'admin':
        #             menu_admin()
        #         elif stored_user_type == 'trainer':
        #             menu_trainer()
        #         elif stored_user_type == 'lecturer':
        #             menu_lecturer()
        #         elif stored_user_type == 'student':
        #             menu_student()
        #         return

        # login_attempts += 1

        # if login_attempts < max_attempts:
        #     print(f'\nLogin failed. Please check your username and password. Attempt {login_attempts} of {max_attempts}.\n')
        # else:
        #     print('\nAccount locked. Too many failed login attempts. Please contact an admin.')
        #     return

def logout():
    print('You have successfully logged out.')
    login()
              
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
        print('\nWhat else would you like to do today?')
        menu_admin()

    elif option == '3':
        assign_levelmodule()
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

def menu_trainer():
    print('you are a trainer.')
    pass
    
def menu_lecturer():
    print('you are a trainer.')
    pass
    
def menu_student():
    print('you are a trainer.')
    pass
    
def register_trainer(): 
    user_type = 'trainer' #ask for user input
    username = input('Trainer username: ')
    password = input('Trainer password: ')
    
    with open('database.txt','r') as file: #open file read by line and makes a list
        lines = file.readlines()
        file.close()
        
    for line in lines:
        stored_user_type, stored_username, stored_password = line.strip().split(':') 
        #split ':' in database.txt & removes any whitespace
        #assigns elements from split(':') e.g. if line = trainer:trainer1:asdasd stored_user_type = trainer, stored_username = trainer1 stored_password = asdasd
        if username == stored_username:
            print(f'\nError: Username "{username}" already exists. Please choose a different username.') #checks if username exists, if exist ask again.
            user_type = 'trainer'
            username = input('Trainer username: ')
            password = input('Trainer password: ')

    with open('database.txt', 'a') as file:
        file.write(f'{user_type}:{username}:{password}\n')
        file.close()
    
    with open('trainer_module.txt','a') as file:
        file.write(f'{user_type}:{username}:level:module\n')
                
    print(f'\n{user_type} {username} registered successfully.')
      
def delete_trainer():
    with open('database.txt','r') as file:
        lines = file.readlines()
        file.close()
    
    username = input('Enter username of trainer you would like to delete: ')

    user_exist = False # check if username exist. Right now this is set to false

    with open('database.txt','w') as file:
        
        for line in lines:
            stored_user_type, stored_username, stored_password = line.strip().split(':')
            
            if username == stored_username and stored_user_type == 'trainer':
                line.rstrip()
                user_exist = True # user exist set to true as username input same as store_username in database
            
            else:
                file.write(line)
    
    with open ('trainer_module.txt','r') as file:
        lines = file.readlines()
        file.close()
        
    with open('trainer_module.txt','w') as file:
        
        for line in lines:
            stored_user_type, stored_username, stored_level, stored_modules = line.strip().split(':')
            
            if username == stored_username and stored_user_type == 'trainer':
                line.rstrip()
                user_exist = True # user exist set to true as username input same as store_username in database
            
            else:
                file.write(line)
    
    if user_exist: #when user_exist is true username deleted
        print(f'Trainer {username} has been deleted.')
    
    else:
        print(f'This trainer does not exist.')
        delete_trainer()

def assign_levelmodule():
    username = input('Enter username of trainer: ')
     
    option = input('''
What level are they teaching? 
1. Beginner
2. Intermediate
3. Advance
Enter a number: ''')
    
    if option == '1':
        level = 'Beginner'
    elif option == '2':
        level = 'Intermediate'
    elif option == '3':
        level = 'Advance'
    else:
        print('Enter a valid number: ')
        assign_levelmodule()
    
    available_modules = ['Python','Java','SQL','C#','C++']
    print(f'Available modules: {available_modules}')

    while True:
        modules_input = input('Enter modules (comma-separated, max 5): ')
        selected_modules = [module.strip() for module in modules_input.split(',')]
    
        if all(module in available_modules for module in selected_modules) and len(selected_modules) <= 5:
            break
        else:
            print('Invalid modules. Please select from the available options.')

    trainer_exist = False

    with open ('trainer_module.txt','r') as file:
        lines = file.readlines()
        file.close()
    
    with open ('trainer_module.txt','w') as file:
        for line in lines:
            stored_user_type, stored_username, stored_level, stored_module = line.strip().split(':')
            
            if username == stored_username and stored_user_type == 'trainer':
                trainer_exist = True
                
                updated_modules = f'trainer:{username}:{level}:{",".join(selected_modules)}\n'
                file.write(updated_modules)
                
            else:
                file.write(line)
                

    if trainer_exist:
        print(f'Trainer {username} has been assigned to teaching {level} {selected_modules}.')
        file.close()
    else:
        print(f'Trainer does not exist.')
        assign_levelmodule()

def view_income():

    username = input('Enter username of trainer: ')
    level_rates = {
        'Beginner': 1.0,
        'Intermediate': 1.5,
        'Advance': 2.0
    }
    module_rate = 100
    
    with open('trainer_module.txt','r') as file:
        lines = file.readlines()
        
    trainer_exist = False

    for line in lines:
        stored_user_type, stored_username, stored_level, stored_module = line.strip().split(':') # assign values from line

        if username == stored_username and stored_user_type == 'trainer':
            modules_num = len([module.strip() for module in stored_module.split(',')])
            trainer_exist = True

            if stored_level in level_rates:
                trainer_income = level_rates[stored_level] * module_rate * modules_num
                print(f'''
Trainer : {username}
Modules : {stored_module}
Level   : {stored_level}
Income  : {trainer_income}''')        
                break
            
            
            
    if not trainer_exist:
        print('Trainer does not exist.')
        view_income()

    
    menu_admin()

    

login()