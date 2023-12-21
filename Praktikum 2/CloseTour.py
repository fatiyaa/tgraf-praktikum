# ukuran board
N = 8

# Knight movement
xMove = [2, 1, -1, -2, -2, -1, 1, 2]
yMove = [1, 2, 2, 1, -1, -2, -2, -1]

# Memeriksa apakah move yang diambil benar (melihat ukuran board, dan petak yang dituju)
def isSafe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Mencetak hasil
def printSolution(board):
    for row in board:
        print(row)

# algoritma untuk menemukan close tour
def findKnightTour(start_row, start_col):
    # mengisi semua board dengan -1 mengindikasi belum dikunjungi
    board = [[-1 for _ in range(N)] for _ in range(N)]
    
    # mengisi petak start 
    board[start_row][start_col] = 1

    # solving 
    if solveKTUtil(start_row, start_col, 1, board, xMove, yMove, start_row, start_col):
        print("Knight's Tour found starting from position:", (start_row, start_col))
        printSolution(board)
    else:
        print("Knight's Tour not found for the given starting position.")

# solving problem
def solveKTUtil(x, y, movei, board, xMove, yMove, start_row, start_col):
    
    # memeriksa closed
    if movei == N**2 and isClosedMove(x, y, start_row, start_col):
        return True

    # menemukan next move
    next_moves = findPossibleMoves(x, y, board, xMove, yMove)

    # menemukan langkah selanjutnya (rekursif)
    for count, k in next_moves:
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        board[next_x][next_y] = movei+1
        if solveKTUtil(next_x, next_y, movei + 1, board, xMove, yMove, start_row, start_col):
            return True
        board[next_x][next_y] = -1

    return False

# menemukan movement yang mungkin di ambil
def findPossibleMoves(x, y, board, xMove, yMove):
    next_moves = []
    
    # perulangan untuk mengecek semua kemungkinan pergerakan 
    for k in range(8):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        if isSafe(next_x, next_y, board):
            count = 0
            for i in range(8):
                new_x = next_x + xMove[i]
                new_y = next_y + yMove[i]
                if isSafe(new_x, new_y, board):
                    count += 1
            next_moves.append((count, k))

    next_moves.sort()
    return next_moves

# Apakah rute yang dilakukan merupakan closed tour
def isClosedMove(x, y, start_row, start_col):
    return abs(x - start_row) == 2 and abs(y - start_col) == 1 or abs(x - start_row) == 1 and abs(y - start_col) == 2

# Example usage, start dapat diubah sesuai yang diinginkan
findKnightTour(0, 3)
