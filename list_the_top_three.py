# -*- coding: utf-8 -*-
# Target: Find the top 3 numbers in the file
# Time complexity: O(n)

# Read the file line by line, and always only keep the top 3 max numbers while reading lines.
# Run command as: python list_the_top_three.py sample1.dat

import sys

sample_data = sys.argv[1]

input_file = open(sample_data, 'r')
current_top_three = [-1, -1, -1]

for line in open(sample_data):
	element = int(input_file.readline())
	if (element > current_top_three[0]):
		if (element > current_top_three[1]):
			if (element > current_top_three[2]):
				current_top_three[0] = current_top_three[1]
				current_top_three[1] = current_top_three[2]
				current_top_three[2] = element
			else:
				current_top_three[0] = current_top_three[1]
				current_top_three[1] = element
		else:
			current_top_three[0] = element
	
print ('Top Three: ')
for element in reversed(current_top_three):
	print element