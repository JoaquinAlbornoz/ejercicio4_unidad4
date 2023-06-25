class Imaginario:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, otro):
        real_suma = self.real + otro.real
        imaginario_suma = self.imaginario + otro.imaginario
        return Imaginario(real_suma, imaginario_suma)

    def __sub__(self, otro):
        real_resta = self.real - otro.real
        imaginario_resta = self.imaginario - otro.imaginario
        return Imaginario(real_resta, imaginario_resta)

    def __mul__(self, otro):
        real_mul = (self.real * otro.real) - (self.imaginario * otro.imaginario)
        imaginario_mul = (self.real * otro.imaginario) + (self.imaginario * otro.real)
        return Imaginario(real_mul, imaginario_mul)

    def __truediv__(self, otro):
        denominador = (otro.real ** 2) + (otro.imaginario ** 2)
        real_div = ((self.real * otro.real) + (self.imaginario * otro.imaginario)) / denominador
        imaginario_div = ((self.imaginario * otro.real) - (self.real * otro.imaginario)) / denominador
        return Imaginario(real_div, imaginario_div)
