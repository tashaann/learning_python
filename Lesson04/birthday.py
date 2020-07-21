#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it
# We will have a variable number of bins (can be months or days)
# And some number of trials for the simulation
# And some number of people whose have random birthdays
# Use assert() to check parameters
# On the command line:
#	python3 birthday.py <bins> <trials> <people>
import random 
import sys

output = 0
trials = int(sys.argv[2])
people = int(sys.argv[3])
bins = int(sys.argv[1])

for trial in range(trials):
	birthdays = {} 
	for person in range(people):
		bday = random.randint(1, bins+1)
		if(bday in birthdays):
			output += 1
			break
		else:
			birthdays[bday] = person
	
print(output/trials)

"""
python3 birthday.py 365 1000 23

"""
