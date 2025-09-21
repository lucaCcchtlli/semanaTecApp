import math

def rectangulo(base, altura):
	area = base * altura
	perimetro = (base + altura)*2

	return area, perimetro

def triangulo(base, altura):
	area = base * altura / 2
	c = math.sqrt(base**2 + altura**2)
	perimetro = base + altura + c

	return area, perimetro

def circulo(radio, medida2):
	area = 3.1416*radio**2
	perimetro = 2*3.1416*radio
	
	return area, perimetro

