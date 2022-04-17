def potencia(numero):
    potencia = 0
    LIMITE = 10

    while (potencia <= LIMITE):
        result = numero ** potencia
        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
        potencia += 1

def run():
    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    potencia(numero)

if __name__ == "__main__":
    run()