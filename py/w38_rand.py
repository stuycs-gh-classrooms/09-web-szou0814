#!/usr/bin/python
print('Content-type: text/html/n')

import random
n = random.randrange(100)
print('Hello World! Let us play a game.')
print('''\n''')
print('I am thinking of a number from 1 to 100. Take a guess!')
print('=' * 50)
print(n, 'is the correct answer! Did you guess it right? Play again!')
