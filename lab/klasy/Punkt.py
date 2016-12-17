import math


class Wektor:
    def __init__(self, x=0, y=0):
        self.a = x
        self.b = y


class Punkt:
    def __init__(self, x=0, y=0):
        self.a = x
        self.b = y

    def odleglosc(self, p):
        return math.sqrt((p.a-self.a)**2+(p.b-self.b)**2)

    def przesun(self, w):
        return Punkt(self.a+w.a, self.b+w.b)

    def __str__(self):
        return "("+str(self.a)+", "+str(self.b)+")"

# p = Punkt()
# print p
# print p.przesun(Wektor(1, 2))
# print p.odleglosc(p.przesun(Wektor(1, 1)))
# p1 = Punkt(1, 1)
# print p.odleglosc(p1)
# print p1.przesun(Wektor(2, 2))
#
#
class Prostokat:
    def __init__(self, x=0, y=0, dx=1, dy=1):
        self.p = Punkt(x, y)
        self.dx = dx
        self.dy = dy

    def pole(self):
        return self.dx*self.dy

    def obwod(self):
        return 2*(self.dx+self.dy)

    def przesun(self, w):
        return Prostokat(self.p.a+w.a, self.p.b+w.b, self.dx, self.dy)


# print Prostokat().pole()
# print Prostokat().obwod()
# print Prostokat().przesun(Wektor(1, 1)).obwod()

class Trojkat:
    def __init__(self, p1, p2, p3):
        self.p1 = Punkt(p1.a, p1.b)
        self.p2 = Punkt(p2.a, p2.b)
        self.p3 = Punkt(p3.a, p3.b)

    def obwod(self):
        return self.p1.odleglosc(self.p2) + \
            self.p2.odleglosc(self.p3) + \
            self.p3.odleglosc(self.p1)

    def pole(self):
        bok1 = self.p2.odleglosc(self.p3)
        bok2 = self.p1.odleglosc(self.p3)
        bok3 = self.p1.odleglosc(self.p2)
        pp = (bok1 + bok2 + bok3)/2.0
        return math.sqrt(pp*(pp-bok1)*(pp-bok2)*(pp-bok3))

a = Punkt(0, 0)
b = Punkt(1, 0)
c = Punkt(0, 1)

t = Trojkat(a, b, c)
print t.pole()
print t.obwod()
