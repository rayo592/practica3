while True:
  try:
    num = int(input('necesito un numero: '))
    den = int(input('necesito un numero: '))
    if num < den and (num/den)>=0.01 and (num/den)<=0.99:
        print("{}/{} = {}".format(num,den, num/den))
        per = (num/den)* 100
        ent = round(per)
        print('El tanque de gasolina está al {} %'.format(ent))
        break
    elif (num/den) < 0.01 and (num/den)>=0:
      print('E')
      break
    elif (num/den) > 0.99 and (num/den)<=1:
      print('F')
      break
    else:
        print("El numerador no puede ser mayor al denominador, escriba de nuevo por favor")
  except ValueError:
    print("Solo se pide que número sea entero")
  except ZeroDivisionError:
    print("El denominador no puede ser 0")
