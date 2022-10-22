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
      <h3 data-example="yes">hi</h3>
      <p>more text.</p>
    </div>
    <ol>
      <li class="special">This list item is special.</li>
      <li class="special">This list item is also special.</li>
      <li>This list item is not special.</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
print("\nget 1st instance of div:")
print(soup.body.div)

print("\nget 1st instance of div, .find() returns class of bs4.element.Tag:")
d = soup.find("div")
print(d)
print(type(d))

print("\nreturn list of all div:")
d = soup.find_all("div")
print(d)

print("\nretrieve by id:")
d = soup.find(id="first")
print(d)

print("\nretrieve by class:")
d = soup.find_all(class_="special")
print(d)

print("\nretrieve by attribute:")
d = soup.find_all(attrs={"data-example": "yes"})
print(d)
