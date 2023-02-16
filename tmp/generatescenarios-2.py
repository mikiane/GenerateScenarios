import csv
import openai
import time
import os
import sys
import itertools



# Définition de la fonction de traitement
def traitement(concatenation):
    # Ajouter "Traitement : " devant la concaténation
    return "Traitement : " + concatenation



# Chemin d'accès au fichier d'entrée
input_file = 'bcef.csv'

# Chemin d'accès au fichier de sortie
output_file = 'bcefout.csv'

# Lecture du fichier d'entrée
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)

    # Récupération de toutes les lignes du fichier dans une liste
    rows = [row for row in reader]

    # Initialisation de la liste de concaténations
    concat_list = []

    # Génération de toutes les paires de lignes
    for row1, row2 in itertools.product(rows, rows):
        # Vérification que les deux lignes sont différentes
        if row1 != row2:
            # Concaténer les deux lignes avec les chaînes "Tendance 1" et "Tendance 2" et ajouter la chaîne à la liste de concaténations
            concat_list.append('Tendance 1 ' + ''.join(row1) + ' Tendance 2 ' + ''.join(row2))

    # Appel de la fonction de traitement pour chaque concaténation et stockage des résultats dans une liste
    traitement_list = [traitement(concat) for concat in concat_list]

    # Écriture de la liste de résultats dans un fichier csv de sortie
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)

        # Écrire chaque résultat dans une nouvelle ligne du fichier de sortie
        for resultat in traitement_list:
            writer.writerow([resultat])

