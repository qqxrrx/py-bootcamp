import unittest
from activities import eat, nap, is_funny, laugh


# >>> py tests.py
# (verbose) = >>> py tests.py -v


class ActivityTests(unittest.TestCase):
    def test_eat_heathy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat("broccoli"),
            "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_unheathy(self):
        """eat should have a negative message for unhealthy eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )

    # testing for error
    def test_eat_healthy_boolean(self):
        """is_healthy must be boolean"""
        with self.assertRaises(ValueError):
            eat("pizza", is_healthy="wow")

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I didn't mean to nap for 3 hours!"
        )

    def test_is_funny_tim(self):
        # this is better rather than do falsey
        self.assertEqual(is_funny("tim"), False)

        # testing for falsey value (None is falsey)
        # self.assertFalse(is_funny("tim"), "tim should not be funny")

    def test_is_funny_anyone_else(self):
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")

    def test_laugh(self):
        # random within
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))


if __name__ == "__main__":
    unittest.main()
