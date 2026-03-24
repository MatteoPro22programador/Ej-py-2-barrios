total=0

while True:
    num=int(input('ingrese numeros positivos:'))

    if num<0:
        break

    total+=num
    print('el total es:',total)