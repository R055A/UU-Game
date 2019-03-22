#!/usr/bin/env python3

from unittest import TestCase
from communication_platform.peer import Peer


class TestPeer(TestCase):
    """
    Tests the Peer class
    Author(s): Adam Ross
    Date: 22/03/19
    """

    def test_communication_platform_peer(self):
        """
        Tests Peer class instance
        """
        test = Peer(True)
        self.assertTrue(isinstance(test, Peer))

    def test_start_server_tournament_server_available(self):
        """
        Test can start a tournament server when tournament server not yet started
        """
        test = Peer(True, True)
        self.assertTrue(test.start_server())
        test.teardown()

    def test_start_server_tournament_server_unavailable(self):
        """
        Test cant start a tournament server when tournament server already started
        """
        test = Peer(True, True)
        self.assertTrue(test.start_server())
        second_server_attempt = Peer(True, True)
        self.assertFalse(second_server_attempt.start_server())
        self.assertFalse(second_server_attempt.start_server())
        self.assertFalse(second_server_attempt.start_server())
        test.teardown()
        second_server_attempt.teardown()

    def test_start_server_singles_server_available(self):
        """
        Test can start a singles server when singles server not yet started
        """
        test = Peer(True)
        self.assertTrue(test.start_server())
        test.teardown()

    def test_start_server_singles_server_unavailable(self):
        """
        Test cant start a singles server when singles server already started
        """
        test = Peer(True)
        self.assertTrue(test.start_server())
        second_server_attempt = Peer(True)
        self.assertFalse(second_server_attempt.start_server())
        self.assertFalse(second_server_attempt.start_server())
        self.assertFalse(second_server_attempt.start_server())
        test.teardown()
        second_server_attempt.teardown()

    def test_start_server_singles_when_tournament_and_available(self):
        """
        Tests singles server is successful when tournament server is running
        """
        test = Peer(True, True)
        self.assertTrue(test.start_server())
        singles_test = Peer(True)
        self.assertTrue(singles_test.start_server())
        test.teardown()
        singles_test.teardown()

    def test_start_server_tournament_when_singles_and_available(self):
        """
        Tests tournament server is successful when singles server is running
        """
        test = Peer(True)
        self.assertTrue(test.start_server())
        tournament_test = Peer(True, True)
        self.assertTrue(tournament_test.start_server())
        test.teardown()
        tournament_test.teardown()

    def test_client_connect_unavailable_server_tournament(self):
        """
        Tests a client connecting to unavailable tournament server fails
        """
        test = Peer(False, True)
        self.assertFalse(test.connect_to_server())
        self.assertFalse(test.connect_to_server())
        self.assertFalse(test.connect_to_server())
        test.teardown()

    def test_client_connect_unavailable_server_singles(self):
        """
        Tests a client connecting to unavailable singles server fails
        """
        test = Peer(False)
        self.assertFalse(test.connect_to_server())
        self.assertFalse(test.connect_to_server())
        self.assertFalse(test.connect_to_server())
        test.teardown()
