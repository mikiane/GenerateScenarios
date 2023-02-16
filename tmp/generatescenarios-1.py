
import csv
import itertools

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
            concat_list.append('Tendance 1 : \n\n' + ''.join(row1) + '\n\n Tendance 2 ' + ''.join(row2) + '\n\n')
            # Affichage de la concaténation avec print
            print('Tendance 1 : \n\n' + ''.join(row1) + '\n\n Tendance 2 ' + ''.join(row2) + '\n\n')
            
            

    # Création d'un nouveau fichier csv de sortie
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)

        # Écrire chaque concaténation dans une nouvelle ligne du fichier de sortie
        for concat in concat_list:
            writer.writerow([concat])
