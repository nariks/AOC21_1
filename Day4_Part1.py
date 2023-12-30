boards = {}
number = 0
BOARD_ROWS = 5
BOARD_COLUMNS = 5


def add_board_lines():
    arr = []
    for i in range(BOARD_ROWS):
        line = file.readline().strip().split()
        arr.append(line)
    return arr, line


with open("input_day4.txt") as file:
    winning_numbers = file.readline().strip().split(",")
    line = file.readline()

    while line:
        number += 1
        boards[number], line = add_board_lines()
        file.readline()

    del boards[number]

drawn_numbers = []
bingo = False


def winning_column(board, drawn_numbers):
    winning_number = -1
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS):
            #print(row, col, board[row][col])
            if board[row][col] not in drawn_numbers:
                break
            if row == BOARD_ROWS - 1:
                return True
    return False


def winning_row(board, drawn_numbers):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] not in drawn_numbers:
                break
            if col == BOARD_COLUMNS - 1:
                return True
    return False

continue_search = True
unmarked_sum = 0

for number in winning_numbers:
    drawn_numbers.append(number)

    if not continue_search:
        break

    for board_number in boards:
        board = boards[board_number]
        winning_board = (winning_row(board, drawn_numbers) or winning_column(board, drawn_numbers))

        if winning_board:
            print(winning_board, board_number)
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLUMNS):
                    if board[row][col] not in drawn_numbers:
                        unmarked_sum += int(board[row][col])

            print(unmarked_sum* int(drawn_numbers[-1]))
            continue_search = False
            break





