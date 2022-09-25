def animate_drop(board, shape, c):
    long = shape.shape[1]
    for i in len(board):
        board[i][c:c+long] == 0 or shape[i]


    return 0

board = np.array([[4,0,0,0],
                [1,0,0,0],
                [1,0,0,0],
                [1,1,0,0]])

shape = np.array([[2,2,2],
                [2,0,0]])

c = 1