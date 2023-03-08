
from searchembeddingfunc import searchembedding
import sys

#récupérer le texte à traiter dans l'argument du script python  
text = sys.argv[1]  
resultat = searchembedding(text, '/Users/michel/tmp/outputscenariosembeddings.csv')
print(resultat)