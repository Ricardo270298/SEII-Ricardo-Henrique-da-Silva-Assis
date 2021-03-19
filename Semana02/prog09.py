print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1

import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']


index = my_module.find_index(courses, 'Math')
print(index)

import my_module as mm

index = mm.find_index(courses, 'Math')
print(index)

from my_module import find_index, test

index = find_index(courses, 'Math')
print(index)
print(test)

from my_module import find_index as fi, test

index = fi(courses, 'Math')
print(index)
print(test)

from my_module import *

index = fi(courses, 'Math')
print(index)
print(test)

print(sys.path)



import sys

sys.path.append('Users/coreyschafer/Desktop/My-Modules')

import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choise(courses)

print(random_course)

import math

rads = math.radians(90)

print(math.sin(rads))

import datetime
import calendar

today = datetime.data.today()
print(today)

print(calendar.isleap(2017))


import os

print(os.getcwd())

print (os.__file__)


import webbrowser
import hashlib

webbrowser.open("https://xkcd.com/353/")

def geohash(latitude, longitude, datedow):
	'''Compute geohash() using the Munroe algorithm.
	
	>>>geohash(37.421542,-122.085589, b'2005-05-26-10458.68')
	37.857713 -122.544543

	'''
	# http://xkcd.com/426/
	h = hashlib.md5(datedow).hexdigest()
	p, q = [('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
	print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))

import antigravity




















