from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>1st html page</title>
</head>
<body>
    <div id="first">
      <h3>nice</h3>
      <h3 data-example="yes">hi</h3>
      <p>more text.</p>
    </div>
    <ol>
      <li class="special super-special">This list item is special.</li>
      <li class="special">This list item is also special.</li>
      <li>This list item is not special.</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
for el in soup.select(".special"):
    print(el.get_text())
    print(el.name)
    print(el.attrs)
    print(type(el))


h3s = soup.find_all("h3")
print(h3s)
for h3 in h3s:
    if "data-example" in str(h3):
        print(h3["data-example"])

print(soup.find("div")["id"])
