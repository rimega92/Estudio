# Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes 
# tipos de valores sin darle importancia a su orden. 
# Identifican a cada elemento por una clave (Key). Se escriben entre {}

def run():
    # Defino el diccionario, agrego los valores.
   mi_diccionario = {
      'clave1' : 1,
      'clave2' : 2,
      'clave3' : 3
   }

   print(mi_diccionario)
   print(mi_diccionario['clave1'])

   # Imprimo las clave.
   for llave in mi_diccionario.keys():
        print(llave)
   # Imprimo el valor de la clave.
   for valores in mi_diccionario.values():
      print(valores)
   # Imprimo el clave y valor
   for llave, items in mi_diccionario.items():
      print("La llave: '" + llave + "' contiene el item: " + str(items))

if __name__ == '__main__':
    run()