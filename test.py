import unittest
from haikuid import HaikuID


class HaikuIDTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_sequence_unique(self):
        haikuID = HaikuID()
        self.assertNotEqual(
            haikuID.generate(),
            haikuID.generate(),
            haikuID.generate()
        )

    def test_return_not_none(self):
        haikuID = HaikuID()
        id = haikuID.generate()
        print(id)
        self.assertIsNotNone(id)


if __name__ == '__main__':
    unittest.main()
