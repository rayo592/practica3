class RECTANGULO:
  def __init__(self, largo,ancho):
    self.largo = largo
    self.ancho = ancho
  def area(self):
   return self.largo * self.ancho
rect1 = RECTANGULO(12,4)
area_mostrada = rect1.area()
print(f'el área del rectángulo es {area_mostrada}')

