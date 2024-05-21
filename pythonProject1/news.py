import requests
from keys import key  # Ensure your key is defined as a string in keys.py

api_address = "http://newsapi.org/v2/top-headlines?country=us&apikey=" + key
response = requests.get(api_address)
j_data = response.json()

# Debugging: Print the response JSON to see its structure
#print(j_data)

def news():
    ar = []
    if 'articles' in j_data:
        for i in range(min(5, len(j_data['articles']))):
            ar.append("number " + str(i+1) + ": " + j_data["articles"][i]["title"] + ".")
    else:
        print("No 'articles' key in the response JSON.")
    return ar

#arr = news()
#print(arr)

