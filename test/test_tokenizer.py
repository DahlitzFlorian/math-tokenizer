import unittest

from tokenizer.tokenizer import tokenize


class TestTokenizer(unittest.TestCase):
    """
    Tests the correct behaviour of the tokenizer
    """
    def test_tokenizer_one_in_row(self):
        """
        Checks scenario when only one of each type
        is in a row (e.g. not two literals behind each
        other)
        """
        # sample function
        function = "2x^2+4x-3"

        # tokenize
        result = tokenize(function)
        expected_result = {
            0 : ("Literal", "2"),
            1 : ("Variable", "x"),
            2 : ("Operator", "^"),
            3 : ("Literal", "2"),
            4 : ("Operator", "+"),
            5 : ("Literal", "4"),
            6 : ("Variable", "x"),
            7 : ("Operator", "-"),
            8 : ("Literal", "3")
        }

        # check
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
