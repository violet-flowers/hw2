from unittest.mock import patch, call   
from unittest import TestCase
from conway_life_modular import *
import unittest

class CreateTests(TestCase):
    def test_blinker(self):
        initial_game = [['*','O','*'],
                ['*','O','*'],
                ['*','O','*']]
        next_game = update_grid(initial_game)
        assert next_game == [['*','*','*'],
                ['O','O','O'],
                ['*','*','*']]
        next_game = update_grid(next_game)
        assert next_game == initial_game

        #print("test passed")
if __name__=="__main__":
    unittest.main()