def check_for_zero(filled_board):
    """Check if an empty space exists in the board."""

    for row in filled_board:
        if 0 in row:
            print("False")
            quit()


def check_numbers(list):
    """Check if every number appears only once in list."""

    for i in range(1,10):
        if list.count(i) != 1:
            print("False")
            quit()


def check_box(board, section_start, section_end):
    """Check if every number appears only once in box."""
    
    test_board = []
    check_list = []

    for row in board:
        test_board.append(row[section_start:section_end])

        if len(test_board) == 3:
            for row in test_board:
                for cell in row:
                    check_list.append(cell)
            print(check_list)
            check_numbers(check_list)
            
            check_list.clear()
            test_board.clear()


def validate_sudoku(board):
    """Validating Sudoku Board."""

    check_list = []
    
    # Check if zero appears on board.
    check_board = board
    check_board = check_for_zero(check_board)

    # Check if every number appears only once in a row.
    for row in board:
        for cell in row:
            check_list.append(cell)
        check_numbers(check_list)

        check_list = []

    # Check if every number appears only once in the boxes.
    check_box(board, 0, 3)
    check_box(board, 3, 6)
    check_box(board, 6, 9)


    check_list = []
        
    # Check if every number appears only once in a column.
    for i in range(9):
        for row in board:
            check_list.append(row[i])
        check_numbers(check_list)

        check_list = []

    print("True")


fixed_board = [[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5],
				[5,5,5,5,5,5,5,5,5]]

true_board = [[9,2,6,5,8,3,4,7,1],
			  [7,1,3,4,2,6,9,8,5],
			  [8,4,5,9,7,1,3,6,2],
			  [3,6,2,8,5,7,1,4,9],
			  [4,7,1,2,6,9,5,3,8],
              [5,9,8,3,1,4,7,2,6],
              [6,5,7,1,3,8,2,9,4],
              [2,8,4,7,9,5,6,1,3],
              [1,3,9,6,4,2,8,5,7]]


validate_sudoku(true_board)