import requests
import json
from datetime import date   

url = "https://api.open-meteo.com/v1/forecast?latitude=41.7281&longitude=1.824&hourly=temperature_2m&forecast_days=1"


resposta = requests.get(url)
if resposta.status_code == 200:
    dades = resposta.json()
    temperatures = dades["hourly"]["temperature_2m"]
else:
    print("Error en la crida a l'API:", resposta.status_code)

max_temp = max(temperatures)
min_temp = min(temperatures)
mitjana_temp = sum(temperatures) / len(temperatures)

resultat = {
"data": str(date.today()),
"max_temp": max_temp,
"min_temp": min_temp,
"mitjana_temp": round(mitjana_temp, 2)
}
nom_fitxer = f"temp_{date.today().strftime('%Y%m%d')}.json"

with open(nom_fitxer, "w") as fitxer:
    json.dump(resultat, fitxer, indent=4)