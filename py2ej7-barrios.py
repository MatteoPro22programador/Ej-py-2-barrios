texto = input("Ingrese un texto: ")

contador = 0
for letra in texto:
    if letra.lower() == "a":
        contador += 1
print("Cantidad de 'a':", contador)