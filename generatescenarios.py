import csv
import time
import os
import sys
import itertools
import openai



def traitement(text):
    attempts = 0
    prompt = "Voici deux tendances à l'horizon 2030. A partir de ces deux tendances, construire un scenario  prospectif de l'évolution du marché du logement à 2030. Donner un titre à ce scenario et imaginer quel impact ce scenario pourrait avoir, sur un acteur du secteur du logement. Quels risques et quelles opportunités il génère ? \n\n" + text
    while attempts < 5:
        try:
            #print(prompt)
            #print("\n\n")
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.9,
                api_key = os.environ.get("OPENAIAPI_KEY"),
                max_tokens=2500,
                top_p=0.9,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\"\"\""])
            message = response.choices[0].text
            print(message)
            print("\n\n")
            return message.strip()
        except:
            attempts += 1
            print("tentative : " + str(attempts))
            time.sleep(5)
    print("Erreur : Echec de la création de la completion après 5 essais")
    sys.exit()
            
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
            # Concaténer les deux lignes avec les chaînes "Tendance 1" et "Tendance 2" et ajouter la chaîne à la liste de concaténations
            concat = 'Tendance 1 : ### ' + ''.join(row1) + ' ###\n\nTendance 2 : ### ' + ''.join(row2) + ' ### \n\n'
            concat_list.append(concat)
            # Appel de la fonction de traitement pour chaque concaténation et stockage des résultats dans une liste
            #print(concat)
            resultat = traitement(concat)
            with open(output_file, 'a', newline='') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow([resultat])
            # Affichage de l'état actuel du traitement
            print("Traitement : ", len(concat_list))

