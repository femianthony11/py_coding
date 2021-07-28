from googletrans import Translator, constants
from pprint import pprint



def runt(phrase,language,langdict):
    translator = Translator()
    translation = translator.translate(phrase,dest = langdict[language.lower()])
    return (f"{translation.text}")



def main():
    s = input("Please enter source Language: ")
    p = input("Please enter Phrase: ")
    l = input("Please enter Destination Language: ")
    langlist = ['english','en','french','fr','afrikaans','af','german','de','latin','la','swahili','sw','yoruba','yo','portuguese','pt','spanish','es','zulu','zu']
    langdict = {'english':'en','french':'fr','afrikaans':'af','german':'de','latin':'la','swahili':'sw','yoruba':'yo','portuguese':'pt','spanish':'es','zulu':'zu'}
    if l.lower() not in langlist:
        print('Invalid Language')
        quit()
    print(runt(p,l,langdict))


if __name__ == "__main__":
    main()
