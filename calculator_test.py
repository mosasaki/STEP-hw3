import unittest
import calculator


class TestCalculator(unittest.TestCase):
    """Test class of calculator.py"""

    def test(self):
        """Testing to see if this calculator program works"""

        test_patterns = ["1", "1+2", "1.0+2", "1.0+2.1-3",
                         "3*3", "3*3.0", "2+3*3.0", "2-3*3.0+2",
                         "3/3", "2+3/3", "2+4*6/2.0-3.0", "2+4*6/2.0-6.0/3*2",
                         "(1+2)*3", "1+(2*3)", "(1+2.0)/3", "3.0*(2.0+3.0)",
                         "3*(2+3)/3.0", "2+4*6/(6.0-2)/3*2", "(3.0-1)+(4+2.0)/3", "(3.0-1)/2*(4+2.0)/3"]
        for test in test_patterns:
            tokens = calculator.tokenize(test)
            actualAnswer = calculator.evaluate(tokens)
            expectedAnswer = eval(test)
            self.assertEqual(expectedAnswer, actualAnswer)


if __name__ == '__main__':
    unittest.main()
