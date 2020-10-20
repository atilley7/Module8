import unittest
from more_fun_with_collections.set_membership import in_set


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        set_one = {1, 2, 3}
        search_var = 1
        self.assertEqual(in_set(set_one, search_var), True)

    def test_in_set_false(self):
        set_one = {1, 2, 3}
        search_var = 0
        self.assertEqual(in_set(set_one, search_var), False)


if __name__ == '__main__':
    unittest.main()
