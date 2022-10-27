import re

text = "Mrs. First ate icecream from Mr. Second place and Ms. Third found out and got mad"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.IGNORECASE)
# \g<???>   ??? = capture group
newtext = pattern.sub("(\g<1> \g<2>)", text)
print(newtext)
