import requests as rq

url = "https://news.ycombinator.com"
rs = rq.get(url)
print(rs.status_code)
