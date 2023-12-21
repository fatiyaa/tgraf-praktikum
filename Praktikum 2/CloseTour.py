N = 8
xMove = [2, 1, -1, -2, -2, -1, 1, 2]
yMove = [1, 2, 2, 1, -1, -2, -2, -1]

def isSafe(x, y, sol):
    return 0 <= x < N and 0 <= y < N and sol[x][y] == -1

def printSolution(sol):
    for row in sol:
        print(row)

def findKnightTour(start_row, start_col):
    sol = [[-1 for _ in range(N)] for _ in range(N)]
    sol[start_row][start_col] = 0

    if solveKTUtil(start_row, start_col, 1, sol, xMove, yMove, start_row, start_col):
        print("Knight's Tour found starting from position:", (start_row, start_col))
        printSolution(sol)
    else:
        print("Knight's Tour not found for the given starting position.")

def solveKTUtil(x, y, movei, sol, xMove, yMove, start_row, start_col):
    if movei == N**2 and isClosedMove(x, y, start_row, start_col):
        return True

    next_moves = findWarnsdorffMove(x, y, sol, xMove, yMove)

    for count, k in next_moves:
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        sol[next_x][next_y] = movei
        if solveKTUtil(next_x, next_y, movei + 1, sol, xMove, yMove, start_row, start_col):
            return True
        sol[next_x][next_y] = -1

    return False

def findWarnsdorffMove(x, y, sol, xMove, yMove):
    next_moves = []
    for k in range(8):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        if isSafe(next_x, next_y, sol):
            count = 0
            for i in range(8):
                new_x = next_x + xMove[i]
                new_y = next_y + yMove[i]
                if isSafe(new_x, new_y, sol):
                    count += 1
            next_moves.append((count, k))

    next_moves.sort()
    return next_moves
def isClosedMove(x, y, start_row, start_col):
    return abs(x - start_row) == 2 and abs(y - start_col) == 1 or abs(x - start_row) == 1 and abs(y - start_col) == 2

# Example usage:
findKnightTour(0, 4)
