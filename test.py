from specs.helpers import *
from src.amount_reader import AmountReader
import unittest, random


class AmountReaderTest(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        self.am = AmountReader()
        super().__init__(methodName)

    def test_100(self):
        self.assertEqual(self.am.t3(100), "một trăm")

    def test_000(self):
        self.assertEqual(self.am.t3(000), "")

    def test_401_and_411(self):
        self.assertEqual(self.am.t3(401), "bốn trăm lẻ một")
        self.assertEqual(self.am.t3(411), "bốn trăm mười một")

    def test_15(self):
        self.assertEqual(self.am.t3(15), "mười lăm")

    def test_94(self):
        self.assertEqual(self.am.t3(94), "chín mươi tư")

    def test_25(self):
        self.assertEqual(self.am.t3(25), "hai mươi lăm")
    def test_4(self):
        self.assertEqual(self.am.t3(4), "bốn")

    def test_over_3_character(self):
        with self.assertRaises(ValueError):
            self.am.t3(random.randint(1000,9999))

if __name__ == "__main__":
    unittest.main()
