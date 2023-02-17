ages = [15,12,18,20,25,30,22,28]

def reverse_list(list):
    list.sort(reverse = True)
    print (list)

reverse_list(ages)

#return function
def squared(age):
    square = [(x)**2 for x in age]
    return (square)

new = squared(ages)
print(new)


