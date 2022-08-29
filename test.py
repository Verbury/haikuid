import unittest
from haikuid import HaikuID


class HaikuIDTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_not_none(self):
        """
        Assert an ID is generated
        """
        haikuid = HaikuID()
        id = haikuid.generate()
        self.assertIsNotNone(id)

    def test_sequence_unique(self):
        """
        Assert a generated sequence are 
        all unique
        """
        haikuid = HaikuID()
        self.assertNotEqual(
            haikuid.generate(),
            haikuid.generate(),
            haikuid.generate(),
        )

    def test_generate_many(self):
        """
        Vanity test to 'see' a variety of 
        IDs being generated
        """
        haikuid = HaikuID()
        for _ in range(10):
            id = haikuid.generate()
            print(id)


if __name__ == '__main__':
    unittest.main()
