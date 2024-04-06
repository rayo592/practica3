def pide_calific():

  calific = input('ingresa numeros enumerandolos por coma: ')
  separadas = calific.split(',')
  lista_almacen = []

  for i in separadas:
    try:  
        enteronum = int(i.strip())  
        lista_almacen.append(enteronum)
    except ValueError:
        print("Colocar un caracter válido")
  return lista_almacen

pide_calific()
