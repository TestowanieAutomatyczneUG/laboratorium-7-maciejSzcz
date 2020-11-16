from zad2.main import ValidPassword
import unittest
from parameterized import parameterized, parameterized_class
from nose.tools import assert_equal

temp = ValidPassword()

@parameterized([
    ("ScalaFavL4nguage!", True),
    ("Pswd1", False),
    ("Haslonowee!", False),
    ("Pswddfsag1", False),
    ("tojestnowehaslo!#", False),
])
def test_validator_outside(input_val, expected):
   assert_equal(temp.validate(input_val), expected)


class TestValidatorInClass(unittest.TestCase):
    @parameterized.expand([
       ("NotAg00dP$$wrd", True),
       ("kot3", False),
       ("mojeDlugiehasloaleniedziala1", False),
       ("WrongPasswordAgain!", False),
       ("gfdsgfdsgdsgdsgsd", False),
    ])
    def test_validator_in_class(self, input_val, expected):
        assert_equal(temp.validate(input_val), expected)
    


@parameterized_class(("input_val", "expected"), [
    ("NotAg00dP$$wrd", True),
    ("kot3", False),
    ("mojeDlugiehasloaleniedziala1", False),
    ("WrongPasswordAgain!", False),
    ("tojestnowehaslo1", False),
])
class TestValidatorFromClass(unittest.TestCase):
    def test_add(self):
        assert_equal(temp.validate(self.input_val), self.expected)
