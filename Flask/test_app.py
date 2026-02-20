import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Temp': 30,
    'Humidity': 70,
    'Cloud_Cover': 5,
    'ANNUAL': 3000, 
    'Jan_Feb': 50,
    'Mar_May': 200,
    'Jun_Sep': 2000,
    'Oct_Dec': 750,
    'avgjune': 250,
    'sub': 1500
}

try:
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Response received successfully.")
        if "FLOOD WARNING" in response.text:
            print("Prediction: FLOOD DETECTED (chance.html rendered)")
        elif "You are Safe" in response.text:
            print("Prediction: NO FLOOD (no chance.html rendered)")
        else:
            print("Prediction unclear. Saving response.")
            with open("response_debug.html", "w", encoding="utf-8") as f:
                f.write(response.text)
    else:
        print(f"Failed with status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
