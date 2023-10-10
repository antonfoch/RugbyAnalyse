import json

# Charger le contenu du fichier JSON dans une variable
with open('data.json', 'r') as json_file:
    data_from_file = json.load(json_file)

# Parcourir les matches et extraire les informations souhaitées
matches_info = []

for match in data_from_file["matches"]:
    # Vérifier que la liste contestants n'est pas vide
    if len(match["contestants"]) >= 2:
        team_1 = match["contestants"][0]["name"]
        team_2 = match["contestants"][1]["name"]
        date = match["date"]

        # Extraire les cotes pour chaque équipe
        cotes = {}
        for selection in match["grouped_markets"][0]["markets"][0]["selections"]:
            equipe = selection[0]["name"]
            cote = selection[0]["odds"]
            cotes[equipe] = cote

        match_info = {
            "Team 1": team_1,
            "Team 2": team_2,
            "Date": date,
            "Cotes": cotes
        }

        matches_info.append(match_info)
    else:
        print(f"Match {match['id']} n'a pas suffisamment de concurrents.")

# Écrire les informations des matches dans un fichier JSON
with open('matches_info.json', 'w') as json_output:
    json.dump(matches_info, json_output, indent=4)
 
print("Données JSON sauvegardées dans matches_info.json")
