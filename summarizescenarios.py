
############## INTEGRER DANS SUMMARIZE SCENARIOS ##############
import os
import csv
import openai
import time
import os
import sys

sleeptime = int(os.environ.get("SLEEP_TIME"))

def summarize(text):
    api_key = os.environ.get("OPENAIAPI_KEY")    
    model_engine="text-davinci-003",
    prompt="Scenario :\n\"\"\"Scénario prospectif: Le marché du logement à l'ère de l'Intelligence Artificielle et de la Transition Energétique à l'horizon 2030\n\nA l'horizon 2030, le marché du logement devrait évoluer considérablement sous l'effet combiné de l'accélération des ruptures technologiques et des conséquences du changement climatique Le développement de l'intelligence artificielle ainsi que des objets connectés auront un impact majeur sur la manière dont les professionnels de l'immobilier travaillent. Les solutions de sobriété énergétique et les normes de construction se renforceront.\n\nCe scénario offre des opportunités considérables pour les acteurs du secteur du logement. Les entreprises qui investissent dans les technologies et en particulier l'IA et qui mettent en place des procédés de conception innovants pourront offrir des solutions plus personnalisées et des services à forte valeur ajoutée. L'IA permettra d'améliorer les outils d'analyse et de prédiction des prix du marché, de réduire les coûts et d'accélérer la réalisation des projets. Les bâtiments intelligents et les objets connectés permettront une plus grande optimisation des espaces et des ressources.\n\nCependant, ce scénario présente également des risques et des défis pour les acteurs du secteur. Les changements dans la répartition démographique et la demande de logement sous l'effet des conséquences du changement climatique, les nouvelles normes et exigences de construction, les nouveaux procédés de conception, les nouvelles compétences requises pour s'adapter aux technologies et les investissements majeurs nécessaires pour s'adapter à ces changements sont autant de risques à prendre en compte.\n\nCe scénario pourrait avoir un impact considérable sur un acteur du secteur du logement. Les entreprises qui sauront investir et se réinventer pour s'adapter aux nouvelles technologies et aux nouvelles normes pourront profiter de l'augmentation de la demande de solutions plus sobres en énergie et de services plus personnalisés.\n\nElles devront toutefois se préparer à affronter les défis et les risques liés aux conséquences du changement climatique et à la préservation de la vie privée et de la cybersécurité. L'adoption des bonnes pratiques et une meilleure gestion des données sont essentielles pour assurer le succès à long terme de ces entreprises.\"\"\"\n\nTitre : Le marché du logement à l'ère de l'Intelligence Artificielle et de la Transition Energétique\nTendances :  L’effet combiné de l'accélération des ruptures technologiques et des conséquences du changement climatique.\nOpportunités : \n- L'IA permettra d'améliorer les outils d'analyse et de prédiction des prix du marché, de réduire les coûts et d'accélérer la réalisation des projets. \n- Les bâtiments intelligents et les objets connectés permettront une plus grande optimisation des espaces et des ressources.\nRisques :\n- Les changements dans la répartition démographique et la demande de logement sous l'effet des conséquences du changement climatique, les nouvelles normes et exigences de construction.\n- Les nouvelles normes et exigences de construction, les nouveaux procédés de conception, les nouvelles compétences requises pour s'adapter aux technologies et les investissements majeurs nécessaires pour s'adapter à ces changements.\nActions à mener :\n- L’adaptation aux nouvelles technologies et aux nouvelles normes pourra profiter de l'augmentation de la demande de solutions plus sobres en énergie et de services plus personnalisés.\n- La préservation de la vie privée et les enjeux de cybersécurité. \n- L'adoption des bonnes pratiques et une meilleure gestion des données sont essentielles pour assurer le succès à long terme de ces entreprises.\n\nScenario :\n\"\"\"" + text + "\"\"\"\n",
    temp=0.7,
    max_tokens=2255,
    top_p=0.8,
    frequency_penalty=0,
    presence_penalty=0
    attempts = 0
    while attempts < 5:
        try:
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                n=1,
                stop=None,
                temperature=temp,
                api_key=api_key,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )
            message = completions.choices[0].text
            return message.strip()
        except:
            attempts += 1
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