class Fraction:
    def __init__(self, brojnik, nazivnik=1):
        self.brojnik = brojnik
        self.nazivnik = nazivnik

    def print(self):
        print(str(self.brojnik) + '/' + str(self.nazivnik))