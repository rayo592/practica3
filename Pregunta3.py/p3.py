class circulo:  
  def __init__(self,radio):
    self.radio = radio
  def area(self):
    return self.radio**2 *3.1415
circ1 = circulo(4)
area_mostrada = circ1.area()
print(f"El radio del círculo es {circ1.radio} y el área es {area_mostrada}")
