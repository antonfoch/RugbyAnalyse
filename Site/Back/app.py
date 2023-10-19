import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
# Initialiser l'application Flask
app = Flask(__name__)
CORS(app)
# Charger le modèle de prédiction
model = joblib.load('rugby_model2.joblib')

# Charger le LabelEncoder
le = LabelEncoder()

# Charger les données
data = pd.read_csv("donneesrugby.csv")
le.fit(data['home_team'])

# Définir la route pour les prédictions


@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données JSON de la requête
    data = request.get_json()

    home_team = data['home_team']
    away_team = data['away_team']

    # Utiliser LabelEncoder pour convertir les noms des équipes en identifiants
    home_team_id = le.transform([home_team])[0]
    away_team_id = le.transform([away_team])[0]

    # Créer une nouvelle entrée pour la prédiction
    new_match = [[home_team_id, away_team_id]]
    prediction = model.predict(new_match)

    winning_team = home_team if prediction[0] == 1 else away_team

    # Retourner la réponse JSON
    response = {'winning_team': winning_team}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
