import requests
import json
import pandas as pd

res = requests.get("http://api.open-notify.org/astros.json")

json_data = res.json()
# json_data = json.loads(res.content)
# json_data = json.loads(res.text)

df = pd.DataFrame(json_data['people'])
print(df)