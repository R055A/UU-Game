#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from pickle import loads, dumps


class Peer:
    """
    A class which acts as a either a server or client. Only serves to send of
    receive data. Only difference between server and client is that server is
    set up to accept a connection from the client.
    Refactoring/integration editor(s): Adam Ross
    Last-edit-date: 21/03/2019
    """

    HOST = '127.0.0.1'  # local IP address
    PORTS = [65001, 65002]  # port address used for conn
    BUF_SIZ = 4096  # the maximum size for each byte transmission over socket

    def __init__(self, server, tournament=False):
        """
        Class constructor. Sets up connection if player is host
        :param server: Determine whether peer should act as server or client
        """
        self.connection = None  # socket housing remote connection
        self.accept_socket = None  # socket used by server to accept connection
        self.server = server  # Boolean to determine if player is host or not
        self.tournament = tournament  # Boolean for if playing tournament

    def start_server(self):
        """
        Starts the server
        :return: Boolean for if connected successfully or not
        """
        print("Booting server...")

        try:
            # AF_INET = IPv4, SOCK_STREAM = TCP Socket
            self.accept_socket = socket(AF_INET, SOCK_STREAM)

            if self.tournament:
                self.accept_socket.bind((self.HOST, self.PORTS[0]))
            else:
                self.accept_socket.bind((self.HOST, self.PORTS[1]))
            self.accept_socket.listen()
            return True
        except (KeyboardInterrupt, SystemExit, ConnectionRefusedError, OSError):
            print("Failed to boot server")
            return False

    def accept_client(self):
        """
        Accepts client to server
        """
        print("Waiting for incoming connection(s)...")

        try:
            self.connection, _ = self.accept_socket.accept()
            print("Client connected!")

        except (KeyboardInterrupt, SystemExit, ConnectionRefusedError, OSError):
            print("Stopped incoming connection(s)")
            self.accept_socket.close()

    def connect_to_server(self):
        """
        Connect to server as client
        :return: Boolean for if connected successfully or not
        """
        print("Connecting to server...")

        try:
            self.connection = socket(AF_INET, SOCK_STREAM)

            if self.tournament:
                self.connection.connect((self.HOST, self.PORTS[0]))
            else:
                self.connection.connect((self.HOST, self.PORTS[1]))
            print("Connected to server")
            return True
        except (KeyboardInterrupt, SystemExit, ConnectionRefusedError, OSError):
            print("Failed to connect to server")
            self.teardown()
            return False

    def send(self, data):
        """
        Send data over socket. pickle.dumps encodes data as byte stream
        """
        self.connection.sendall(dumps(data))

    def receive(self):
        """
        Receive data from socket. recv() is blocking. pickle.loads preserves data types.
        """
        try:
            data = self.connection.recv(self.BUF_SIZ)
            return loads(data)
        except OSError:
            self.teardown()

    def teardown(self):
        """
        Closes socket or sockets
        """
        try:
            self.connection.close()

            if self.server:
                self.accept_socket.close()
        except (KeyboardInterrupt, SystemExit, AttributeError):
            pass
