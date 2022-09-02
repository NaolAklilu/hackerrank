import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real 
        self.imaginary = imaginary
        
    def __add__(self, no):
        a, b = self.real , self.imaginary
        c, d = no.real, no.imaginary
    
        return Complex(a + c, b + d)
    
    def __sub__(self, no):
        a, b = self.real , self.imaginary
        c, d = no.real, no.imaginary
    
        return Complex(a - c, b - d)
    
    def __mul__(self, no):
        a, b = self.real , self.imaginary
        c, d = no.real, no.imaginary
        
        return Complex(a*c - b*d, a*d + b*c)
    
    def __truediv__(self, no):
        a, b = self.real , self.imaginary
        c, d = no.real, no.imaginary
        
        common_divider = 1 / (c ** 2 + d ** 2)
        
        return Complex(common_divider * (a*c + b*d), common_divider *(b*c - a*d))
    
    def mod(self):
        modulus = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(round(modulus, 2), 0.00)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(
