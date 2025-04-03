varaible=20
variable2=30

print(variable2==varaible)

# necesito saber si un usuario es mayor de edad y esta registrado
#(edad>18) and (emailRegistrado)

clave=5
entrada = int(input("ingrese la clave:"))

if entrada == clave:
    print("la clave es correcta")
elif entrada>clave:
    print("tu valor es muy grande")
elif entrada<clave:
    print("tu valor es muy pequeño")
else:
    print("la clave es incorreecta")
