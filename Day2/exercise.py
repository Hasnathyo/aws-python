#create a list of 10 items
items = ["Baguette", "Croissant", "Tea", "Coffee", "Milk", "Almonds", "Pistachio", "Cashews", "Cakes", "Cookies"]
#save 5th item as a variable
five = items[4]
#insert it into beginning of the list
items.insert(0,five)
print (items)
#sort the list in reverse order
items.sort(reverse=True)
#items.reverse()
print(items)

