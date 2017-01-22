#!/usr/bin/env python

def strip_html(line):
	quote = False
	tag = False
	out = ""
	for c in line:
		if c == '<' and not quote:
			tag = True
		elif c == '>' and not quote:
			tag = False
		elif c == '"' or c == "'" and tag:
			quote = not quote ## invert the value
		elif not tag:
			out = out + c

	return out

def tests():
	print strip_html("<b>Hello</b> Philip!")
	print strip_html('<b>Hello</b> <a href="www.google.com">Philip!</a>')
	print strip_html('<a href=">">Hi "Philly"</a>')

	print strip_html('<b>bold text<b>')
	print strip_html('<b>"bold text"<b>')
	print strip_html('"<b>bold text<b>"')
	print strip_html('<"b">bold text<"b">')

tests()
