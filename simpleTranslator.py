from googletrans import Translator, constants
from pprint import pprint


def invert_dict(dictionary):
    #function to invert dicts
    new_dict = dict([(value, key) for key, value in dictionary.items()])
    return (new_dict)

def runt(phrase,language,langdict):
    #run function to translate phrases
    translator = Translator()
    translation = translator.translate(phrase,dest = langdict[language])
    return (f"{translation.text}")



def main():
    #prints available languages
    print("""This is the available list of languages: 
        England:1  
        French: 2  
        Afrikaans: 3
        German: 4 
        Latin: 5 
        Swahili: 6 
        Yoruba: 7  
        Portuguese: 8 
        Spanish: 9 
        Zulu: 10 
            """)
    #asks for inputs
    s = input("Please enter source Language: ")
    p = input("Please enter Phrase: ")
    l = input("Please enter Destination Language: ")
    langlist = ['english','en','french','fr','afrikaans','af','german','de','latin','la','swahili','sw','yoruba','yo','portuguese','pt','spanish','es','zulu','zu','yo', 'yoruba']
    langdict = {'english':'en','french':'fr','afrikaans':'af','german':'de','latin':'la','swahili':'sw','yoruba':'yo','portuguese':'pt','spanish':'es','zulu':'zu','yo': 'yoruba'}
    langsdict = {'english': 1 ,'french': 2 ,'afrikaans':3,'german':4,'latin':5,'swahili':6,'yoruba':7,'portuguese':8,'spanish':9,'zulu':10,'yo': 'yoruba'}
    inverted = invert_dict(langsdict)
    l = (inverted[int(l)])

#    if l.lower() not in langlist:
 #       print('Invalid Language')
  #      quit()
    print(runt(p,l,langdict))


if __name__ == "__main__":
    main()
