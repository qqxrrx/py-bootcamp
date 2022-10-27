import re


titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Micheal Tolliver Lives (2007)",
]

titles.sort()
fixed_titles = []


# 2nd capture group only takes the digits and ignores the parenthesis (because it is outside)
pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')

for book in titles:
    result = pattern.sub("\g<date> - \g<title>", book)
    fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)
