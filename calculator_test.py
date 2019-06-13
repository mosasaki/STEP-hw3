import unittest
import calculator


class TestCalculator(unittest.TestCase):
    """Test class of calculator.py"""

    def test_quits_when_invalid_character(self):
        """Testing to see if this the program quits when there are invalid characters in input """

        with self.assertRaises(SystemExit) as cm:
            calculator.tokenize("!3")
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            calculator.tokenize("3+4?")
        self.assertEqual(cm.exception.code, 1)

    def test_addition_should_succeed(self):
        """Testing to see if addition works"""

        test_patterns = ["1", "1+2", "1.0+2"]
        for test in test_patterns:
            tokens = calculator.tokenize(test)
            actualAnswer = calculator.evaluate(tokens)
            expectedAnswer = eval(test)
            self.assertEqual(expectedAnswer, actualAnswer)

    def test_subtraction_should_succeed(self):
        """Testing to see if subtraction works"""

        test_patterns = ["3-1", "3.0-1+2", "5.0+4-3.0"]
        for test in test_patterns:
            tokens = calculator.tokenize(test)
            actualAnswer = calculator.evaluate(tokens)
            expectedAnswer = eval(test)
            self.assertEqual(expectedAnswer, actualAnswer)

    def test_multiply_should_succeed(self):
        """Testing to see if multiplication works"""

        test_patterns = ["3*3", "3*3.0", "2+3*3.0", "2-3*3.0+2"]
        for test in test_patterns:
            tokens = calculator.tokenize(test)
            actualAnswer = calculator.evaluate(tokens)
            expectedAnswer = eval(test)
            self.assertEqual(expectedAnswer, actualAnswer)

    def test_divide_should_succeed(self):
        """Testing to see if division works"""

        test_patterns = ["3/3", "2+3/3", "2+4*6/2.0-3.0", "2+4*6/2.0-6.0/3*2"]
        for test in test_patterns:
            tokens = calculator.tokenize(test)
            actualAnswer = calculator.evaluate(tokens)
            expectedAnswer = eval(test)
            self.assertEqual(expectedAnswer, actualAnswer)

    def test_parentheses_should_succeed(self):
        """Testing to see if parentheses works"""

        test_patterns = ["(1+2)*3", "1+(2*3)", "(1+2.0)/3", "3.0*(2.0+3.0)",
                         "3*(2+3)/3.0", "2+4*6/(6.0-2)/3*2", "(3.0-1)+(4+2.0)/3", "(3.0-1)/2*(4+2.0)/3"]
        for test in test_patterns:
            tokens = calculator.tokenize(test)
            actualAnswer = calculator.evaluate(tokens)
            expectedAnswer = eval(test)
            self.assertEqual(expectedAnswer, actualAnswer)


    def test_parentheses_quits_when_invalid_syntax(self):
        """Testing to see if this the program quits when there are invalid characters in input """

        with self.assertRaises(SystemExit) as cm:
            calculator.evaluate(calculator.tokenize("(((3+"))
        self.assertEqual(cm.exception.code, 1)

        with self.assertRaises(SystemExit) as cm:
            calculator.evaluate(calculator.tokenize("6)(8"))
        self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
