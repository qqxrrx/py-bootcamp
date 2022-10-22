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
print("\n .select() uses css selectors and always returns a list")

print("\nretrieve by id:")
d = soup.select("#first")
print(d)
print(type(d))  # resultset is a list, therefore use index

print("\nretrieve by element:")
d = soup.select("div")
print(d)

print("\nretrieve by attribute:")
d = soup.select("[data-example='yes']")
print(d)
