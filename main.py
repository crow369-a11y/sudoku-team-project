import sys

sys.setrecursionlimit(3000) # Увеличение лимита рекурсии необходимо для корректной работы рекурсивного решателя судоку на сложных полях.

import copy

import field_generator
import Sudoku_ToMakeHoles_and_Check
import game

field_generator.generate()
game_board = Sudoku_ToMakeHoles_and_Check.remove_numbers(field_generator.zero_field)

game_solution = copy.deepcopy(game_board)

Sudoku_ToMakeHoles_and_Check.solve_and_count(game_solution)

# for row in game_board:
#     print(row)
#
# for row in game_solution:
#     print(row)

game.game_face(game_board, game_solution,3)
