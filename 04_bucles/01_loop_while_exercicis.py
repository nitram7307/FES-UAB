###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
while num > 0:
    print(num)
    num -= 1
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
while num <= 20:
    if num % 2 == 0:
        suma += num
    num += 1
# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
input_num = int(input("Introdueix un número enter positiu: "))
factorial = 1
while input_num > 1:
    factorial *= input_num
    input_num -= 1
print("El factorial és:", factorial)
# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
password = input("Introdueix una contrasenya (almenys 8 caràcters): ")
while len(password) < 8:
    password = input("Contrasenya massa curta. Torna a introduir-la: ")
print("Contrasenya vàlida")
# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num = int(input("Introdueix un número: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
num = int(input("Introdueix un número enter positiu N: "))
current = 2
while current <= num:
    es_primer = True
    divisor = 2
    while divisor < current:
        if current % divisor == 0:
            es_primer = False
            break
        divisor += 1
    if es_primer:
        print(current)
    current += 1
# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
suma = 0
while True:
    num = int(input("Introdueix un número (0 per acabar): "))
    if num == 0:
        break
    suma += num
print("La suma total és:", suma)

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
num = int(input("Introdueix un número enter positiu: "))
if num == 0:
    digits = 1
else:
    digits = 0
    while num > 0:
        num //= 10
        digits += 1
print("El nombre de xifres és:", digits)
# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
num_terms = int(input("Introdueix el nombre de termes de la seqüència de Fibonacci: "))
a, b = 0, 1
i = 0
while i < num_terms:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
numero_secret = 7
while True:
    intent = int(input("Endevina el número secret (entre 1 i 10): "))
    if intent == numero_secret:
        print("Enhorabona! Has endevinat el número secret.")
        break
    elif intent < numero_secret:
        print("El número secret és més gran.")
    else:
        print("El número secret és més petit.")