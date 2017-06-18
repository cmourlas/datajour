

# Catherine Sotirakou
#05/24/2017
#"Homework 2, Part 2"

#LISTS

#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = ['Canada', 'Ukraine', 'Georgia', 'Portugal', 'Mexico', 'Italy', 'Austria']

#2) Using a for loop, print each element of the list

for country in countries:
  print(country)

#3) Sort the list permanently.

countries.sort()
print(countries)

#4) Display the first element of the list.
print(countries[0])

#5) Display the second-to-last element of the list.

print(countries[-2])

#6) Delete one of the countries from the list using its name.

del countries[2]
print(countries)
#7) Using a for loop, print each country's name in all caps.

#print("countries".upper())

for i in countries:
  print(i.upper())

#DICTIONARIES

# + + = North/East
# + - = North/West
# - - = South/West
# - + = South/East 
#https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8
#1) Make a dictionary called 'tree' that responds to 
tree = {
'name': 'Jaya Sri Maha Bodhi', 
'species': 'Sacred fig', 
'age': '2300', 
'location_name': 'Sri Lanka',
'latitude': 7873054,
'longitude': 80771797
}

#print(tree.keys())

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"


print(tree ['name'], "is a", tree['age'], "years old tree that is in", tree['location_name'])

#3) The coordinates of New York City are 40.7128 N, 74.0059 W. Check 
#to see if the tree is south of NYC, and print 
#"The tree {name} in {location} is south of NYC" if it is. 
#If it isn't, print "The tree {name} in {location} is north of NYC"

nyc = {
'latitude': 407128,
'longitude': -80771797
}

if nyc['latitude'] < tree['latitude']:
  print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC")
else:
  print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC")

#4) Ask the user how old they are. 
#If they are older than the tree, display "you are {XXX} years older than {name}." 
#If they are younger than the tree, display "{name} was {XXX} years old when you were born."

user_age = input("How old are you?")

print(user_age)

if int(user_age) > int(tree['age']):
  print( "You are", abs(int(user_age) - int(tree['age'])), "years older than", tree['name'])
else:
  print("You are", abs(int(tree['age']) - int(user_age)), "years younger than", tree['name'])

#PART TWO: Lists of dictionaries

#1) Make a list of dictionaries of five places across the world 
#- (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. 
#Each dictionary should include each city's name and latitude/longitude (see note above).
#places = ['Moscow', 'Tehran', 'Falkland Islands', 'Seoul', 'Santiago']

cities = [
{
'name':"Moscow", 
'latitude': 55755826,
'longitude': 37617300
},

{
'name':"Tehran", 
'latitude': 35689197,
'longitude': 51388974
},

{
'name':"Falkland Islands", 
'latitude': -51796253,
'longitude': -59523613
},

{
'name':"Seoul", 
'latitude': 37566535,
'longitude': 126977969
},

{
'name':"Santiago", 
'latitude': -33448890,
'longitude':-70669265
}

]

#2) Loop through the list, printing each city's name 
#and whether it is above or below the equator (How do you know? Think hard about the latitude.).
 #When you get to the Falkland Islands, also display the message 
 #"The Falkland Islands are a 
#biogeographical part of the mild Antarctic zone,
#" which is a sentence I stole from Wikipedia.

#for a in cities:
  #if cities['latitude'] > 0:
    #print("it is above equator")
  #elif cities['latitude'] < 0:
    #print("it is below equator")
  #elif cities['latitude'] == -51796253:
    #print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")

#3) Loop through the list, 
#printing whether each city is north of south of your tree from the previous section.

for loc in cities:
  if loc['latitude'] > tree['latitude']:
    location_to_tree = 'above'
    print location_to_tree
  elif loc['latitude'] < tree['latitude']:
    location_to_tree = 'below'
    print location_to_tree
  

