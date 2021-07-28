
def invert_dict(dictionary):
    new_dict = dict([(value, key) for key, value in dictionary.items()])
    return (new_dict)
language_abbrevs = {"French" : "fr", "English" : "en", "German" : "ge"}

inverted = invert_dict(language_abbrevs)

print(f"inverted = {inverted}")
