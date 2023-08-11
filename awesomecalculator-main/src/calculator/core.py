import math
class Calculator:
    def __init__(self):
        pass

    def Add(self, *args):       #modified add function
        return math.sum(args)

    def Substract(self, value1, value2):
        return value1 - value2

    def Multiply(self, value1, value2):
        return value1 * value2

    def Divide(self, value1, value2):
        return value1 / value2
    
    def square_root(self,num):  #added square_root function
        return math.sqrt(num)
    
    def percentage(self, value, percentage): #added percentage function
        return ((value*percentage)/100)
    