class FizzBuzz:
    def game(self, num):

        if type(num) != int:
            raise Exception("Not a valid number")
        if ((num % 15) == 0):
            return "FizzBuzz"
        elif ((num % 3) == 0):
            return "Fizz"
        elif ((num % 5) == 0):
            return "Buzz"
        else:
            raise Exception("Error in FizzBuzz")


if __name__ == "__main__":
    pass