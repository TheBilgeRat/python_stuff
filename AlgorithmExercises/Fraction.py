class Fraction:
    """
    Class representing a Fraction.  Add, subtract, multiply and divide are
    provided.  Integer division only.
    """
    def __init__(self, top, bottom):
        """
        Constructor
        :param top: the numerator of the fraction
        :param bottom: the denominator of the fraction
        :return: none
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        """
        override to allow printing of fraction
        :return: string representation of fraction
        """
        return "{0}/{1}".format(self.num, self.den)

    def __add__(self, other):
        """
        override the add method to allow addition of fractions
        :param other: another Fraction
        :return: A Fraction with the products of the addition
        """
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __floordiv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __lt__(self, other):
        """
        less than override for Fraction class
        :param other: Fraction for comparison
        :return: bool
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 < num2

    def __le__(self, other):
        """
        less than or equal override for Fraction class
        :param other: Fraction for comparison
        :return: bool
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 <= num2

    def __eq__(self, other):
        """
        eqality override for Fraction class.  Deep equality
        :param other: Fraction for comparison
        :return: bool
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 == num2

    def __ge__(self, other):
        """
        greater than or equal override for fraction class.
        :param other: Fraction for comparison
        :return: bool
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 >= num2

    def __gt__(self, other):
        """
        greater than override for Fraction class
        :param other: Fraction for comparison
        :return: bool
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 > num2

    def __ne__(self, other):
        """
        not equal comparison for Fraction class.  Deep equality
        :param other: Fraction for comparison
        :return: bool
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 != num2

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

