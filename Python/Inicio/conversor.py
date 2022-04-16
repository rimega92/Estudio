#convierte pesos mexicanos, argentinos y colombianos a dólares

def conversor(trm,nacionalidad):
    pesos = input("¿Cuantos pesos " + nacionalidad + " tienes?:      ")
    pesos = float(pesos)
    dolares = pesos / trm
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares") 

# """ """ permite crear strings multi lineas
menu = """
Bienvenido al conversor de monedas multi país

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción: 

"""
# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
   conversor(19.50, "Mexicanos")
elif opcion == 2: #pesos colombianos
   conversor(3700, "Colombianos")
elif opcion == 3: #pesos argentinos
   conversor(60, "Argentinos")
else:  #el usuario escribió algo diferente
   print('Escribe una opción correcta')