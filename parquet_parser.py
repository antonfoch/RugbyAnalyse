import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Étape 1 : Charger les données à partir du fichier CSV
data = pd.read_csv("donneesrugby2.csv")

# Étape 2 : Prétraiter les données
# Utiliser Label Encoding pour convertir les noms d'équipes en identifiants numériques
le = LabelEncoder()
data['home_team_id'] = le.fit_transform(data['home_team'])
data['away_team_id'] = le.transform(data['away_team'])

# Sélectionner les caractéristiques (features) et la cible (target)
X = data[['home_team_id', 'away_team_id']]
y = (data['home_score'] > data['away_score']).astype(
    int)  # 1 si l'équipe à domicile gagne, 0 sinon
 
# Étape 3 : Entraîner un modèle de classification (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Étape 4 : Faire des prédictions pour de nouveaux matchs depuis l'entrée standard (terminal)
home_team = input("Nom de l'équipe à domicile : ")
away_team = input("Nom de l'équipe à l'extérieur : ")

# Utiliser LabelEncoder pour convertir les noms des équipes en identifiants
home_team_id = le.transform([home_team])[0]
away_team_id = le.transform([away_team])[0]

# Créer une nouvelle entrée pour la prédiction
new_match = [[home_team_id, away_team_id]]
prediction = model.predict(new_match)

winning_team = home_team if prediction[0] == 1 else away_team

print("L'équipe gagnante est : {}".format(winning_team))
