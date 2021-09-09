def main():
    # Escribe el código adecuado para completar el programa
   a = float(input("Ingresa el primer número: "))
   b = float(input("Ingresa el segundo número: "))
   c = float(input("Ingresa el tercer número: "))
   
   if (a > b) and (a > c):
      g = a
   elif (b > a) and (b > c):
      g = b
   else:
      g = c

   if (a < b) and (a < c):
      p = a
   elif (b < a) and (b < c):
      p = b
   else:
      p = c

   if (a < b) and (a > c):
      e = a
   elif (b < a) and (b > c):
      e = b
   else:
      e = c

   print(str(int(p)))
   print(str(int(e)))
   print(str(int(g)))
   pass


if __name__=='__main__':
    main()
