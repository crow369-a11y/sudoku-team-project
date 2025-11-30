
# Шаг 1: Генерируем решение
from game import play_game
from Sudoku_ToMakeHoles_and_Check import remove_numbers
exec(open("main").read())

# Шаг 2: Создаём головоломку

# Читаем solution.txt
solution = []
with open("solution.txt", "r", encoding="utf-8") as f:
    for line in f:
        row = line.strip().replace(
            "[", "").replace("]", "").replace(",", "").split()
        solution.append([int(x) for x in row])

# Делаем головоломку
puzzle = [row[:] for row in solution]  # копия
puzzle = remove_numbers(puzzle, num_to_remove=40)

# Шаг 3: Запускаем игру
play_game(puzzle, solution)
