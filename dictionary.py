# dictionary -> data structure that allows you to store data in a key-value format

words = {
    "City": "Big town with a population of over 5 Million",
    "Continent": "A geographical location the size of over 1M Square KMs"
}

# print(words["City"])
# print(words.get("City"))

words["Continent"] = "sfjsdjf mdfbisdgfuisd fjbdfyusdgf"
# print(words["Continent"])

# print(words.keys())
# print(words.values())

new_words = {
    "Kenya": "Country",
    "Heaven": "Place"
}

words.update(new_words)

# print(words)

# challenge: write a python function called create_word() that creates an empty dictionary. Create another function called add_word() that adds words in key-value pairs to the empty dictionary created above.


def create_word():
    empty_dict = {}
    return empty_dict


def add_word():
    dictionary = create_word()
    dictionary.update(words)
    return dictionary


print(add_word())
