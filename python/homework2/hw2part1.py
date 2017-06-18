 
# Catherine Sotirakou
#05/24/2017
#"Homework 2, Part 1"
#1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]
#2) Display the number of elements in the list.
print("The numbers of the elements is", len(numbers))
#3) Display the 4th element of this list.
print("The 4th element is:", numbers[3])
#print(numbers.count)

#4) Display the sum of the 2nd and 4th element of the list.

print("The sum is", numbers[1] + numbers[3])  
 
#5) Display the 2nd-largest value in the list.
# sorted list goes from lowest to highest so the max will be -1
second_max = sorted(numbers)[-2]
print("The 2nd largest is:", second_max)
 
#6) Display the last element of the original unsorted list
print("The last element of the original unsorted list", numbers[-1])
 
#7) For each number, display a number: if your original number is less than 10, multiply it by thirty. If it's also even, add six. If it's greater than 50 subtract ten. If it's not negative ten, subtract one. (For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even, so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)
#number = input ("Insert a number")
#print(number)
#number = int(number)

for number in numbers:
  value = number
  if number < 10:
      value = number * 30
      if number % 2 == 0:
          value = value + 6
  if number > 50:
      value = number - 10
  if number != -10:
      value = value -1
  print(value)


#8) Display the sum of all of the numbers divided by two.
print("The sum divided by two is", sum(numbers) / 2 ) 

#8 Dictionary 
movie = {
  'title':"The Prestige",
  'year' :"2006",
  'director': "Christopher Nolan"
}

print("My favorite movie is", 
  movie['title'], 
  "which was released in", 
  movie['year'], 
  "and was directed by", 
  movie['director'])

#9

movie.update({'budget': 40000000})
movie.update({'revenue': 109000000})

print ("The difference between revenue and budget is", int(movie['revenue']) - int(movie['budget']), "dollars")

#10

if int(movie['budget']) > int(movie['revenue']):
 print("It was a flop")
elif int(movie['revenue']) - int(movie['budget']) > 5 * int(movie['budget']): 
 print("That was a good investment.")
else:
 print("Box office was just ok")


#11
state_populations = {
  'Manhattan': 1600000,
  'Brooklyn': 2600000,
  'Bronx': 1400000,
  'Queens': 2300000,
  'Staten Island': 470000
}

#print(state_populations.keys())

#12 Display the population of Brooklyn.

print(state_populations['Brooklyn'], " residents is the population of Brooklyn.")

#13) Display the combined population of all five boroughs.
total_pop = sum(state_populations.values())

print("The combined population of all five boroughs is", sum(state_populations.values()), "residents.")
#14) Display what percent of NYC's population lives in Manhattan.
per = ((state_populations['Manhattan'] / total_pop ))*100

#print ("%.2f of NYC's population lives in Manhattan." %per)
print ("%.0f %% of NYC's population lives in Manhattan." %per)
