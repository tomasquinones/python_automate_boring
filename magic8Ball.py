# Automate the Boring Stuff - Chapter 3 - Magic 8 Ball

import random 

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'YES'
    elif answerNumber == 4:
        return 'Reply Hazy Try Again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubful'
    
r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
