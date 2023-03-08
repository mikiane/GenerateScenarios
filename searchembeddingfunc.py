#from openai.embeddings_utils import get_embedding
#from transformers import GPT2TokenizerFast
#from sklearn.metrics.pairwise import cosine_similarity
import os


# Aprés 5 à 10 minutes
def get_embedding(text, model="text-embedding-ada-002"):
    import openai
    #definir la clé OpenAI
    openai.api_key = os.environ.get("OPENAIAPI_KEY")
    text = text.replace("\n", " ")
    return openai.Embedding.create(input = [text], engine=model)['data'][0]['embedding']

def searchembedding(text, filename):
    import numpy as np
    import pandas as pd
    import openai
    #definir la clé OpenAI
    openai.api_key = os.environ.get("OPENAIAPI_KEY")

    # read the csv file
    df = pd.read_csv(filename)
    # convert the strings stored in the ad_vector column
    # into vector objects
    df['ada_embedding'] = df.ada_embedding.apply(eval).apply(np.array)

    #We can access the values using - this will be a 2D vector
    df.loc[0]['ada_embedding']

    # convert our search term into a vector
    searchvector = get_embedding(text, model='text-embedding-ada-002')

    #df['ada_embedding'] = df.ada_embedding.apply(lambda x: x.reshape(1, -1))

    # create a new column using cosine_similarity on EVERY row
    # comparing our searchvector string to the value in our local dataset
    df['similarities'] = df.ada_embedding.apply(lambda x: np.dot(x, searchvector))

    # sort the list by the difference and take the top n rows
    # res is up to 1 rows
    # it contains all data
    res = df.sort_values('similarities', ascending=False).head(1)
    # we can access the combined column to get the matching text
    # we could also access any of the other columns in the Data Frame

    #stocker dzans un fichier csv le resultat de la recherche
    #res.to_csv('resultat.csv', index=False)

    #afficher le resultat de la recherche à l'écran
    #from IPython.display import display
    import pandas as pd
    pd.set_option('display.max_columns', None)
    #display(res)

    #afficher le resultat de la colonne 'combined" de la premiere ligne.
    # vérifier si la colonne 'combined' existe dans le DataFrame
    if 'Scenarios' in res.columns:
        # vérifier si le DataFrame n'est pas vide
        if not res.empty:
            # vérifier si l'index est de type entier
            if res.index.dtype == 'int64':
                # renvoie tous les enregistremnts (3)
                return '\n'.join(res['Scenarios'].values)
                # renvoie le 1er enregistremnt de la base
                #return res.iloc[0]['combined']
            else:
                return "L'index du DataFrame n'est pas de type entier"
        else:
            return "Le DataFrame est vide"
    else:
        return "La colonne 'Scenarios' n'existe pas dans le DataFrame"
