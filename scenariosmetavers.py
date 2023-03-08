import csv
import time
import os
import sys
import itertools
import openai


def generatesimilarity(ph1, ph2):
    api_key = os.environ.get("OPENAIAPI_KEY")
    attempts = 0
    while attempts < 5:
        try:
            print("ph1 : " + ph1 + " - ph2 : " + ph2  + " - attempts : " + str(attempts))   
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt="Tendance 1 : ### " + ph1 + " ### \nTendance 2 :  ### " + ph2 + " ### \n\nÀ partir de ces deux tendances, construire 4 scénarios résultant de la combinaison de ces deux tendances et de leur impact sur l'évolution du développement et de l'adoption du metavers. \nLe scenario 1 correspond à la croissance de la tendance 1 et de la tendance 2. \nLe scenario 2 correspond à la décroissance de la tendance 1 et la croissance de la tendance 2. \nLe scenario 3 correspond à la croissance de la tendance 1 et la décroissance de la tendance 2. \nLe scenario 4 correspond à la décroissance de la tendance 1 et de la tendance 2. \nChaque scenario doit être titré et raconter une courte histoire.\n",
                temperature=0.98,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                n=1,
                api_key=api_key,
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



# Ouvrir le fichier txt contenant les phénomènes
with open("tendances.txt", "r", encoding="utf-8") as f:
    phenomenes = f.read().splitlines()

# Ouvrir un nouveau fichier txt pour stocker les résultats
with open("resultats.txt", "w", encoding="utf-8") as f:
    # Trouver les liens entre les phénomènes
    for i, ph1 in enumerate(phenomenes):
        for j, ph2 in enumerate(phenomenes):
            if i != j:
                sim = generatesimilarity(ph1, ph2)
                # Écrire la valeur de sim dans le fichier txt
                f.write(str(sim) + "\n")
                print(str(sim) + "\n")


# Afficher un message pour indiquer que le traitement est terminé
print("Les résultats ont été stockés dans le fichier resultats.txt.")


### Reste ensuite à clusteriser les résultats pour trouver les scenarios qui s'en dégagent :
### https://github.com/openai/openai-cookbook/blob/main/examples/Clustering.ipynb
