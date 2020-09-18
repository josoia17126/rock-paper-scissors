#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:28:51 2020

@author: apple
"""

import random

default_list = ['paper', 'scissors', 'rock']

player_name = input('Enter your name:')
print('Hello, ' + player_name)
player_score = 0
rating = open('rating.txt', 'r', encoding='utf-8')
for line in rating:
    name, score = line.strip('\n').split()
    if player_name == name:
        player_score = int(score)

rating.close()
list_option = input()
print("Okay, let's start")
if list_option == '':
    options = default_list
else:
    options = list_option.split(',')

while True:
    option = input()
    oc = random.choice(options)
    length = (len(options) - 1) // 2
    doptions = options + options[:]
    number = doptions.index(oc)
    winning_list = doptions[number + 1:number + length + 1]
    losing_list = options[:]
    for i in options:
        if i in winning_list:
            losing_list.remove(i)
    losing_list.remove(oc)
    if option in options:
        if option in losing_list:
            print('Sorry, but the computer chose ' + oc)
        elif option in winning_list:
            print('Well done. The computer chose ' + oc + ' and failed')
            player_score += 100
        elif option == oc:
            print('There is a draw (' + oc + ')')
            player_score += 50
    elif option == '!exit':
        print('Bye!')
        break
    elif option == '!rating':
        print('Your rating: ' + str(player_score))
    else:
        print('Invalid input')
        continue
