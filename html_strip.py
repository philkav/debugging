#!/usr/bin/env python

from sys import argv

mode=1
out = []
for i in range(1, len(argv)):
	for c in argv[i]:
		if c == '<':
			mode = 0
		if c == '>':
			mode = 1
			continue
		if mode == 1:
			out.append(c)
	out.append(' ')

print ''.join(out)
