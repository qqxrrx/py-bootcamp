import re

pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

pat2 = re.compile(r"""
  ^([a-z0-9_\.-]+)   # first part of email
  @                  # single @ sign
  ([0-9a-z\.-]+)     # email provider
  \.                 # single .
  ([a-z\.]{2,6})$    # com, org, net, etc.
""", re.VERBOSE | re.IGNORECASE)  # or "re.X | re.I"

match = pat2.search("test321@yehey.com")
print(match.groups() if match else None)

match2 = pat2.search("Ttest321@Yehey.com")
print(match2.groups() if match2 else None)
