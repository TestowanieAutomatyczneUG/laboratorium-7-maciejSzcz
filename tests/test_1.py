from zad1.main import FizzBuzz
import unittest


class TestSimple(unittest.TestCase):
    def test_parametrized_from_file(self):
        f = open('./data/test_zad1', 'r+')
        temp_FizzBuzz = FizzBuzz()

        for line in f:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                values = line.split(" ")
                result, input_val= (values[0], int(values[1].strip("\n")))
                print(result)
                self.assertEqual(temp_FizzBuzz.game(input_val), result)
        f.close()
