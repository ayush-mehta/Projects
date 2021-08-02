import numpy as np


def rotate_2D(board, k):
    board[:] = list(map(list, zip(*board[::-1])))
    k = k - 1
    if k == 0:
        return board
    return rotate_2D(board, k)


def add(cur_board, d, i, l):
    if d == 'right':
        if cur_board[i][l - 1] == cur_board[i][l]:
            cur_board[i][l] = cur_board[i][l] * 2
            cur_board[i][1:l] = cur_board[i][:l - 1]
            cur_board[i][0] = 0
        if l == 1 and i == 3:
            return cur_board
        if l == 1:
            i = i + 1
            l = 4
        return add(cur_board, d, i, l - 1)


def max_val(board, val, k, check):
    val.append(max(board[k]))
    if max(val) == 2048 and check != 1:
        print('You Win!')
        return None
    if max(val) == 2048 and check == 1:
        return 1
    if k == 3:
        return None
    return max_val(board, val, k + 1, check)


def move_2048(cur_board, d):
    check = max_val(cur_board, list(), 0, 1)
    output = main(cur_board, d, 0, 0)
    board = output
    max_val(board, list(), 0, check)
    return output


def main(cur_board, d, i, j):
    if d == 'right':
        if cur_board[i][j + 1] == 0:
            cur_board[i][1:j + 2] = cur_board[i][:j + 1]
            cur_board[i][0] = 0
        if i == 3 and j == 2:
            cur_board = add(cur_board, d, 0, 3)
            return cur_board
        if j == 2:
            i = i + 1
            j = -1
        return main(cur_board, d, i, j + 1)
    if d == 'up':
        cur_board = rotate_2D(cur_board, 1)
        d = 'right'
        cur_board = main(cur_board, d, i, j)
        cur_board = rotate_2D(cur_board, 3)
        return cur_board
    if d == 'left':
        cur_board = rotate_2D(cur_board, 2)
        d = 'right'
        cur_board = main(cur_board, d, i, j)
        cur_board = rotate_2D(cur_board, 2)
        return cur_board
    if d == 'down':
        cur_board = rotate_2D(cur_board, 3)
        d = 'right'
        cur_board = main(cur_board, d, i, j)
        cur_board = rotate_2D(cur_board, 1)
        return cur_board


cur_board = [[2, 2, 4, 8], [1024, 1024, 0, 0], [16, 4, 4, 2], [0, 2, 2, 2]]
d = 'left'
print(np.array(cur_board), '\n')
# output = main(cur_board, d, 0, 0)
output = move_2048(cur_board, d)
print(np.array(output))
