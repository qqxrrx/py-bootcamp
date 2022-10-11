import requests as rq

url = "https://icanhazdadjoke.com/search"

rs = rq.get(
    url,
    headers={"Accept": "application/json"},
    params={
        "term": "rain",
        "limit": "100"
    })

data = rs.json()

print(data['results'])
