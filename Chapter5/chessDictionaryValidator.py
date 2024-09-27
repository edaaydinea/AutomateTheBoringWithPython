def isValidChessBoard(board):
    # Define valid ranks and files
    valid_squares = {f"{rank}{file}" for rank in range(1, 9) for file in 'abcdefgh'}
    piece_types = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    # Initialize counters
    black_king_count = 0
    white_king_count = 0
    black_pawn_count = 0
    white_pawn_count = 0
    piece_count = {'w': 0, 'b': 0}
    
    # Check each piece on the board
    for position, piece in board.items():
        # Check if the position is valid
        if position not in valid_squares:
            return False
        
        # Check if the piece name is valid
        if not isinstance(piece, str) or len(piece) < 2:
            return False
            
        color = piece[0]
        if color not in {'w', 'b'}:
            return False
        
        # Split piece name to check validity
        if piece[1:] not in piece_types:
            return False
        
        # Count kings and pawns
        if piece == 'bking':
            black_king_count += 1
        elif piece == 'wking':
            white_king_count += 1
        elif piece == 'bpawn':
            black_pawn_count += 1
        elif piece == 'wpawn':
            white_pawn_count += 1
        
        # Count total pieces for each color
        piece_count[color] += 1
    
    # Validate counts
    if black_king_count != 1 or white_king_count != 1:
        return False
    if piece_count['b'] > 16 or piece_count['w'] > 16:
        return False
    if black_pawn_count > 8 or white_pawn_count > 8:
        return False
    
    return True

# Example usage
chess_board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking',
    '2h': 'wpawn'
}

print(isValidChessBoard(chess_board))  # Output: False, as there are two kings
