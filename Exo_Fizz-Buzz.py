def Fizz(nombre):       
    mod3 = nombre % 3 # Si le nombre est un multiple 3.
    if mod3==0:
        res="Fizz"    # La fonction retourne "Fizz".
    else:
        res=""        # Sinon la fonction retourne le nombre tel quel.
    return res 

def Buzz(nombre):
    mod5 = nombre % 5 # Si le nombre est un multiple 5.
    if mod5==0:
        res="Buzz"    # La fonction retourne "Buzz".
    else:
        res=""        # Sinon la fonction retourne le nombre tel quel.
    return res

def Kizz(nombre):
    mod7 = nombre % 7 # Si le nombre est un multiple 7.
    if mod7==0:
        res="Kizz"    # La fonction retourne "Kizz".
    else:
        res=""        # Sinon la fonction retourne le nombre tel quel.
    return res

i=0

for nombre in range(101):
    if bool(Fizz(nombre)) == True or bool(Buzz(nombre)) == True or bool(Kizz(nombre)) == True:
        print(
            Fizz(nombre) + Buzz(nombre) + Kizz(nombre)
        )

    else:
        print(i)
