#create a list of numbers called ages
#create another empty list called new_age
#write a for loop to append
#the value of the square of ages
#print your new list

ages = [45,35,23,41,29]
new_age = []
ages.sort()
for x in ages:
     new_age.append(x%5)
print(new_age)

#sort is permenant, sorted is temporary
#print (ages)
