import requests
import re
from dotenv import load_dotenv
import os

def convert_units(**kwargs):
    load_dotenv()
    source = kwargs.get("from")
    target = kwargs.get("to")

    match_source = re.match(r"(\d+)([a-zA-Z]+)", source)
    if not match_source:
        print("Invalid '--from' format. Use like 10ft")
        return

    value, unit_from = match_source.groups()
    unit_to = target

    api_url = f"https://api.api-ninjas.com/v1/convertunit?value={value}&from={unit_from}&to={unit_to}"
    api_key = os.getenv("UNIT_CONVERSION_API_KEY")
    headers = {"X-Api-Key": api_key} 

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        result = data.get("new_value", None)
        if result:
            print(f"{result} {unit_to}")
        else:
            print("Conversion failed.")
    else:
        print("Error calling API:", response.text)
