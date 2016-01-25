#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.modele.Contrainte import *

class Test_Contrainte(unittest.TestCase):
	def test_nothing(self):
		test = Contrainte()
		#self.assertEqual(test.do_shit(), 8)
		


if __name__ == "__main__":
	unittest.main()
