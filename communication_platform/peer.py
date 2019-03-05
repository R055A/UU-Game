#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM
from pickle import loads, dumps


class Peer:
    """
    A class which acts as a either a server or client. Only serves to send of
    receive data. Only difference between server and client is that server is
    set up to accept a connection from the client.
    Refactoring/integration editor(s): Adam Ross
    Last-edit-date: 04/03/2019
    """

    HOST = '127.0.0.1'  # local IP address
    PORT = 65001  # port address being used for connection
    BUF_SIZ = 4096  # the maximum size for each byte transmission over socket
    TIME_OUT = 60  # the maximum time (s) a socket will listen for a connection

    def __init__(self, server):
        """
        Class constructor. Sets up connection if player is host
        :param server: Determine whether peer should act as server or client
        """
        self.connection = None  # socket housing remote connection
        self.accept_socket = None  # socket used by server to accept connection
        self.server = server  # Boolean to determine if player is host or not

        if self.server:
            try:
                print("Booting server")
                # AF_INET = IPv4, SOCK_STREAM = TCP Socket
                self.accept_socket = socket(AF_INET, SOCK_STREAM)
                self.accept_socket.bind((self.HOST, self.PORT))
                # self.accept_socket.settimeout(self.TIME_OUT)
                self.accept_socket.listen()
            except (KeyboardInterrupt, SystemExit):
                print("\nShutting down server")

    def accept_client(self):
        """
        Accepts client as server.
        """
        print("Waiting for incoming connection...")
        try:
            self.connection, _ = self.accept_socket.accept()
            print("Client connected!")

        except KeyboardInterrupt:
            print("\nStopped incoming connections")
            self.accept_socket.close()

    def connect_to_server(self):
        """
        Connect to server as client
        """
        print("Connecting to server...")
        self.connection = socket(AF_INET, SOCK_STREAM)
        self.connection.connect((self.HOST, self.PORT))
        print("Connected to server")

    def send(self, data):
        """
        Send data over socket. pickle.dumps encodes data as byte stream
        """
        self.connection.sendall(dumps(data))

    def receive(self):
        """
        Receive data from socket. recv() is blocking. pickle.loads preserves data types.
        """
        data = self.connection.recv(self.BUF_SIZ)
        return loads(data)

    def teardown(self):
        """
        Closes socket or sockets
        """
        self.connection.close()

        if self.server:
            self.accept_socket.close()
