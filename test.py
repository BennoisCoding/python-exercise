board = [[1,7,3,2,6,8,9,5,4],
		 [4,2,5,1,9,3,7,6,8],
		 [8,6,9,7,4,5,1,2,3],
		 [6,1,2,8,3,7,4,9,5],
		 [3,9,8,4,5,6,2,1,7],
		 [5,4,7,9,1,2,3,8,6],
		 [9,5,4,3,8,1,6,7,2],
		 [2,3,6,5,7,9,8,4,1],
		 [7,8,1,6,2,4,5,3,9]]

test_board = []
check_list = []

def check_box(board, section, section1):
    """"""
    test_board = []
    check_list = []

    for row in board:
        test_board.append(row[section:section1])

        if len(test_board) == 3:
            for row in test_board:
                for cell in row:
                    check_list.append(cell)
            print(check_list)
            # testen
            check_list.clear()
            test_board.clear()



check_box(board,0 , 3)


#print(test_board[3:6])
