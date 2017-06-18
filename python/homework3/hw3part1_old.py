#Catherine Sotirakou
#04/11/1988
#"Homework 3"

numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]

#print(len([4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]))

#1) Count how many numbers are in the list. Use a for loop, do NOT use len. 

#print(len(numbers))

value = 0 
for elem in numbers:
  value += 1
print(value, "numbers are in the list.")

#2) Add another number to the list. You can pick the number!-
numbers.insert(2, 8)

#print(numbers)

#3) Count how many even numbers are in the list. Use a for loop.

modulusnumber = 0

for a in numbers:
  if int(a) % 2 == 0:
    modulusnumber += 1
print(modulusnumber, "are even numbers.") 

#4) Count how many values are above the mean and how many are below the mean. 
#Use a for loop.

import statistics as s
s.mean(numbers)
print(s.mean(numbers), "is the mean.")

v = 0
v1 = 0
for i in numbers:
  if i > s.mean(numbers):
    v += 1
  elif i < s.mean(numbers):
    v1 += 1
print(v, "values are above the mean and", v1, "are below the mean.")


#5) Total up the numbers. Use a for loop, do NOT use sum().
#sum(numbers)
#print(sum(numbers))

sum_numbers = 0

for n in numbers:
  sum_numbers += n
print("The sum is:", sum_numbers)

#6) Total up the numbers that are above the mean and the numbers below the mean. 
#Use a for loop, do not use sum().

sum_numbers = 0
sum_numbers_2 = 0
for x in numbers:
  if x > s.mean(numbers):
    sum_numbers += x
  elif x < s.mean(numbers):
    sum_numbers_2 += x
print("Total above", sum_numbers)
print("Total below", sum_numbers_2)

#7) Find the largest number. Use a for loop.

largest= numbers[0]
for large in numbers:
  if large > largest:
    largest=large
print("The largest number is", largest)

#8) You have a list of dogs, shown below. BUT YOU GOT ANOTHER DOG!!! 
#His name is Maxwell, please add him to the list 
#(and no, you don't just add him to the end of that line). Use a for loop.

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]

#dogs.append("Maxwell") #.append adds more than one elements as one (sublist) instead of .extend that adds multiple. 
#or
#dogs = dogs + ["Maxwell"]

dogs += ["Maxwell"]
#print(dogs)

#9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.

dogs_names = []

for dog in dogs:
  if len(dog) <= 5:
    dogs_names += [dog]
print("The list with the dogs that have name of 5 characters or less:", dogs_names)

#10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH
cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

for i in cantons:
  print("http://important-swiss-things.ch/docs/download/{}".format(i))

#11) I'm trying to get some top-secret documents from top-secret-secrets.com,
# and while I know the URL pattern I don't want to type them all out individually!

ids = ['qq7lthm', 'jemsqhg', 'O6itcke', 'cp4Iua0', 'bkijcmo', 'ctoyjrm', 'z8wc6xy', 'zk4Bmm0']
pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#t = ids[1].upper()

for i in ids:
  t = i.upper()
#  print("t: {}".format(t))
  for p in pages:
 #  print('{num:03d}'.format(num=p))
    print("www.top-secret-pdfs.com/content/secrets/%s/page/%03d.pdf" % (t, p) )

#print('{num:03d}'.format(num=i))
