import re
import string
import distutils

class ValidPassword:
    def validate(self, password):
        if type(password) != str:
            raise TypeError()
        elif len(password) < 8:
            return False
        elif re.search('[0-9]', password) is None:
            return False
        elif re.search('[A-Z]', password) is None:
            return False
        elif re.search(f'[{string.punctuation}]', password) is None:
            return False
        else:
            return True

if __name__ == "__main__":
    temp = ValidPassword()

    def test_parametrized_from_file():
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
                print(temp_password.validate(input_val) == result)

    test_parametrized_from_file()
    pass
