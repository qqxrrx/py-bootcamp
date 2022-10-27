import re


def extract_phone(input):
    # \b = boundary
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    return match.group() if match else None

# print(extract_phone("hohoho 111 111-1111"))
# print(extract_phone("hohoho 111 111-1111000"))


def extract_all_phones(input):
    # \b = boundary
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    return match if match else None

# print(extract_all_phones("hohoho 111 111-1111 or 232 111-5232"))
# print(extract_all_phones("hohoho 111 111-1111000 "))


# def is_valid_phone(input):
#     # ^ = has to start
#     # $ = has to end
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     return True if match else False

def is_valid_phone(input):
    # ^ = has to start
    # $ = has to end
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.fullmatch(input)
    return True if match else False


print(is_valid_phone("111 111-1111"))
print(is_valid_phone("111 111-1111 wow"))
print(is_valid_phone("hehe 111 111-1111"))
