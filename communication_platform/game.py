import sys
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


def online_vs(nick, c, human, server, play):
    """
    Simulates an online game
    nick : string
        String representing local player's name
    c : Peer
        Class Peer, connection with remote player
    human : Boolean
        True = Human player, False = NPC player
    server : Boolean
        Whether this player acts as server or not. Needed in order to properly synchronize peers

    Notes
    -----
    This is an example of how to use the Peer to communicate. Was used for testing \
    the communication platform
    """
    starting_player = None
    if not human:
        tmp = "tmp"  # Make this player NPC

    t.sleep(2)
    # Decide starting player
    if server:
        i = random.randint(0, 1)
        if i == 1:
            starting_player = True
            c.send("WAIT")
            c.receive()
        else:
            starting_player = False
            c.send("START")
            c.receive()
    else:
        ack = c.receive()
        if ack == "WAIT":
            starting_player = False
            c.send("ACK")
        else:
            starting_player = True
            c.send("ACK")

    if starting_player:
        play_game(True, True, human, play, c)
    else:
        play_game(False, False, human, play, c)


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
                        y, x = input("\nEnter 2 ints 0-3 separated by a space: ").\
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
