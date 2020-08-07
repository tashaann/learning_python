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

# bootstrapping, resampling : do an average of averages: plot, central limit theorm
# try to generate a plot 

resamplings_out = 0

bins = int(sys.argv[1])
trials = int(sys.argv[2])
people = int(sys.argv[3])
resamplings = int(sys.argv[4])


# assert statements
assert(trials > 0)
assert(people > 0)
assert(bins > 0)
assert(resamplings > 0)


for resampling in range(resamplings):
	output = 0
	for trial in range(trials):
		birthdays = [0]*bins
		for person in range(people):
			bday = random.randint(0, bins-1)
			#print(bday)
			birthdays[bday] += 1
			if birthdays[bday] > 1:
				output += 1
				break
	resamplings_out += output/trials
print(resamplings_out/resamplings)


"""
python3 birthday.py 365 1000 23

"""

