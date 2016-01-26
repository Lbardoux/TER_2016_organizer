#!/usr/bin/python
# -*-coding:utf-8 -*
import unittest
import sys
sys.path.insert(0, "../src")

from src.pyconstraints_1_0_1.pyconstraints.problem import Problem

class Test_PyConstraint(unittest.TestCase):
	"""
	Les tests pour la prise en main de la lib pyConstraint
	@author: Laurent Bardoux p1108365
	"""
	
	def test_priseEnMain(self):
		"""
		Premier essai
		"""
		p = Problem()
		p.add_variable("x", range(4))
		p.add_variable("y", range(4))
		p.add_constraint(lambda z : z%2 == 0, ["x"])
		p.add_constraint(lambda a, b : a != b, ["x", "y"])
		
		resultats = p.iter_solutions().next()
		self.assertTrue(resultats["x"]%2 == 0)
		self.assertTrue(resultats["x"] != resultats["y"])
	#fin test_priseEnMain
	
	def test_echec(self):
		"""
		Que se passe-t-il si les contraintes sont trop restrictives ?
		"""
		p = Problem()
		p.add_variable("x", [0])
		p.add_variable("y", [0])
		p.add_constraint(lambda x, y : x != y, ["x", "y"])
		with self.assertRaises(StopIteration):
			p.iter_solutions().next()
	#fin test_echec
	
#fin Test_PyConstraint


if __name__ == "__main__":
	unittest.main()
#fin if
