import re

url_regex = re.compile(
    r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search("http://www.youtube.com/watch?v=wow")
print(match.group(0))
print(f"protocol: {match.group(1)}")
print(f"domain: {match.group(2)}")
print(f"everything else: {match.group(3)}")

url_regex = re.compile(
    r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search("http://www.youtube.com/watch?v=wow")
print(match.groups())
