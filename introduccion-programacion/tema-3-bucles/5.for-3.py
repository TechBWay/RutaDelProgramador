# x*x=16

n=int(input('ingrese el numero a adivinar:'))
valorNuevo=int(n/2)+1
for i in range(valorNuevo):
    if i*i==n:
        print(f'esta es la raiz cuadrada {i}')

