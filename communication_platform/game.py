import random
import time as t


def local_vs(players, humans):
    """
    Simulates a local game.
    players : array
        List of strings, which represents the players
    humans : array
        List of booleans, representing whether players are human or NPC
    """
    if humans[0]:
        tmp = "tmp"  # Make player 1 NPC
    elif humans[1]:
        tmp = "tmp"  # Make player 2 NPC

    print("Simulating local game...")
    t.sleep(2)
    outcome = random.randrange(2)
    if outcome == 1:
        return "DRAW"
    outcome = random.randrange(2)
    if outcome == 1:
        return players[0]
    else:
        return players[1]


def online_vs(name, peer, user, server, play):
    """
    Plays online 1 vs 1 games
    :param name: players name
    :param peer:
    :param user: if player is a user
    :param server: if player is server host
    :param play: Play() class instance
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
        play_game(True, True, user, play, peer)
    else:
        play_game(False, False, user, play, peer)


def play_game(my_turn, first_draw, is_human, play, c):
    while True:
        declare_available_pieces(play)
        declare_board_status(play)
        declare_current_player(play)

        if not my_turn:
            play = c.receive()
            my_turn = True
            declare_available_pieces(play)
            declare_board_status(play)
            declare_current_player(play)

        if my_turn and not first_draw:
            declare_selected_piece(play)
            if is_human:
                while True:
                    try:
                        y, x = input("\nEnter 2 ints 0-3 separated by a space: "). \
                            split()

                        if play.play_placement(y, x):
                            declare_board_status(play)
                            break
                    except:
                        continue
            else:
                play.play_placement()

        if my_turn:
            if is_human:
                while True:
                    pce = input("\nEnter number 0-15 of piece selection: ")

                    if play.play_selection(pce):
                        break
            else:
                play.play_selection()
            if first_draw:
                my_turn = False
                first_draw = False

        declare_selected_piece(play)

        c.send(play)
        my_turn = False

        if play.game.has_won_game(play.selected_piece):
            declare_board_status(play)
            return play.current_player.name
        elif not play.game.has_next_play():
            declare_board_status(play)
            return "DRAW OR??"


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
