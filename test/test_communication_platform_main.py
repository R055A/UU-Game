from unittest import TestCase
from communication_platform.main import CommunicationPlatform


class TestCommunicationPlatform(TestCase):
    """
    Tests the CommunicationPlatform class
    Author(s): Adam Ross
    Date: 28/02/19
    """

    def test_communication_platform_main(self):
        """
        Tests CommunicationPlatform class instance
        """
        test = CommunicationPlatform()
        self.assertTrue(isinstance(test, CommunicationPlatform))
