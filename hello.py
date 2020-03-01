# Hello.py is a test of comparisons and flow control

name = 'Mary'
password = 'swordfish'

enterPassword = input('Enter your password')

if name == 'Mary':
    print('Hello, Mary')
    if enterPassword == password:
        print('Access Granted')
    else:
        print('Access Denied')

