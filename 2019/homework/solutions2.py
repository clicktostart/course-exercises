#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sergio Mathurin'
__copyright__ = 'Copyright (C) 2019, Click to Start'
__credits__ = ['Sergio Mathurin']
__license__ = 'MIT'
__version__ = '0.0.1'

# Enter your name in this variable
name = 'Mentor'
print('This is the homework #1 for {}'.format(name))


# Question 1
# Create a function to called 'Hello'. This function takes no parameters/input
# and prints 'Hello There' to the screen.

def hello():
    print("Hello There")


# Question 2
# Create a function to called 'HelloThereName'. This function takes one parameters/input
# called name. It prints 'Hello There _______ ' to the screen where the blank is replaced
# by the name entered.

def hello_there_name(name):
    print("Hello There {}".format(name))


# Question 3
# Create a function call 'RectArea' that takes in two parameters/inputs called
# length and width. This function returns the calculated area of a rectangle using the
# length and width provided.
# Area of a rectangle = length * width

def rect_area(length, width):
    return length * width


# Question 4
# What value does the following function return. Print that value?
#
# def func1():
#   num1 = 36
#   num2 = 4
#   num3 = 10
#   prod = num1 * num2 * num3
#   prod = prod/2
#   return num2
#   prod2 = prod * 4
#   div = prod2/8
#   return div

print(4)


# Question 5
# What do the following function calls print to the screen? Print your answers.
#
# def HeyThere(first_name, last_name):
#   print("Hey There, my name is {} {}. I'm very famous, maybe you've heard of me.".format(first_name, last_name))
#
# HeyThere("Jeff", "Johns")
# HeyThere("Clarke, "Kent")
# HeyThere("Bruce", "Wayne")
# HeyThere("Wally", "West")

print("Hey There, my name is Jeff Johns. I'm very famous, maybe you've heard of me.")
print("Hey There, my name is Clarke Kent. I'm very famous, maybe you've heard of me.")
print("Hey There, my name is Bruce Wayne. I'm very famous, maybe you've heard of me.")
print("Hey There, my name is Wally West. I'm very famous, maybe you've heard of me.")
