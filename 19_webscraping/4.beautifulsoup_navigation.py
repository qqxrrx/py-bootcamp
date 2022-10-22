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
    <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
data = soup.body.contents[1].contents  # start at index 1 because of '\n'
print(data)

print("\n-----------")
data = soup.body.contents[1].next_sibling.next_sibling  # avoid '\n'
print(data)

print("\n-----------")
data = soup.find(class_="super-special").parent.parent
print(data)


# find methods skips '\n' and goes into an actual object

print("\n-----------")
data = soup.find(id="first").find_next_sibling()
print(data)

print("\n-----------")
data = soup.find(id="first").find_next_sibling().find_next_sibling()
print(data)

print("\n-----------")
data = soup.select("[data-example]")[1].find_previous_sibling()
print(data)

print("\n-----------")
data = soup.find(class_='super-special').find_next_sibling(class_="special")
print(data)

print("\n-----------")
data = soup.find("h3").find_parent("html")
print(data)
