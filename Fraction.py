class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print("{0}/{1}".format(self.num, self.den))

    def __str__(self):
        return "{0}/{1}".format(self.num, self.den)

