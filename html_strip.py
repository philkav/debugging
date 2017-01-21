#!/usr/bin/env python

def strip_html(line):
	mode = 1
	out = ""
	for c in line:
		if c == '<':
			mode = 0
		elif c == '>':
			mode = 1
		elif mode == 1:
			out = out + c

	return out

print strip_html("<b>Hello</b> Philip!")
print strip_html('<b>Hello</b> <a href="www.google.com">Philip!</a>')
