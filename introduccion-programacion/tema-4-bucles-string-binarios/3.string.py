cadena="adsljfheqwepqwekasdjasd"

word= input('ingrese la palabra: ')
cadenaResultado=''

for i in word:
    if i in cadena:
        cadenaResultado=cadenaResultado+i
    else:
        print(f'esta letra no existe en la cadena {i}')


print(cadenaResultado)

