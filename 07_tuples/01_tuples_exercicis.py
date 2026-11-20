# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Barcelona", "Madrid", "València", "Sevilla", "Bilbao")
print(ciutats[1])
print(ciutats[-2])
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numeros = (1, 2, 3, 4, 3, 5, 3)
count_3 = numeros.count(3)
print(count_3)
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla):
    return tuple(sorted(tupla))
numeros_desordenats = (5, 2, 9, 1, 3)
numeros_ordenats = ordenar_tupla(numeros_desordenats)
print(numeros_ordenats)