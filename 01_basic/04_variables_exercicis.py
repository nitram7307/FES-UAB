###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom = "Encaminador 1"
ubicacio = "Datacenter A"
ports = 24
estat = True
print(f"El {nom} està ubicat a {ubicacio} i té {ports} ports.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_inclosos = 10
gb_consumits = 4
gb_restants = gb_inclosos - gb_consumits
print(f"Queden {gb_restants} GB del pla de dades.")