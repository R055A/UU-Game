from os import system
from game_engine.player_human import PlayerHuman


# def local_vs(players, humans):
#     """
#     Simulates a local game.
#     players : array
#         List of strings, which represents the players
#     humans : array
#         List of booleans, representing whether players are human or NPC
#     """
#     if humans[0]:
#         tmp = "tmp"  # Make player 1 NPC
#     elif humans[1]:
#         tmp = "tmp"  # Make player 2 NPC
#
#     print("Simulating local game...")
#     t.sleep(2)
#     outcome = random.randrange(2)
#     if outcome == 1:
#         return "DRAW"
#     outcome = random.randrange(2)
#     if outcome == 1:
#         return players[0]
#     else:
#         return players[1]


def online_vs(name, peer, user, server, play, auto):
    """
    Plays online 1 vs 1 games
    :param name: players name
    :param peer: network connection
    :param user: if player is a user
    :param server: if player is server host
    :param play: Play() class instance
    :param auto: Boolean for if game is automated or not
    """
    if server:
        if play.current_player == name:
            starting_player = True
            peer.send("WAIT")
            peer.receive()
        else:
            starting_player = False
            peer.send("START")
            peer.receive()
    else:
        ack = peer.receive()

        if ack == "WAIT":
            starting_player = False
            peer.send("ACK")
        else:
            starting_player = True
            peer.send("ACK")

    if starting_player:
        return play_game(True, True, user, play, peer, auto)
    else:
        return play_game(False, True, user, play, peer, auto)


def play_game(my_turn, first_draw, is_human, play, c, auto):
    while True:
        if not auto:
            declare_pieces_and_board(play)

        if not my_turn:
            if first_draw and not auto:
                print("\nWait for opponent to pass a piece")
            elif not auto:
                print("\nWait for opponent to place the piece")
            play = c.receive()

            if not auto:
                declare_pieces_and_board(play)

            if play.game.has_won_game(play.selected_piece):
                return play.current_player.name
            elif not play.game.has_next_play():
                return "DRAW"

            if not first_draw:
                if not auto:
                    print("\nWait for opponent to pass a piece")
                play = c.receive()

                if not auto:
                    declare_pieces_and_board(play)
            first_draw = False
            my_turn = True

        if not first_draw:
            place(is_human, play, auto)
            c.send(play)

            if play.game.has_won_game(play.selected_piece):
                return play.current_player.name
            elif not play.game.has_next_play():
                return "DRAW"
        choose(is_human, play)

        if not auto:
            declare_selected_piece(play)

        if first_draw:
            my_turn = False
            first_draw = False
        c.send(play)
        my_turn = False


def place(is_human, play, auto):
    if not auto:
        declare_selected_piece(play)

    if is_human:
        while True:
            y, x = input("\nEnter 2 ints 0-3 separated by a space: "). \
                split()

            if play.play_placement(y, x):
                declare_pieces_and_board(play)
                break
    else:
        play.play_placement()


def choose(is_human, play):
    if is_human:
        while True:
            pce = input("\nEnter number 0-15 of piece selection: ")

            if play.play_selection(pce):
                break
    else:
        play.play_selection()


def declare_pieces_and_board(play):
    system('clear')
    declare_available_pieces(play)
    declare_board_status(play)
    declare_current_player(play)


def declare_available_pieces(play):
    """
    Declares to the players the pieces available for selection
    Temporary for the CLI testing
    """
    print("\nGame pieces status:")
    print(list(play.game.pieces.items())[:int((len(play.game.
                                                   pieces) + 1) / 2)])

    if len(play.game.pieces) > 1:
        print(list(play.game.pieces.
                   items())[int((len(play.game.pieces) + 1) / 2):])


def declare_board_status(play):
    """
    Declares to the players the current status of the game board
    Temporary for the CLI testing
    """
    print("\nGame board status:")
    print(*(row for row in play.game.board), sep="\n")


def declare_selected_piece(play):
    """
    Temporary printing of selected piece for CLI testing and presenting
    """
    print("\nCurrent piece: " + play.selected_piece)


def declare_current_player(play):
    """
    Temporary printing of current player for CLI testing and presenting
    """
    print("\nCurrent player: '" + play.current_player.name + "'")


def play_manual(play):
    """
    Plays manual game between either player vs player or player vs AI game
    :return: the winner's name or None for a draw
    """
    start = True

    while True:
        if start:
            declare_current_player(play)
            start = False
        declare_available_pieces(play)  # prints game board status
        declare_board_status(play)  # prints available pieces status

        if isinstance(play.current_player, PlayerHuman):
            while True:
                pce = input("\nEnter number 0-15 of piece selection: ")

                if play.play_selection(pce):
                    break
        else:
            play.play_selection()
        declare_selected_piece(play)  # prints the selected piece
        declare_current_player(play)  # prints the current player turn

        if isinstance(play.current_player, PlayerHuman):
            while True:
                try:
                    y, x = input("\nEnter 2 ints 0-3 separated by a space: ").\
                        split()

                    if play.play_placement(y, x):
                        break
                except:
                    continue
        else:
            play.play_placement()

        if play.game.has_won_game(play.selected_piece):
            declare_board_status(play)  # prints final status of board
            return play.current_player.name
        elif not play.game.has_next_play():  # checks if turns remaining
            declare_board_status(play)  # prints final status of board
            return None
