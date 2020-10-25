"""Testing web APIs with HTTP GET method"""

import json
import sys

import requests

def print_coord(address):
    """Retrieve coordinates from Open Street Map"""
    osm = "https://nominatim.openstreetmap.org/search"
    data = {'q': address, 'format': 'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    for item in json_list:
        display_name = item['display_name']
        short_name = display_name.split(", ")[0]
        lat = item['lat']
        lon = item['lon']
        print(f"{short_name} ({lat} - {lon})")

def print_info(country_name):
    """Retrieve country info from REST API"""
    base_url = "https://restcountries.eu/rest/v2/"
    name_url = base_url + "name/"
    code_url = base_url + "alpha/"
    resp = requests.get(name_url + country_name)
    try:
        country = json.loads(resp.text)[0]
        languages = country['languages']
        print(f"Languages: {', '.join([lang['name'] for lang in languages])}")
        border_codes = country['borders']
        border_names = []
        for code in border_codes:
            resp = requests.get(code_url + code)
            border_country = json.loads(resp.text)
            border_name = border_country["name"]
            border_names.append(border_name)
        print(f"Borders: {', '.join(border_names)}")
    except KeyError:
        print("Unknown country, please use English or native name")

def print_sentiment(text_eval):
    """Retrieve sentiment info from text API"""
    # text_eval now takes input from the console, but can later take the extracted text of the bulletins
    base_url = "http://text-processing.com/api/sentiment/"
    param={
        "language":"french",
        "text": text_eval
        }
    resp = requests.post(base_url, data=param)
    # print(f"Status: {resp.status_code}")
    try:
        sentiment = json.loads(resp.text)
        label = sentiment['label']
        print(f"Sentiment tendency of analysed text: {label}")
        probability= sentiment['probability']
        pos = probability['pos']
        neg = probability['neg']
        neutral = probability['neutral']
        print(f"Probability that the text is positive: {pos}")
        print(f"Probability that the text is negative: {neg}")
        print(f"Probability that the text is neutral: {neutral}")
    except KeyError:
        print("Insufficient text to recognise sentiment, please try again")

if __name__ == "__main__":
    try:
        service = sys.argv[1]
        if service == "coord":
            try:
                address = sys.argv[2]
                print_coord(address)
            except IndexError:
                print("Please enter an address")
        elif service == "info":
            try:
                country_name = sys.argv[2]
                print_info(country_name)
            except IndexError:
                print("Please enter a country name")
        elif service == "sentiment":
            try:
                text_eval = sys.argv[2]
                print_sentiment(text_eval)
            except IndexError:
                print("Please enter text")
        else:
            print("Unknown action, please use either 'coord' or 'info' or 'sentiment'")
    except IndexError:
        print("Missing action, please use either 'coord' or 'info'")
