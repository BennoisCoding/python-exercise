#def update_adjacent(board, row, col):
#    """Update adjacent cells to None when there are 4 same values in a row."""

#    chk_value = board[row][col]

    # Check horizontally
    #for i in range 


def check_additional(board, row, value):
    """If there is a 4 combo checking if there are more same values touching the combo."""

    chk_value = row[value]
    pos_list = []

    for i, row_0 in enumerate(board):
        for j, cell in enumerate(row_0):
            if row_0[j] == chk_value:
                pos_list.append((i, j))
                row_0[j] = None

    #for pos in pos_list:
    #    update_adjacent(board, pos[0], pos[1])


def check_column(board, section_0, section_1):
    """Checking if values match in a column."""

    check_list = []
    del_chk = False

    # add to check_list
    for row in board:
        for i, cell in enumerate(row[section_0:section_1]):
            check_list.append(cell)
            
            # check if first values are the same
            if len(check_list) == 4:
                chk = True
                for value in check_list:
                    if value != check_list[0]:
                        chk = False
                
                if chk == False:
                    del check_list[0]
                    del_chk = True

    # Check if more than 4 values are the same in the column.
    if chk == True and del_chk == False:
        if check_list[-1] != check_list[-2]:
            # Also check row before creating empty spaces in the column.
            for row in board:
                row = check_row(board, row)
            for row in board[0:4]:
                for i, cell in enumerate(row[section_0:section_1]):
                    row[section_0] = None
        else:
            # Also check row before creating empty spaces in the column.
            for row in board:
                row = check_row(board, row)
            for row in board:
                for i, cell in enumerate(row[section_0:section_1]):
                    row[section_0] = None

    # When chk == True and del_chk == True create empty spaces for the last 4 values in the column.
    if chk == True and del_chk == True:
            # Also check row before creating empty spaces in the column.
            for row in board:
                row = check_row(board, row)
            for row in board[1:5]:
                for i, cell in enumerate(row[section_0:section_1]):
                    row[section_0] = None

    # When chk == False check if there is a combo in the rows.
    if chk == False:
        for row in board:
            row = check_row(board, row)


def check_row(board, row):
    """Checking if values match in a row."""

    chk = True

    # check first 4 candies.
    for cell in row[0:3]:
        if cell != row[0]:
            chk = False
    
    # if 4 in a row check if more are in a row and make empty spaces.
    if chk == True:
        if row[3] != row[4]:
            for i, cell in enumerate(row[0:4]):
                row[i] = None
        else:
            check_additional(board, row, 0)
            for i, cell in enumerate(row):
                row[i] = None
    
    # check next 4 candies.
    for cell in row[1:5]:
        if cell != row[1]:
            chk = False

    # if chk == True make empty spaces of last five values in the row.
    if chk == True:
        for i, cell in enumerate(row[1:5]):
            row[i] = None


def candy_crush(board):
    """Playing Candy Crush."""

    # Check 4 combo in each column.
    check_column(board, 0, 1)
    #check_column(board, 1, 2)
    #check_column(board, 2, 3)
    #check_column(board, 3, 4)
    #check_column(board, 4, 5)

    print("\n")
    for row in board:
        print(row)


game_board = [["Red", "Red", "Red", "Red", "Red"],
              ["Blue", "Red", "Blue", "Red", "Blue"],
              ["Blue", "Red", "Red", "Red", "Yellow"],
              ["Blue", "Yellow", "Red", "Blue", "Yellow"],
              ["Red", "Yellow", "Blue", "Red", "Yellow"],]

candy_crush(game_board)