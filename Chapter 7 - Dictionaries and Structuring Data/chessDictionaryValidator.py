def isValidChessboard(board):
    """
    Takes a dictionary representing a chessboard and returns True if
    its valid, otherwise returns False
    """

# ------------------- STEP 1: Define what is valid -------------------

# All possible squares on a chessboard: '1a' to '8h'
valid_squares = set()
for rank in range(1,9): # 1 to 8
    for file in 'abcdefgh':
        valid_squares.add(str(rank) + file)

#  Valid piece types (without color)
valid_piece_types = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
# ------------------- STEP 2: Set up counters -------------------
    
white_king = 0
black_king = 0
white_pieces = 0
black_pieces = 0
white_pawns = 0
black_pawns = 0



