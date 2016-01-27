#!/usr/bin/python
# -*-coding:utf-8 -*

def enum(*sequential, **named):
	"""
	une façon de definir des enum en python.
	Merci à Alec Thomas de StackOverflow pour la solution
	--> http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
	USAGE :
	Numbers = enum('ZERO', 'ONE', 'TWO')
	Numbers.ZERO
	Numbers.ONE
	"""
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)
#end enum
