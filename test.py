import unittest
from haikuid import HaikuID


class HaikuIDTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_not_none(self):
        """
        Assert an ID is generated
        """
        client = HaikuID()
        id = client.generate()
        self.assertIsNotNone(id)

    def test_sequence_unique(self):
        """
        Assert a sequence of 3 generated are 
        all unique
        """
        client = HaikuID()
        self.assertNotEqual(
            client.generate(),
            client.generate(),
            client.generate()
        )

    def test_generate_many(self):
        """
        A vanity test to 'see' a variety of 
        IDs being generated
        """
        client = HaikuID()
        for _ in range(10):
            id = client.generate()
            print(id)


if __name__ == '__main__':
    unittest.main()
