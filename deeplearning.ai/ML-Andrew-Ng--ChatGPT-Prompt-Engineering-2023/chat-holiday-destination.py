import json
from util_chat import send_prompt
from util_json import save_json_to_file

prompt = f"""
Your task is to provide a list of top 5 summer holiday destinations.

The criteria are outdoor sports, beautiful landscapes, temperate weather, located in Europe.

The output should be in JSON format and include the fields: country, month, region, closest_airport, average_temperature, summary, public_image_url

"""

rsp = send_prompt(prompt)
save_json_to_file(json.loads(rsp), "./data/holiday-destinations.json")
