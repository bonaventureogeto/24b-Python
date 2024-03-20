import re

# pattern = re.compile('^Hello')

# result = pattern.sub('Hi', 'Hello World, Hello, Kenya')

# print(result)

# (?\d{3})?[-.\s]?\d{3}[-.\s]?\d{4} -> +254 797 111 340

# \d -> 0, 9
# \w -> 0-9, a-z, A-Z, _
# \s -> whitespace characters
# [] ->
# () -> grouping
# *
#

text = "This is my phone number +254-234-098-134"

pattern = r"\+\d{3}-\d{3}-\d{3}-\d{3}"


result = re.search(pattern, text)

# print(result)


sentence = "define a regex pattern for the phone number (+254) 098 1134, (+254).098.1234, (+254)-098-5134"

phone = "(123) 456-7890"

phone_pattern = r"\(\+\d{3}\)\s\d{3}\s\d{3}\s\d{3}"

phone2_pattern = r"\(\+?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

print(re.findall(phone2_pattern, sentence))
