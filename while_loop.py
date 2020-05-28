num_of_tries=0
while num_of_tries != 3:
    username = input('Please Enter Your Username: ')
    password = input('Please Enter Your Password: ')

    if username == 'Mohamed' and password == 'adp10': # condition
        print('Welcome to our website')
        num_of_tries = 0
        exit()
    else: # else condition
        print('Login Error')
        num_of_tries +=1
        print('you have ' + str(3 - num_of_tries)  + " tries left")