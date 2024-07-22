import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("donneesrugby.csv")

le = LabelEncoder()
data['home_team_id'] = le.fit_transform(data['home_team'])
data['away_team_id'] = le.transform(data['away_team'])

X = data[['home_team_id', 'away_team_id']]
y = (data['home_score'] > data['away_score']).astype(
    int)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'rugby_model2.joblib')

home_team = input("Nom de l'équipe à domicile : ")
away_team = input("Nom de l'équipe à l'extérieur : ")

home_team_id = le.transform([home_team])[0]
away_team_id = le.transform([away_team])[0]

new_match = [[home_team_id, away_team_id]]
prediction = model.predict(new_match)

winning_team = home_team if prediction[0] == 1 else away_team

print("L'équipe gagnante est : {}".format(winning_team))
