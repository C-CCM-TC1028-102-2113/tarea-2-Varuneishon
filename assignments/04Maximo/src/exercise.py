def main():
    #escribe tu código abajo de esta línea
   a = float(input("Ingresa el primer número: "))
   b = float(input("Ingresa el segundo número: "))
   c = float(input("Ingresa el tercer número: "))
   
   if (a > b) and (a > c):
      g = a
   elif (b > a) and (b > c):
      g = b
   else:
      g = c
   
   print(str(int(g)))
   pass


if __name__=='__main__':
    main()
