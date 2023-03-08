# imports
import numpy as np
import pandas as pd
import os
import openai

openai.api_key = os.environ.get("OPENAIAPI_KEY")


# load data
datafile_path = "/Users/michel/tmp/outputscenariosembeddings.csv"

df = pd.read_csv(datafile_path)
df["ada_embedding"] = df.ada_embedding.apply(eval).apply(np.array)  # convert string to numpy array
matrix = np.vstack(df.ada_embedding.values)
matrix.shape

from sklearn.cluster import KMeans

n_clusters = 15

kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
kmeans.fit(matrix)
labels = kmeans.labels_
df["Cluster"] = labels

#df.groupby("Cluster").Scenarios.mean().sort_values()

from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt

tsne = TSNE(n_components=2, perplexity=75, random_state=42, init="random", learning_rate=1000)
vis_dims2 = tsne.fit_transform(matrix)

x = [x for x, y in vis_dims2]
y = [y for x, y in vis_dims2]

#for category, color in enumerate(["purple", "green", "red", "blue"]):
for category, color in enumerate(['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white', 
          'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 
          'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 
          'cornflowerblue', 'cornsilk', 'crimson', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 
          'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 
          'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 
          'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 
          'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 
          'goldenrod', 'gray', 'grey', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 
          'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 
          'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgrey', 'lightgreen', 
          'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 
          'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 
          'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 
          'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 
          'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 
          'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff']):
    xs = np.array(x)[df.Cluster == category]
    ys = np.array(y)[df.Cluster == category]
    plt.scatter(xs, ys, color=color, alpha=0.3)

    avg_x = xs.mean()
    avg_y = ys.mean()

    plt.scatter(avg_x, avg_y, marker="x", color=color, s=100)
plt.title("Clusters identified visualized in language 2d using t-SNE")
plt.savefig('/Users/michel/tmp/graph.png')

import openai

# Reading a review which belong to each group.
rev_per_cluster = 10

#Fichier de sortie
#file = open("/Users/michel/tmp/scenariosculturisesoutput.txt", "w")


for i in range(n_clusters):
    print(f"Cluster {i} Theme:", end=" ")
    #file.write(f"Cluster {i} Theme:", end=" ")

    reviews = "\n".join(
        df[df.Cluster == i]
        .Scenarios.str.replace("Title: ", "")
        .str.replace("\n\nContent: ", ":  ")
        .sample(rev_per_cluster, random_state=42)
        .values
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'Décrire en une phrase comment ces scenarios anticipent le futur du metavers. \n\nScenarios :\n"""\n{reviews}\n\n Résumé : ""',
        temperature=0.1,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response["choices"][0]["text"].replace("\n", ""))
    #file.write(response["choices"][0]["text"].replace("\n", ""))


    #sample_cluster_rows = df[df.Cluster == i].sample(rev_per_cluster, random_state=42)
    #summary_scenarios = ""
    #for j in range(rev_per_cluster):
    #    summary_scenarios = summary_scenarios + "######### \n\n" + sample_cluster_rows.Scenarios.values[j] + "\n\n"
    
    
    #response2 = openai.Completion.create(
    #    engine="text-davinci-003",
    #    prompt=summary_scenarios + "tl;dr",
    #    temperature=0.5,
    #    max_tokens=400,
    #    top_p=1,
    #    frequency_penalty=0,
    #    presence_penalty=0,
    #)
    #print(response2["choices"][0]["text"].replace("\n", ""))
    #file.write(response2["choices"][0]["text"].replace("\n", ""))
    #file.close()
    
    
    