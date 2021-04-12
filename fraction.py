class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def gcd(self, a, b):
        if b > a:
            a, b = b, a

        while a % b != 0:
            old_a = a
            old_b = b

            a = b
            b = old_a % old_b

        return b

    def __add__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = (new_denominator // self.denominator) * self.numerator + \
                        (new_denominator // other.denominator) * other.numerator

        gcd_val = self.gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // gcd_val, new_denominator // gcd_val)

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False


a = Fraction(1, 25)
b = Fraction(1, 25)
print(a+b)
print(a==b)

