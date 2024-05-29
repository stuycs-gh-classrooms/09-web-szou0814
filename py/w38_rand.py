#!/usr/bin/python
print('Content-type: text/html\n')

import random
ans = random.randrange(100)
n1 = random.randrange(100)
n2 = random.randrange(100)

print('Hello World! Let us play a game.')
print('<br>' * 2)
print('I am thinking of a number from 1 to 100. Take a guess!')
print('<br>')
print('<br>', ans,'</b>', 'is the correct answer! Did you guess it right? +2 if you did!')
print('<br>' * 2)
print('Here is a list of runner up answers:')
print('<ul><li>', n1, '</li><li>', n2, '</li></ul>')
print('<br>')
print('+1 if you guessed any of them right!')
print('<br>' * 2)
print('Let us play again!')
