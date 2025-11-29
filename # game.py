# game.py
from utils import print_board, is_complete


def play_game(puzzle, solution):
    # Маска исходных чисел
    original = [[puzzle[i][j] != 0 for j in range(9)] for i in range(9)]

    print(" Добро пожаловать в Судоку!")
    print("У вас есть 3 попытки на каждую ячейку.")

    while not is_complete(puzzle):
        print_board(puzzle)
        try:
            row = int(input("\nСтрока (1-9): ")) - 1
            col = int(input("Столбец (1-9): ")) - 1

            if not (0 <= row < 9 and 0 <= col < 9):
                print(" Введите числа от 1 до 9!")
                continue
            if original[row][col]:
                print(" Эта ячейка дана — её нельзя менять!")
                continue
            if puzzle[row][col] != 0:
                print(" Эта ячейка уже заполнена.")
                continue

            # 3 попытки
            for attempt in range(3, 0, -1):
                try:
                    num = int(input(f"Число (1-9) ({attempt} попыток): "))
                    if not (1 <= num <= 9):
                        raise ValueError

                    if num == solution[row][col]:
                        puzzle[row][col] = num
                        print(" Верно!")
                        break
                    else:
                        if attempt > 1:
                            print(" Неверно. Попробуйте снова.")
                        else:
                            correct = solution[row][col]
                            puzzle[row][col] = correct
                            print(
                                f"💀 Попытки закончились. Правильный ответ: {correct}")
                except ValueError:
                    if attempt > 1:
                        print(" Введите число от 1 до 9!")
                    else:
                        correct = solution[row][col]
                        puzzle[row][col] = correct
                        print(
                            f"💀 Попытки закончились. Правильный ответ: {correct}")
        except ValueError:
            print(" Неверный формат ввода.")

    print("\n Поздравляем! Вы решили Судоку!")
    print_board(puzzle)
