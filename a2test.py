# GAURAV AGGARWAL
# 2017288 - A3
# TEST FILE

import unittest
from a2 import validmove,win,takeNaiveMove,takeStrategicMove,validBoard,game,game1,game2,game3,set_variables
import globals

class testpoint(unittest.TestCase):
	def test_game1(self):
		self.assertAlmostEqual(game1(10000),0.58,delta=0.02)
		self.assertAlmostEqual(game1(100000),0.58,delta=0.015)

	def test_game2(self):
		self.assertAlmostEqual(game2(10000),0.006,delta=0.005)
		self.assertAlmostEqual(game2(100000),0.006,delta=0.002)
	
	def test_game3(self):
		self.assertAlmostEqual(game3(10000),0)
		self.assertAlmostEqual(game3(100000),0)
	
	def test_game(self):
		globals.tile1=globals.tile2=globals.tile3=1;globals.tile4=globals.tile8=globals.tile6=2
		self.assertAlmostEqual(game(1),1)
		set_variables()
	
	def test_win(self):
		globals.tile1=globals.tile2=globals.tile3=2
		self.assertTrue(win())
		set_variables()

		globals.tile1=globals.tile2=2; globals.tile3=1
		self.assertFalse(win())
		set_variables()

		globals.tile1=globals.tile2=2; globals.tile3=1
		self.assertFalse(win())
		set_variables()

		self.assertFalse(win())
	
	def test_validBoard(self):
		globals.tile1=2
		self.assertFalse(validBoard())
		set_variables()

		globals.tile1=2; globals.tile7=globals.tile9=1
		self.assertTrue(validBoard())
		set_variables()

	def test_takeNaiveMove(self):
		self.assertTrue(takeNaiveMove())

	def test_takeStrategicMove(self):
		self.assertTrue(takeStrategicMove())

	def test_validmove(self):
		globals.tile1 = 1
		self.assertFalse(validmove(1))
		set_variables()

		self.assertTrue(validmove(7))
		set_variables()
	
if __name__=='__main__':
	unittest.main()
