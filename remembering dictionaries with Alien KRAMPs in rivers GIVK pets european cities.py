#Alien KRAMP's in rivers GIVK pets european languages and cities! 30 aliens?
#K is for creating a key-value, which are the building blocks of a dictionary.
alien_0 = {'color' : 'green', 'points' : 5}
#the other way of doing K is to start with an empty dictionary ...
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#R is for removing a pair
del alien_0['points'] #notice things like this tend to follow the order: dictionary, key, value.
#A is for adding a pair.
alien_0['speed'] = 'medium'#notice things like this tend to follow the order: dictionary, key, value.
print(alien_0)
#M is for modifying a key
alien_0['speed'] = 'mach 9'
#P is for printing a key's value in an f-string
print(f"{alien_0['color']}")
#S is for the .set() function which prints keys or values without repeating.
rivers = {
	'nile' : 6853,
	'amazon' : 6400,
	'yangtze' : 6300,
	'amazon' : 6400,
	}
for river in set(rivers.values()):
	print(river)
#G is for the .get() method. The get() method returns the value of an item with the specified key.
x = rivers.get('nile')
print(x)
#I is for the .items() method. It pegs keys, values to a dictionary variable.
for key, value in rivers.items():
	print(f"The river {key.title()} is {value} km's long.")
#V is for the .values() method. It prints the values only.
for kilometers_long in rivers.values():
	print(kilometers_long)
#K (E looks a bit like a K) is for the .keys() method. It prints the keys only.
for river in rivers.keys():
	print(river.title())
	    ### NESTING ###
#A LIST OF DICTIONARIES (i.e. a dictionary inside a list)
pets = []
pet = {
    'animal type': 'cat',
    'name': 'sam',
    'owner': 'bruce annd lee',
    'weight': 8,
    'eats': 'whiskas',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'jazba',
    'owner': 'charlotte',
    'weight': 19,
    'eats': 'chicken',
}
pets.append(pet)
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

#A LIST IN A DICTIONARY (i.e. lists inside a dictionary)
european_languages = {
	'germany' : ['english', 'german'],
	'denmark' : ['danish', 'english', 'german', 'swedish'],
	'poland' : ['polish', 'silesian'],
	}
for country, languages in european_languages.items():
	print(f"\n{country.title()}'s popular langauges are:")
	for language in languages:
		print(f"\t{language.title()}")

#A DICTIONARY WITHIN A DICTIONARY
cities = {
    'berlin': {
        'country': 'germany',
        'population': 3800000,
        'mountain range': 'bavarian alps',
        },
    'copenhagen': {
        'country': 'denmark',
        'population': 1990000,
        'mountain range': 'scandinavian mountains',
        }
    }
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['mountain range'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {mountains} are nearby.")
print('\n')
#30 Aliens?