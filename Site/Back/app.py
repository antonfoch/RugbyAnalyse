import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load('rugby_model2.joblib')


le = LabelEncoder()


data = pd.read_csv("donneesrugby.csv")
le.fit(data['home_team'])


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    home_team = data['home_team']
    away_team = data['away_team']

    home_team_id = le.transform([home_team])[0]
    away_team_id = le.transform([away_team])[0]

    new_match = [[home_team_id, away_team_id]]
    prediction = model.predict(new_match)

    winning_team = home_team if prediction[0] == 1 else away_team

    response = {'winning_team': winning_team}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
