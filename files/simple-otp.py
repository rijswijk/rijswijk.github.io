#!/usr/bin/env python3.6

#
# Simple one-time pad generator
# Copyright (c) 2018 University of Twente
# All Rights Reserved
#
# This software is released into the public domain
# and may be used, modified and copied free of charge
# without warranty of fitness for a particular purpose
#

import sys
import os
import secrets

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#
# Choose the number of entries you want in your
# one-time pad; note, if you pick a number over
# 100, the formatting of the pad may look strange
# so try to pick something reasonable
#
entries = 10

def main():
	print('Generating one-time pad with {} entries'.format(entries))
	print()

	for i in range(1, entries + 1):
		# Step 1: create a set with all letters of the alphabet
		alphaset = set()

		for letter in alphabet:
			alphaset.add(letter)

		# Step 2: randomly pick letters from the set and add them
		#         to our new pad line
		otpline = str()

		while len(alphaset) > 0:
			letter = secrets.choice(list(alphaset))
			
			alphaset.remove(letter)

			otpline += letter

		# Step 3: output the OTP line
		sys.stdout.write('{:02d}'.format(i))

		for letter in alphabet:
			sys.stdout.write(' {}'.format(letter))

		sys.stdout.write('\n') # End the line
		sys.stdout.write('  ') # Indent next line

		for letter in otpline:
			sys.stdout.write(' {}'.format(letter))

		sys.stdout.write('\n') # End the line
		print()

if __name__ == "__main__":
	main()
