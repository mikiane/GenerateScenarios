import csv
import re

# Ouvrir le fichier input.txt
with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Séparer le texte en lignes
lines = input_text.split('\n')

# Initialiser la liste des paragraphes
paragraphs = []

# Parcourir les lignes et récupérer les paragraphes
for line in lines:
    # Vérifier si la ligne commence par "Scenario"
    if re.match(r'^\s*[Ss]cénario', line) or re.match(r'^\s*[Ss]cenario', line):
        # Ajouter le paragraphe courant à la liste
        if paragraphs:
            paragraphs[-1] = paragraphs[-1].strip()
        paragraphs.append(line)
    else:
        # Ajouter la ligne courante au paragraphe courant
        if paragraphs:
            paragraphs[-1] += "\n" + line

# Ajouter le dernier paragraphe à la liste
if paragraphs:
    paragraphs[-1] = paragraphs[-1].strip()

# Écrire les paragraphes dans un fichier CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    for paragraph in paragraphs:
        writer.writerow([paragraph])
