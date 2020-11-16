from src.zad1.main import ValidPassword
import unittest


class TestSimple(unittest.TestCase):
    def test_parametrized_from_file(self):
        f = open('./data/test_zad1', 'r+')
        temp_password = ValidPassword()

        for line in f:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                values = line.split(" ")
                input_val, result = (values[0], values[1].strip("\n"))
                if result == "True":
                    result = True
                elif result == "False":
                    result = False

                self.assertEqual(temp_password.validate(input_val), result)

        f.close()
