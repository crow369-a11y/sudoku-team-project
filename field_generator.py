from random import *

# solution = open("solution.txt", "w", encoding="utf-8")

zero_field = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]


#позволяет обращаяться к стобцу по его номеру. Возвращаяет список значений в столбце
def column (column_ind):
    column_list = [zero_field[0][column_ind], zero_field[1][column_ind], zero_field[2][column_ind],
                   zero_field[3][column_ind], zero_field[4][column_ind], zero_field[5][column_ind],
                   zero_field[6][column_ind], zero_field[7][column_ind], zero_field[8][column_ind]]
    return column_list

#вспомогательная функция для cell. Разбивает ячейки 3х3 по координатам для удобного обращения к ним по индексу, наподобии матрицы.
#Возвращает список значений в ячейке 3х3
def cell_sheet (cell_ind_y, cell_ind_x):
    cell_list = []
    if cell_ind_x == 0 and cell_ind_y == 0:
        cell_list.append(zero_field[0][0])
        cell_list.append(zero_field[0][1])
        cell_list.append(zero_field[0][2])
        cell_list.append(zero_field[1][0])
        cell_list.append(zero_field[1][1])
        cell_list.append(zero_field[1][2])
        cell_list.append(zero_field[2][0])
        cell_list.append(zero_field[2][1])
        cell_list.append(zero_field[2][2])
    elif cell_ind_x == 1 and cell_ind_y == 0:
        cell_list.append(zero_field[0][3])
        cell_list.append(zero_field[0][4])
        cell_list.append(zero_field[0][5])
        cell_list.append(zero_field[1][3])
        cell_list.append(zero_field[1][4])
        cell_list.append(zero_field[1][5])
        cell_list.append(zero_field[2][3])
        cell_list.append(zero_field[2][4])
        cell_list.append(zero_field[2][5])
    elif cell_ind_x == 2 and cell_ind_y == 0:
        cell_list.append(zero_field[0][6])
        cell_list.append(zero_field[0][7])
        cell_list.append(zero_field[0][8])
        cell_list.append(zero_field[1][6])
        cell_list.append(zero_field[1][7])
        cell_list.append(zero_field[1][8])
        cell_list.append(zero_field[2][6])
        cell_list.append(zero_field[2][7])
        cell_list.append(zero_field[2][8])
    elif cell_ind_x == 0 and cell_ind_y == 1:
        cell_list.append(zero_field[3][0])
        cell_list.append(zero_field[3][1])
        cell_list.append(zero_field[3][2])
        cell_list.append(zero_field[4][0])
        cell_list.append(zero_field[4][1])
        cell_list.append(zero_field[4][2])
        cell_list.append(zero_field[5][0])
        cell_list.append(zero_field[5][1])
        cell_list.append(zero_field[5][2])
    elif cell_ind_x == 1 and cell_ind_y == 1:
        cell_list.append(zero_field[3][3])
        cell_list.append(zero_field[3][4])
        cell_list.append(zero_field[3][5])
        cell_list.append(zero_field[4][3])
        cell_list.append(zero_field[4][4])
        cell_list.append(zero_field[4][5])
        cell_list.append(zero_field[5][3])
        cell_list.append(zero_field[5][4])
        cell_list.append(zero_field[5][5])
    elif cell_ind_x == 2 and cell_ind_y == 1:
        cell_list.append(zero_field[3][6])
        cell_list.append(zero_field[3][7])
        cell_list.append(zero_field[3][8])
        cell_list.append(zero_field[4][6])
        cell_list.append(zero_field[4][7])
        cell_list.append(zero_field[4][8])
        cell_list.append(zero_field[5][6])
        cell_list.append(zero_field[5][7])
        cell_list.append(zero_field[5][8])
    elif cell_ind_x == 0 and cell_ind_y == 2:
        cell_list.append(zero_field[6][0])
        cell_list.append(zero_field[6][1])
        cell_list.append(zero_field[6][2])
        cell_list.append(zero_field[7][0])
        cell_list.append(zero_field[7][1])
        cell_list.append(zero_field[7][2])
        cell_list.append(zero_field[8][0])
        cell_list.append(zero_field[8][1])
        cell_list.append(zero_field[8][2])
    elif cell_ind_x == 1 and cell_ind_y == 2:
        cell_list.append(zero_field[6][3])
        cell_list.append(zero_field[6][4])
        cell_list.append(zero_field[6][5])
        cell_list.append(zero_field[7][3])
        cell_list.append(zero_field[7][4])
        cell_list.append(zero_field[7][5])
        cell_list.append(zero_field[8][3])
        cell_list.append(zero_field[8][4])
        cell_list.append(zero_field[8][5])
    elif cell_ind_x == 2 and cell_ind_y == 2:
        cell_list.append(zero_field[6][6])
        cell_list.append(zero_field[6][7])
        cell_list.append(zero_field[6][8])
        cell_list.append(zero_field[7][6])
        cell_list.append(zero_field[7][7])
        cell_list.append(zero_field[7][8])
        cell_list.append(zero_field[8][6])
        cell_list.append(zero_field[8][7])
        cell_list.append(zero_field[8][8])
    else:
        print("cell invalid")
        return None
    return cell_list

#Определяет в какой ячейке 3х3 находится число. Возвращает список значений в этой ячейке 3х3, также как и в cell_sheet
def cell (line, column_id):
    if 0<=line<=2 and 0<=column_id<=2:
        cell_id = cell_sheet(0,0)
    elif 0<=line<=2 and 3<=column_id<=5:
        cell_id = cell_sheet(0,1)
    elif 0<=line<=2 and 6<=column_id<=8:
        cell_id = cell_sheet(0,2)
    elif 3<=line<=5 and 0<=column_id<=2:
        cell_id = cell_sheet(1,0)
    elif 3<=line<=5 and 3<=column_id<=5:
        cell_id = cell_sheet(1,1)
    elif 3<=line<=5 and 6<=column_id<=8:
        cell_id = cell_sheet(1,2)
    elif 6<=line<=8 and 0<=column_id<=2:
        cell_id = cell_sheet(2,0)
    elif 6<=line<=8 and 3<=column_id<=5:
        cell_id = cell_sheet(2,1)
    elif 6<=line<=8 and 6<=column_id<=8:
        cell_id = cell_sheet(2,2)
    else:
        print("cell find failed")
        return None
    return cell_id

#проверяет есть ли уже это число в строке
def line_comp (num, line):
    if num in zero_field[line]:
        return False
    else:
        return True

#проверяет есть ли уже это число в столбце
def column_comp (num, column_ind):
    if num in column(column_ind):
        return False
    else:
        return True

#проверяет есть ли уже это число в ячейку 3х3
def cell_comp (num, line, column_id):
    if num in cell(line, column_id):
        return False
    else:
        return True

# алгоритм генерации собственной персоны
def generate():
    for i in range(len(zero_field)):
        for j in range(len(zero_field[i])):
            gen_flag = True
            num_list = [1,2,3,4,5,6,7,8,9]
            while gen_flag:
                if not num_list:
                    for k in range(len(zero_field)):
                        zero_field[k] = [0,0,0,0,0,0,0,0,0]
                    return generate()
                else:
                    shuffle(num_list)
                    num = num_list[0]

                    if line_comp(num, i) and column_comp(num, j) and cell_comp(num, i, j):
                        # print(zero_field)
                        num_list = [1,2,3,4,5,6,7,8,9]
                        zero_field[i][j] = num
                        gen_flag = False
                    else:
                        num_list.remove(num)

generate()
# print(zero_field)

# for line in zero_field:
#     solution.write(str(line) + "\n")
# solution.close()