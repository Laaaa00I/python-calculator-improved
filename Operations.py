import math


class StandardOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self): return self.num1 + self.num2

    def sub(self): return self.num1 - self.num2

    def mul(self): return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            raise ZeroDivisionError("division by zero!")
        return self.num1 / self.num2

    def pow(self):
        if self.num1 == 0 and self.num2 < 0:
            raise ZeroDivisionError("cannot raise 0 to a negative power!")
        try:
            return self.num1 ** self.num2
        except OverflowError:
            raise OverflowError("result is too large!")

    def root(self):
        if self.num2 == 0:
            raise ZeroDivisionError("degree of the root cannot be zero!")
        if self.num1 < 0 and self.num2 % 2 == 0:
            raise ValueError("even root of a negative number!")
        if self.num1 < 0:
            return -math.exp(math.log(abs(self.num1)) / self.num2)
        return math.exp(math.log(self.num1) / self.num2)

class TrigonometricOperations:
    def __init__(self, num): self.num = num

    def sin(self): return math.sin(self.num)

    def cos(self): return math.cos(self.num)

    def tan(self): return math.tan(self.num)

    def cot(self):
        try:
            return 1 / math.tan(self.num)
        except ZeroDivisionError:
            raise ZeroDivisionError("cotangent is undefined!")

    def sec(self):
        cos_val = math.cos(self.num)
        if cos_val == 0:
            raise ZeroDivisionError("secant is undefined for x = π/2 + nπ!")
        return 1 / cos_val

    def cosec(self):
        sin_val = math.sin(self.num)
        if sin_val == 0:
            raise ZeroDivisionError("cosecant is undefined for x = nπ!")
        return 1 / sin_val