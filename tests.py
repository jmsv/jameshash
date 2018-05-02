import unittest

from jameshash import hash_password, check_password, merge_lists, largest_prime_factor


class CheckHashes(unittest.TestCase):
    def test_hash_password(self):
        """
        Checks hashes are as expected for password/username input
        """
        self.assertEqual(
            hash_password("password", "username"),
            "b30d9fd9f52f296bab0177fd47d703c9cf693317d5a93103053769c12983c54d"
        )
        self.assertEqual(
            hash_password("password1", "username"),
            "2bd9330169c79d27d3815f99030bc35d8bf5af8375e1a5d73103e1fd25abb941"
        )
        self.assertEqual(
            hash_password("password2", "username"),
            "4b9dd391a16bb5b3f7092bc94b4fe711d7855373596df9d38debe53df5430949"
        )

    def test_check_password(self):
        """
        Checks password/username/hash checker returns correct True/False
        """
        # Check True is returned for correct password/username/hash
        self.assertTrue(check_password(
            "Avocad0", "jmsv_",
            "59c36135b1472d471b0563bd07893d09912fbdf3093d6ded7f77cf436f4b9b43")
        )

        # Check False is returned for wrong password/username/hash
        self.assertFalse(check_password(
            "guessed password", "jmsv_",
            "59c36135b1472d471b0563bd07893d09912fbdf3093d6ded7f77cf436f4b9b43")
        )
        self.assertFalse(check_password(
            "Avocad0", "guessed username",
            "59c36135b1472d471b0563bd07893d09912fbdf3093d6ded7f77cf436f4b9b43")
        )

    def test_merge_lists(self):
        """
        Test method to merge to lists together in format:
        [1, 2, 3, 4, 5, 6] & ['a', 'b', 'c']
        => [1, 'a', 2, 'b', 3, 'c', 4, 5, 6]
        """
        self.assertEqual(
            merge_lists([1, 2, 3, 4, 5], ['a', 'b', 'c']),
            [1, 'a', 2, 'b', 3, 'c', 4, 5]
        )
        self.assertEqual(
            merge_lists(['a', 'b', 'c', 'd', 'e'], ['x', 'y', 'z']),
            ['a', 'x', 'b', 'y', 'c', 'z', 'd', 'e']
        )

    def test_largest_prime_factor(self):
        """
        Test method that calculates a numbers largest prime factor
        :return:
        """
        self.assertEqual(largest_prime_factor(35), 7)
        # High-value test cases from:
        # http://www.javascripter.net/math/calculators/primefactorscalculator.htm
        self.assertEqual(largest_prime_factor(39865), 67)
        self.assertEqual(largest_prime_factor(9007199254740991), 20394401)
        self.assertEqual(largest_prime_factor(9007199254740993), 28059810762433)


if __name__ == '__main__':
    unittest.main()
