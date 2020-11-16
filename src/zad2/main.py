
import re
import string

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
    pass
