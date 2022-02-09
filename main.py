import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT = "77"
HEIGHT = "180"
AGE = "28"

APP_ID = os.environ.get("NUT_APP_ID")
APP_KEY = os.environ.get("NUT_APP_KEY")
sheety_endpoint = f"{os.environ.get('SHEETY_ENDPOINT')}"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()



exercise_data = result['exercises'][0]
today = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime("%X")

sheety_header = {
    "Authorization": f"{os.environ.get('SHEETY_AUTH')}",
    # "Username": "cornholio",
    # "Password": "butthole"
}

param = {
    "workout": {
        "date": f"{today}",
        "time": f"{time}",
        "exercise": f"{exercise_data['name'].title()}",
        "duration": f"{exercise_data['duration_min']}",
        "calories": f"{exercise_data['nf_calories']}"
    }
}

response2 = requests.post(url=sheety_endpoint, json=param, headers=sheety_header)

print(response2.text)

