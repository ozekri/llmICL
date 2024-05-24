import numpy as np
import pickle
import matplotlib.pyplot as plt

def entier_vers_liste(entier):
    liste_chiffres = [int(chiffre) for chiffre in str(entier)]
    return liste_chiffres
# Charger les données à partir du fichier .pkl
with open('0.pkl', 'rb') as f:
    data = pickle.load(f)

data = entier_vers_liste(data)

# Supposons que vos données soient stockées sous forme de listes (x_data et y_data)
x_data = np.arange(len(data))
y_data = data

# Créer un graphique en utilisant Matplotlib
plt.plot(x_data, y_data)
plt.xlabel('t')
plt.ylabel('i(t)')
plt.title('Graphique à partir de données .pkl')
plt.grid(True)
plt.show()
"""
import pickle

# Ouvrir le fichier .pkl en mode lecture binaire ('rb' pour read binary)
with open('0.pkl', 'rb') as f:
    # Charger les données depuis le fichier .pkl
    donnees = pickle.load(f)

# Maintenant, vous pouvez utiliser les données comme bon vous semble
print(donnees)
"""