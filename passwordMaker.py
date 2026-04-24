import string,random


while True:
    lenght = int(input('Please enter your preferred password length : '))
    chars = string.ascii_letters + string.digits + '!@#$%^()-+&*~'

    password = ''.join([random.choice(chars) for i in range(lenght)])

    print('Your Password : {}'.format(password))

    answer = input('Do you want another password (Y/N)? ').lower()
    if answer == 'n':
        break
