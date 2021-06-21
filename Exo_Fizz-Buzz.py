# Test de Fizz-Buzz
# Si le nombre est divisible par 3 : on écrit Fizz
# Si le nombre est divisible par 5 : on écrit Buzz
# Si le nombre est divisible par 7 : on écrit Kizz
# Si le nombre est divisible par 3 et par 5 : on écrit FizzBuzz
# Si le nombre est divisible par 3 et par 7 : on écrit FizzKizz
# Si le nombre est divisible par 5 et par 7 : on écrit BuzzKizz
# Si le nombre est divisible par 3 et 5 et par 7 : on écrit FizzBuzzKizz
# Sinon on écrit le nombre

def Fizz(nombre):
    mod3 = nombre % 3
    if mod3==0:
        res="Fizz"
    else:
        res=""
    return res

def Buzz(nombre):
    mod5 = nombre % 5
    if mod5==0:
        res="Buzz"
    else:
        res=""
    return res

def Kizz(nombre):
    mod7 = nombre % 7
    if mod7==0:
        res="Kizz"
    else:
        res=""
    return res

i=0

for nombre in range(101):
    if bool(Fizz(nombre)) == True or bool(Buzz(nombre)) == True or bool(Kizz(nombre)) == True:
        print(
            Fizz(nombre) + Buzz(nombre) + Kizz(nombre)
        )

    else:
        print(i)
    i = i+1
