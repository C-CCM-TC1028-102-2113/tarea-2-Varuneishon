def main():
    #escribe tu código abajo de esta línea
    p = float(input("Peso en Kg: "))
a = float(input("Altura en metros: "))

i = p/(a**2)
 
if (0 > i < 20):
   print('PESO BAJO')

elif (20 <= i <25):
    print('NORMAL')

elif (25 <= i <30):
    print('SOBREPESO')

elif (30 <= i <40):
    print('OBESIDAD')

elif (40 < i):
    print('OBESIDAD MORBIDA')

else:
    print('Revisa tus datos, alguno de ellos es erróneo.')
    pass
if __name__=='__main__':
    main()
