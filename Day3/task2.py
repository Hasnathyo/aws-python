#print cube of odd numbers between 1-10
#print the square of the remainder between 10 - 20 when divided by 3 using list comprehension
# x % 3

#oddnumbers = list(range(1,11,2))
#print(oddnumbers)

#numbers = list(range(10,21))

#print the square of the remainder between 10 - 20 when divided by 3 using list comprehension
square = [(i %3)**2 for i in range (10,21)]
print (square)