board = [
    "X", "O", "X", "O", "X", "O", "X",  # Row 1
    "O", "X", "O", "X", "O", "X", "O",  # Row 2
    "X", "O", "X", "O", "X", "O", "X",  # Row 3
    "O", "X", "O", "X", "O", "X", "O",  # Row 4
    "X", "O", "X", "O", "X", "O", "X",  # Row 5
    "O", "X", "O", "X", "O", "X", "O",  # Row 6
]


def Playable_columns():
    return [i for i in range(7) if any(board[7*n+i] == " " for n in range(6))]

