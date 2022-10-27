import re


def parse_name(input):
    # ?P<...> = label for the group
    name_regex = re.compile(
        r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first_label>[A-Za-z]+) (?P<last_label>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.group('first_label'))
    print(matches.group('last_label'))


parse_name("Mrs. XXX YYY")
