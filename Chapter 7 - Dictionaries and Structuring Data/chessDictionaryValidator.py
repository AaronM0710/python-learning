def isValidChessBoard(board):
    # Generate all valid chess squares like 'a1', 'h8'
    valid_squares = set()
    for rank in range(1, 9):
        for file in 'abcdefgh':
            valid_squares.add(file + str(rank))

    # All allowed pieces (book uses short notation)
    valid_pieces = {'wK', 'wQ', 'wR', 'wB', 'wN', 'wP',
                    'bK', 'bQ', 'bR', 'bB', 'bN', 'bP'}

    white_king = 0
    black_king = 0
    white_pieces = 0
    black_pieces = 0
    white_pawns = 0
    black_pawns = 0

    for square, piece in board.items():
        if square not in valid_squares:
            return False
        if piece not in valid_pieces:
            return False

        # Count kings
        if piece == 'wK':
            white_king += 1
        elif piece == 'bK':
            black_king += 1

        # Count total pieces and pawns
        if piece[0] == 'w':
            white_pieces += 1
            if piece[1] == 'P':
                white_pawns += 1
        else:
            black_pieces += 1
            if piece[1] == 'P':
                black_pawns += 1

    # Final validation
    if white_king != 1 or black_king != 1:
        return False
    if white_pieces > 16 or black_pieces > 16:
        return False
    if white_pawns > 8 or black_pawns > 8:
        return False

    return True


board = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
print(isValidChessBoard(board))   # Should print True