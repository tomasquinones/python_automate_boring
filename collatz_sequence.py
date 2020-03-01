# Automate the Boring Stuff - Collatz Sequence

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(str(number))
        else:
            number = (3 * number) + 1 
            print(str(number))

mynumber = input("Enter an integer: ")
mynumber = int(mynumber)

print(collatz(mynumber))