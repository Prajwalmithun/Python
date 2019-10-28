# abbrevation of state with abbrevation
states = {
    'Karnataka' : 'KAR',
    'Tamil Nadu' : 'TN',
    'Kerala' : 'KER',
    'Andhra Pradesh' : 'AP'
}

cities = {
    #'KAR' : 'Mysore',
    #'TN' : 'Chennai',
    'KER' : 'Wayand',
    'AP' : 'Hyderabad'
}

#adding some more cities
cities['KAR'] = 'Bangalore'
cities['TN'] = 'Vellore'

#printing cities
print('-' * 10)
print('KAR state has : ',cities['KAR'])
print('AP state has : ',cities['AP'])

#printing states
print('-' * 10)
print('Karnataka abbrevation is :', states['Karnataka'])

# from state to city
print('-' * 10)
print('Karnataka has :', cities[states['Karnataka']])
print('Andhra Prades has :', cities[states['Andhra Pradesh']])

# print state and its abbrevation
print('-' * 10)
for state, abbr in states.items():
    print('{} is abbrevated as {}'.format(state, abbr))

# print ecery city in state
print('-' * 10)
for abbr, city in cities.items():
    print('{} has city {}'.format(abbr,city))

# now doing both at the same time
print('-' * 10)
for state, abbr in states.items():
    print('{} is abbrevated as {}'.format(state,abbr))
    print('has city {}'.format(cities[abbr]))

# get the abbrevation which is not existing in the dictionary
print('-' * 10)
state = states.get('Goa')

if not state:
    print('Sorry , No Goa')

# get city with default value
city = cities.get('GO','Does NOt Exist')
print("The city for the state 'GO' is : {}".format(city))