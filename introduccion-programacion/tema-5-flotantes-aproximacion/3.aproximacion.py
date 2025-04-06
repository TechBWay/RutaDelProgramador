x=36 # 6
epsilon=0.001
num_guess=0
guess=0.0
incrementado=0.00001

while abs(guess**2-x)>=epsilon:
    guess+=incrementado
    num_guess+=1

print(guess)
