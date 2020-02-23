from collections import OrderedDict

favourite_language = OrderedDict()

favourite_language['jen'] = 'python'
favourite_language['pi'] = 'c'
favourite_language['kitty'] = 'Java'


for name, language in favourite_language.items():
    print(name, language)

from random import randint

x = randint(1, 6)

for i in range(100):
    print(str(randint(1, 6)) + " ")