import csv
csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()



#1
#for i in data:
    #print(i)

print(data[0].keys())
# ['Country', 'Continent', 'GDP_per_capita', 'life_expectancy', 'Population']

#2

value = 0
for o in data:
  value += 1
print(value)

#3 How many countries in Asia? How about North America?
val = 0
val1 = 0
for u in data:
  art = u['Continent']
  if (art == 'Asia'):
    val += 1
  elif (art == 'N. America'):
    val1 += 1

print(val, "countries are in Asia and", val1, "in North America.")

#print(data)

#4) What is the total population of the world?

sum_pop = 0

for l in data:
  k = int(l['Population'])
  sum_pop += k
print(sum_pop)
