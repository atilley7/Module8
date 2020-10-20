import unittest
from more_fun_with_collections.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_A(self):
        self.assertEqual('one', switch_average('A'))
        self.assertEqual('one', switch_average('a'))

    def test_B(self):
        self.assertEqual('two', switch_average('B'))
        self.assertEqual('two', switch_average('b'))

    def test_C(self):
        self.assertEqual('three', switch_average('C'))
        self.assertEqual('three', switch_average('c'))

    def test_D(self):
        self.assertEqual('four', switch_average('D'))
        self.assertEqual('four', switch_average('d'))

    def test_E(self):
        self.assertEqual('five', switch_average('E'))
        self.assertEqual('five', switch_average('e'))

    def test_non_key(self):
        self.assertEqual('invalid key', switch_average('z'))


if __name__ == '__main__':
    unittest.main()
