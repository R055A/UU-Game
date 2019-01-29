def game_init():
    n = 4  # n will likely be N, which is a constant and initialized outside of any function/method
    pieces = dict({str(i): bin(i)[2:].zfill(n) for i in range(n * n)}.items())  # pieces will likely be a global
    board = [[None for i in range(n)] for j in range(n)]  # board will likely be a global
    print(pieces)
    print(board)
    board[0][0] = pieces["15"]
    pieces.pop("15")
    print(board)
    print(pieces)


# current_player = players[abs(players.index(current_player) - 1)]  # this could be used for every player turn change
game_init()
