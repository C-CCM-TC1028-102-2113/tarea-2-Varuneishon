
def main():
    #Escribe tu código debajo de esta línea
    e = int(input ("DIngresa tu edad: " ))


if e>=19:
    print("¿Tienes identificación oficial? (s/n): ")
    i = str(input())

else:
    print("No cumples requisitos")


if (i == 'n') or (i == 's'):
    print("Trámite de licencia concedido")

else:
    print("TNo cumples requisitos")
    pass


if __name__ == '__main__':
    main()
