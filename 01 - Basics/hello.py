# Hello.py is a test of comparisons and flow control

name = ''
password = 'swordfish'


enterName = input('Enter Your Name. (Hint: Mary) ')
enterPassword = input('Enter your password ')


if name == 'Mary':
    print('Hello, Mary')
    if enterPassword == password:
        print('Access Granted')
    else:
        print('Access Denied')
else:
    print("I don't know this name, security notified.")
