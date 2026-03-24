nombrePrincipal=[]
#agrega nombres
while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    
    if nombre.lower() == "fin":
        break
    
    nombrePrincipal.append(nombre)

#ordena la lista alfabeticamente

nombrePrincipal.sort()

print('lista ordenada:',nombrePrincipal)

#contador

contador=0

for n in nombrePrincipal:
    if n.lower().startswith("a") or n.lower().startswith("e"):
        contador += 1
        print('cuntos nombres empeizan con la letra a o e:',contador)

#busca nombres

buscar=input('Busca un nombre en la lista')


if buscar in nombrePrincipal:
        print('el nombre',buscar,'si esta en la lista')
else:
        print('el nombre',buscar,'no esta en la lista')
