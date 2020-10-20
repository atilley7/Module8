import unittest
from more_fun_with_collections.dict_membership import in_dict


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'A'), True)

    def test_in_dict_false(self):
        self.assertEqual(in_dict({'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, 'Z'), False)


if __name__ == '__main__':
    unittest.main()
