print('Welcome all who view this to where all my projects will be done')
print('\n Now we start project 1')
# USER INPUT

# PASSWORD STRENGTH CHECKER
# NAME INPUT
print('\n Please fill out to check password strength')
while True:
    Name = input(' Your name: ')
    if not Name.isalpha():
        print('invalid input')
    else:
        break

# E-MAIL INPUT
while True:
    Email = input('\n email: ')
    if '@gmail.com' not in Email.lower():
        print('invalid input, only google accounts are accepted')
    elif not Email.lower():
        print('Cannot be left empty')
    else:
        break

# DATE OF BIRTH INPUT
while True:
    Date_of_birth = input('\n Enter date of birth in (DD/MM/YY): ')
    parts = Date_of_birth.split('/')
    if len(parts) == 3 or not all(part.isdigit() for part in parts):
        print(' Error must be in 0/0/0 format')
    elif not Date_of_birth:
        print('Cannot be left empty')
    else:
        break

# PASSWORD INPUT
while True:
    password = input('\n password: ')
    common_passwords = ['1234qwerty', 'password11',
                        'qwerty', 'abcd1234', '00000000']
    if len(password) < 8:
        print('Cannot be less than 8 characters')
    elif password.isalpha() or password.isdigit():
        print(' too weak, must contain alphabets, numbers and symbols')
    elif Name not in password:
        print('Error,  name must be part of password')
    elif password in common_passwords:
        print(' password to common')
    else:
        print('password is ok ')
        break
