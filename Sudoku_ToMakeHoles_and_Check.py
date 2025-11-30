# Ф-я проверки можно ли поместить число в ячейку
def is_valid(board, row, col, num):
    # Проверяем строку
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Проверяем 3x3 блок
    br, bc = (row // 3) * 3, (col // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == num:
                return False
    return True

# Ф-я подсчета кол-ва решений судоку
def solve_and_count(board):
    count = [0] # Счетчик решений
    def solve(): # Внутренняя ф-я для решения судоку - метод backtracking
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0: # Если ячейка пустая
                    for num in range(1, 10):
                        if is_valid(board, i, j, num): # Если число можно поставить
                            board[i][j] = num # Ставим число
                            if solve(): # Рекурсивно продолжаем
                                return True
                            board[i][j] = 0  # Если не получилось откатываем 
                    return False # Если не нашли подходящее число возвращаем False
        # Если дошли до конца  нашли одно решение
        count[0] += 1
        return True
    
    solve()
    return count[0]

# Ф-я удаления чисел из судоку и проверки на только одно решение
def remove_numbers(board, num_to_remove=40): #Здесь можно поменять кол-во удаленных цифр изменением num_to_remove=
    positions = [(i, j) for i in range(9) for j in range(9)] # Список всех позиций в судоку
    # Перемешиваем позиции случайным образом
    import random
    random.shuffle(positions)
    removed = 0 # Счетчик удаленных чисел

    for row, col in positions: # Проходим по всем позициям
        if removed >= num_to_remove: # Если уже удалили нужное кол-во чисел, выходим
            break
        if board[row][col] != 0: # Если ячейка не пустая
            backup = board[row][col] # Сохраняем значение
            board[row][col] = 0 # Удаляем число (ставим 0)
            board_copy = [r[:] for r in board]  # Создаем копию доски для проверки
            if solve_and_count(board_copy) == 1: # Проверяем, сколько решений у новой доски
                removed += 1 
            else: # Если больше одного решения, восстанавливаем число
                board[row][col] = backup
    # Возвращаем измененную доску
    return board


# Пример на готовой доске
# sudoku = [
#     [5,3,4,6,7,8,9,1,2],
#     [6,7,2,1,9,5,3,4,8],
#     [1,9,8,3,4,2,5,6,7],
#     [8,5,9,7,6,1,4,2,3],
#     [4,2,6,8,5,3,7,9,1],
#     [7,1,3,9,2,4,8,5,6],
#     [9,6,1,5,3,7,2,8,4],
#     [2,8,7,4,1,9,6,3,5],
#     [3,4,5,2,8,6,1,7,9]
# ]

# Удаляем 40 чисел и проверяем, что остается только одно решение
# puzzle = remove_numbers(sudoku, num_to_remove=40)
#
# for row in puzzle:
#     print(row)