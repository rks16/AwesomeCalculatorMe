# Awesome Calculator
This is a basic python package project to play around with GitHub Actions, you can check the repository [here](https://github.com/dedreira/awesomecalculator)

1.created a new method inside class called square_root which allows to find the square root of a number.
    import math

class Calculator:
    def square_root(self, num):
        return math.sqrt(num)

# Example usage
calculator = Calculator()
result = calculator.square_root(25)
print(result)  # Output should be 5.0 (square root of 25)

2.created a new method inside class called perecentage which gives us the percentage of a number if when 2 arguements are passed.
    class Calculator:
    def percentage(self, value, percentage):
        return (value * percentage) / 100

# Example usage
calculator = Calculator()
result = calculator.percentage(200, 20)
print(result)  # Output should be 40.0 (20% of 200)

3.modified the add function which could accept more than one arguement and sums them all.
    import math

class Calculator:
    def Add(self, *args):
        return sum(args)

# Example usage
calculator = Calculator()
result = calculator.Add(1, 2, 3, 4, 5)
print(result)  # Output should be 15

