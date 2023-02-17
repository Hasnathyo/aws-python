#lists
#tupple
#dictionary

#list = a group of values [] that are treated as one entity

##names = ["Billal", "Ryan", "Ibrahim", "Dyeshikey"]
##print(names, "class type of names:", type(names))

#can have multiple data types in a list
##new_list = [12, 1.5,[1,2,3,4], "Hasnath", True, False]
#len counts the number of items in a list or string or more idk
##print (len(new_list))

names = ["Billal", "Ryan", "Ibrahim", "Dyeshikey"]
names[2] = "Umar"
#append adds to the end of the list
#insert adds where you specify: names.insert(2,"Alex")
names.insert(2,"Alex")
names.sort()
print(names)