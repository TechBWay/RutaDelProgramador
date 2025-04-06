# 0 o 1
# int (12312123) a binario

numero=1507
result=''
if numero==0:
    result='0'

while numero>0:
    result=str(numero%2)+result
    numero=numero//2

print(result)
# 0.1/2 = 0.05