import csv
import re

# Ouvrir le fichier CSV en lecture
with open('output-preclean.csv', 'r', newline='', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    # Ouvrir le fichier CSV en écriture
    with open('cleanoutput.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        # Parcourir chaque ligne du fichier en entrée
        for row in reader:
            # Supprimer les expressions "Scenario x :" ou "Scénario x :"
            row[0] = re.sub(r'^\s*[Ss]cénario\s*\d\s*:', '', row[0])
            row[0] = re.sub(r'^\s*[Ss]cenario\s*\d\s*:', '', row[0])
            row[0] = re.sub(r'^\s*[Ss]cenario\s*\d\s*-', '', row[0])
            row[0] = re.sub(r'^\s*[Ss]cénario\s*\d\s*-', '', row[0])
            # Écrire la ligne modifiée dans le fichier de sortie
            writer.writerow(row)
