
def main():
    #Escribe tu código debajo de esta línea

e = int(input ("DIngresa tu edad: " ))


if e>=19:
    print("¿Tienes identificación oficial? (s/n): ")
    i = str(input())
    

else:
    print("No cumples requisitos")
    print("¿Tienes identificación oficial? (s/n): ")
    i = str(input())


if (i == 's') and (e >= 19):
    print("Trámite de licencia concedido")

elif (i == 'n') or (e < 18):
    print("No cumples requisitos")

else:
    print('Respuesta incorrecta')


    pass


if __name__ == '__main__':
    main()
