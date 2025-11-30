def game_face(puzzle, solution, total_attempts=3):
    """
    Игра Судоку с общим лимитом в 3 попытки на всю игру.
    - При ошибке (неверное число или неверный ввод) — списывается 1 попытка.
    - Если попытки закончились — игра заканчивается немедленно.
    """
    original = [[puzzle[i][j] != 0 for j in range(9)] for i in range(9)]
    attempts_left = total_attempts

    print(" Добро пожаловать в Судоку!")
    print(f"У вас есть {attempts_left} попытки на всю игру.")

    while not is_complete(puzzle) and attempts_left > 0:
        print_board(puzzle)
        try:
            row = int(input("\nСтрока (1-9): ")) - 1
            col = int(input("Столбец (1-9): ")) - 1

            if not (0 <= row < 9 and 0 <= col < 9):
                print("  Введите числа от 1 до 9!")
                attempts_left -= 1
                print(f" Осталось попыток: {attempts_left}")
                continue

            if original[row][col]:
                print("  Эта ячейка дана — её нельзя менять!")
                attempts_left -= 1
                print(f" Осталось попыток: {attempts_left}")
                continue

            if puzzle[row][col] != 0:
                print("  Эта ячейка уже заполнена.")
                attempts_left -= 1
                print(f" Осталось попыток: {attempts_left}")
                continue
            try:
                num = int(input("Число (1-9): "))
                if not (1 <= num <= 9):
                    raise ValueError
            except ValueError:
                print("  Введите число от 1 до 9!")
                attempts_left -= 1
                print(f" Осталось попыток: {attempts_left}")
                continue
            if num == solution[row][col]:
                puzzle[row][col] = num
                print("  Верно!")
            else:
                attempts_left -= 1
                print(f"  Неверно! Это не {num}.")
                print(f" Осталось попыток: {attempts_left}")

        except Exception:
            print("  Ошибка ввода.")
            attempts_left -= 1
            print(f" Осталось попыток: {attempts_left}")

    print("\n" + "="*50)
    if is_complete(puzzle):
        print(" ПОЗДРАВЛЯЕМ! Вы решили Судоку!")
        print_board(puzzle)
    else:
        print(" 💀 ПОПЫТКИ ЗАКОНЧИЛИСЬ. Игра окончена.")
        print(" Правильное решение:")
        print_board(solution)
    print("="*50)
