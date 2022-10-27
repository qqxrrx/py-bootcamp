import re

# r'' = raw string, to just use regular backslashes
pattern = re.compile(r'\d{3} \d{3}[-? ]\d{4}')

# return 'None' if pattern not found, only returns 1st occurance
res = pattern.search("call now at 111 111-1111 or 222 222 2222!")
print(res.group() if res else 'not found')

# returns all occurances
res = pattern.findall("call now at 111 111 1111 or 222 222-2222!")
print(res)
