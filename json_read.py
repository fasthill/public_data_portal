import requests
import json
import pandas as pd

res = requests.get("http://api.open-notify.org/astros.json")
json_data = json.loads(res.content)

df = pd.DataFrame(json_data['people'])
print(df)