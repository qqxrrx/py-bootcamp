import requests as rq

url = "https://icanhazdadjoke.com/"

rs = rq.get(url, headers={"Accept": "application/json"})

data = rs.json()  # python dictionary

print(data['joke'])
