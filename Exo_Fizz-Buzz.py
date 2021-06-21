# Test de Fizz-Buzz
# Si le nombre est divisible par 3 : on écrit Fizz
# Si le nombre est divisible par 5 : on écrit Buzz
# Si le nombre est divisible par 3 et par 5 : on écrit Fizzbuzz
# Sinon on écrit le nombre

nombre = int(input("Saisissez un nombre : "))
mod3 = nombre % 3
mod5 = nombre % 5

if mod3==0 and mod5==0 :
    print("Fizzbuzz")
    
elif mod3 ==0 :
    print("Fizz")
    
elif mod5 ==0 :
    print("Buzz")

else:
    print(nombre)