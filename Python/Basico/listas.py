from itertools import count


def run():
   mi_lista = [] # Creo una lista vacía
   mi_lista = list() # Creo una lista vacía (Otra manera de hacerlo)
   mi_lista = [8,4,6,3,1,7,2,5,2]
   print(mi_lista)
   print(sorted(mi_lista))
   print(mi_lista.count(2))
   mi_lista.reverse()
   print(mi_lista)
   mi_lista.append(9)
   print(mi_lista)
   print(mi_lista.index(7))
   print(mi_lista[3])
   print(mi_lista)
   mi_lista.pop(2) # Elimina el elemento en la posición 2
   print(mi_lista)
   print("\n")
   for elementos in mi_lista:
      print(elementos)
   print("\n")
   print(mi_lista[::-1]) # Imprime la lista al revés
if __name__ == "__main__":
   run()