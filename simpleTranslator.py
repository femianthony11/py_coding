from googletrans import Translator, constants
from pprint import pprint
phrase = input("Please enter phrase in English: ")
language = input("Please enter Language: ")
langlist = ['french','fr','afrikaans','af','german','de','latin','la','swahili','sw','yoruba','yo','portuguese','pt','spanish','es','zulu','zu']
langdict = {'french':'fr','afrikaans':'af','german':'de','latin':'la','swahili':'sw','yoruba':'yo','portuguese':'pt','spanish':'es','zulu':'zu'}

translator = Translator()

if language not in langdict:
    print('Invalid Language')
    quit()

translation = translator.translate(phrase,dest = langdict[language.lower()])

print(f"{translation.text}")
