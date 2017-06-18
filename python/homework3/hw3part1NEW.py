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

#for i in ids:
 # t = i.upper()
  #print("t: {}".format(t))
#for p in pages:
 # print('{num:03d}'.format(num=p))
  #print("www.top-secret-pdfs.com/content/secrets/{}".format(t), '/page/', int('{num:03d}'.format(num=i)), ".pdf")
for i in ids:
  t = i.upper()
#  print("t: {}".format(t))
  for p in pages:
 #  print('{num:03d}'.format(num=p))
    print("www.top-secret-pdfs.com/content/secrets/%s/page/%03d.pdf" % (t, p) )

#print('{num:03d}'.format(num=i))
#print('{num:03d}'.format(num=i))

#PART TWO: Dictionaries
#1) Let's say we are terrible doctors and we have a patient. 
#Define a dictionary called patient that works with the following code.
patient = {
'name': '',
'complaint':'', 
}
print("Doctor, it looks like the patient's is complaining about", patient['complaint'])

#2) We aren't really listening to their complaint, but as more test results come in,
#we'll add these things to the patient's record. Add the following to the patient dictionary:

patient.update({'Heart rate': 70, 'Temperature': 98.6, 'Infection': 'No'}) 

print(patient.keys())

#3) Now let's be doctors! First, if they have a heart rate about 100, 
#we should tell them to relax. Store your diagnosis in a key called 'diagnosis'.
patient.update({'diagnosis':''})

#* If their temperature is above 102 but they do not have an infection, they have heat stroke.
#* If they have a high temperature and they have an infection, they have the flu.
#* If they have an infection but no high temperature, it's probably a cold.
#* If none of the above, tell them to take an aspirin and call you in the morning.

#When you are finished, print "Your diagnosis is _______."


patients = [{'name': 'Dean', 'Heart rate': 67, 'Temperature': 109, 'Infection': 'No', 'complaint': 'pain'}, {'name': 'Mark', 'Heart rate': 70, 'Temperature': 98.6, 'Infection': 'No', 'complaint': 'pain'}, {'name': 'Susan', 'Heart rate': 110, 'Temperature': 105, 'Infection': 'Yes','complaint': 'pain'}] 

print(patients)

for patient in patients:
    patient['diagnosis'] = "Take an aspirin and call you in the morning!"
    if patient['Heart rate'] > 100:
       advice = "You should relax"
       print("%s %s" % (patient['name'], advice) )
    if patient['Temperature'] > 102: 
      if patient['Infection'] == 'No':
        patient['diagnosis'] = "Your diagnosis is a heat stroke"
      elif patient['Infection'] == 'Yes':
        patient['diagnosis'] = "Your diagnosis is  the flu"
    elif patient['Temperature'] < 102:
      if patient['Infection'] == 'Yes':
        patient['diagnosis'] = "Your diagnosis is   a cold"
    print("%s , As a doctor I tell you that:  %s" % (patient['name'], patient['diagnosis']) )


temperatures = [ 99, 105 ]

records = []
for patient in patients:
   records.append(patient['diagnosis'])

#edw thelw oles tis diagnoseis mazemenes!!!! pairnei mono tin teleutaia!
print(records)
print("---------------------------------------")

for record in records:
  if record == 'Your diagnosis is a heat stroke': # edw eprepe na valw mono to 'heat stroke'
    print("This patient has heat stroke!")
  else:
    print("This patient does not have heat stroke")
