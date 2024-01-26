#import libraries
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd



car_data_list = []
#url of the target website
for i in range(1,6):
    url = f"https://www.pakwheels.com/used-cars/peshawar/24821?page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    car_data = soup.find_all("li", class_ = "classified-listing")
    for car_item in car_data:
        script_tag = car_item.find("script", type="application/ld+json")
        if script_tag:
            car_json = json.loads(script_tag.string)

            description = car_json.get("description")
            item_condition = car_json.get("itemCondition")
            model_date = car_json.get("modelDate")
            manufacturer = car_json.get("manufacturer")
            fuel_type = car_json.get("fuelType")
            name = car_json.get("name")

            # Print or store the extracted data as needed in a list
            car_data_list.append({
                "description": description,
                "item_condition": item_condition,
                "model_date": model_date,
                "manufacturer": manufacturer,
                "fuel_type": fuel_type,
                "name": name
            })

car_df = pd.DataFrame(car_data_list)    
