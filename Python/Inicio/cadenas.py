nombre = "Ricardo Mesa Gallego"
print("Nombre: ", nombre)
print("Eliminando espacios es: ", nombre.lstrip())
print("Letras en minúsculas: ", nombre.lower())
print("Letras en mayúsculas: ", nombre.upper())
print("Primera letra en mayúscula: ", nombre.capitalize())
print("Reemplazando carácter a por e: ", nombre.replace("a", "e"))
print("Cantidad de letras: ", len(nombre))
print("Tercera letra: ", nombre[2])

print("\n<><><><><><><><><><> \n")

print("Nombre: ", nombre)
print("Primeros 3 caracteres: ", nombre[0:3])
print("Primeros 3 caracteres: ", nombre[:3]) #Otra forma
print("Últimos 3 caracteres: ", nombre[-3:])
print("Desde el indice 2 hasta el final: ", nombre[2:])
print("Desde el indice 0 hasta el 8, de 2 en dos: ", nombre[0:8:2])
print("Palabra al revés: ", nombre[::-1])