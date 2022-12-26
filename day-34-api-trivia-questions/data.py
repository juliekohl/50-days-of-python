from typing import List, Any
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data: Any = response.json()
question_dataList: List[str] = data["results"]
