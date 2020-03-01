# Magic 8 ball, refactored to use a list instead of a ton of if and elif

import random
import time

def whatIsMyFortune():
    fortunes = ['Nope',
                'No way',
                'Not going to happen',
                'Nuh-uh',
                'I do not think so',
                'Mmmmm, no',
                'Negatory',
                'Negative',
                'That would be a big fat "No"',
                'What is the opposite of Yes?']
    r = random.randint(1,len(fortunes))
    return fortunes[r]

question = input("What is your question?")

print(f"You asked: {question}, but your answer is...")

time.sleep(2)

print(f"...{whatIsMyFortune()}...sorry")