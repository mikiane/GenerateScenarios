import os
import csv
import openai
import time
import os
import sys

sleeptime = int(os.environ.get("SLEEP_TIME"))

def summarize(text):
    api_key = os.environ.get("OPENAIAPI_KEY")    
    attempts = 0
    while attempts < 5:
        try:
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt = "Décrire un concept de service ou de produit du secteur de l'immobilier qui saisirait les opportunités d'un tel scenario à l'horizon 2030 : \n\n" + text,
                n=1,
                temperature=0.95,
                api_key=api_key,
                max_tokens=2000,
                top_p=0.90,
                frequency_penalty=0.5,
                presence_penalty=0.5
            )
            message = completions.choices[0].text
            return message.strip()
        
        except Exception as e:
            error_code = type(e).__name__
            error_reason = str(e)
            attempts += 1
            print(f"Erreur : {error_code} - {error_reason}. Nouvel essai dans 5 secondes...")
            time.sleep(5)

    print("Erreur : Echec de la création de la completion après 5 essais")
    sys.exit()

input_file = None
output_file = None

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

with open(input_file, "r") as input_file:
    reader = csv.reader(input_file)
    header = next(reader)
    header = ["Résumé"] + header[1:]
    with open(output_file, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        for row in reader:
            text = row[0]
            summary = summarize(text)
            row = [summary]
            writer.writerow(row)
            print(row)
            time.sleep(sleeptime)