###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
input_nom_tecnic = input("Introdueix el nom del tècnic: ")
input_nom_xarxa = input("Introdueix el nom de la xarxa: ")
print(f"El tècnic {input_nom_tecnic} està instal·lant la xarxa {input_nom_xarxa}.")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
input_longitud_km = input("Introdueix la longitud de l'enllaç de fibra en km: ")
input_velocitat_gbps = input("Introdueix la velocitat de transmissió en Gbps: ")
longitud_km = float(input_longitud_km)
velocitat_gbps = float(input_velocitat_gbps)
temps_transmissio_segons = (8 / velocitat_gbps)
print(f"Per transmetre 1 GB de dades a {velocitat_gbps} Gbps caldrien aproximadament {temps_transmissio_segons:.2f} segons.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
input_hores = input("Introdueix el nombre d'hores de feina: ")
input_preu_hora = input("Introdueix el preu per hora: ")
input_preu_material = input("Introdueix el preu del material: ")
hores = float(input_hores)
preu_hora = float(input_preu_hora)
preu_material = float(input_preu_material)
cost_total = (hores * preu_hora) + preu_material
print(f"El cost total de la instal·lació és: {cost_total:.2f} unitats monetàries.")