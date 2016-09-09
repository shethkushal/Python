# nqueens.py : Solve the N-Queens problem!
# D. Crandall, August 2016
#
# The N-rooks problem is: Given an empty NxN chessboard, place N queens on the board so that no queens
# can take any other, i.e. such that no two queens share the same row or column or diagonal.

# This is N, the size of the board.

# EDITED VERSION
# Edited By Kushal Sheth (kmsheth@iu.edu)
# This program solves n-rooks and n-queens (n=8) problem and also shows the time taken for the execution [in seconds]

import time
# Change value of N
N = 4

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )

# Check for the queens in respective diagonals
def count_on_diag(board, row, col):
    r = row
    c = col
    while r > 0 and c > 0:
        r -= 1
        c -= 1
        if board[r][c] == 1:
            return False
    r = row
    c = col
    while r < N-1 and c > 0 :
        r += 1
        c -= 1
        if board[r][c] == 1:
            return False
    r = row
    c = col
    while r <N-1  and c < N-1:
        r += 1
        c += 1
        if board[r][c] == 1:
            return False
    r = row
    c = col
    while r > 0 and c < N-1:
        r -= 1
        c += 1
        if board[r][c] == 1:
            return False

    return True

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
   return "\n".join([ " ".join([ "Q" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1, ] + board[row][col + 1:]] + board[row + 1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

# Successor function for n-rooks (QUESTION 3)
def successors2(board):
    new_state = []
    for c in range(0, N):
        for r in range (0, N):
            state = add_piece(board, r, c)
            if  board[r][c] != 1 and count_pieces(board) < N:
                new_state.append(state)
    return new_state

# Successor function for n-rooks (QUESTION 4)
def successors3(board):
    # new_state = []
    # for c in range(0, N):
    #     for r in range(0, N):
    #         state = add_piece(board, r, c)
    #         if board[r][c] != 1 and count_on_row(board, r) <1 and count_on_col(board,c) <1:
    #             new_state.append(state)
    new_state = [add_piece(board, r, c) for c in range(0, N) for r in range(0,N) if count_on_row(board, r) <1 and count_on_col(board,c) <1]
    return new_state

# Successor function for n-queeens
def nqueens_successors(board):
    new_state = [add_piece(board, r, c) for c in range(0, N) for r in range(0, N) if
                 count_on_row(board, r) < 1 and count_on_col(board, c) < 1 and count_on_diag(board, r, c)]
    return new_state

# check if board is a goal state for n-rooks
def is_goal(board):
    return count_pieces(board) == N and \
        all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
        all([count_on_col(board, c) <= 1 for c in range(0, N)])

# check if board is a goal state for n-queens
def nqueens_is_goal(board):
    return count_pieces(board) == N

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors3( fringe.pop() ):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# Solve n-queens!
def nqueens_solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in nqueens_successors( fringe.pop() ):
            if nqueens_is_goal(s):
                return(s)
            fringe.append(s)
    return False

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
state_list = []

# Printing initial empty board
print "Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n"
start = time.time()

#Printing solution for n-rooks
print "Solution for (N) = ", N,"Rooks"
solution = solve(initial_board)
print time.time() - start
print printable_board(solution) if solution else "Sorry, no solution found. :("

print "  "

#Printing solution for n-queens
print "Solution for (N) = ", N,"Queens"
solution_nqueens = nqueens_solve(initial_board)
print time.time() - start
print printable_board(solution_nqueens) if solution_nqueens else "Sorry, no solution found. :("
