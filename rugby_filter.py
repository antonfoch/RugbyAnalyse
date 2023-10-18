import pandas as pd

# Charger les données depuis un fichier CSV
data = pd.read_csv('donneesrugby.csv')

# Fonction pour déterminer le gagnant


def determine_winner(row):
    if row['home_score'] > row['away_score']:
        return 1
    elif row['away_score'] > row['home_score']:
        return -1
    else:
        return 0  # Tie


# Ajouter une colonne "winner" avec les valeurs encodées
data['winner'] = data.apply(determine_winner, axis=1)

# Enregistrez le jeu de données mis à jour dans un nouveau fichier CSV
data.to_csv('donneesrugby2.csv', index=False)
