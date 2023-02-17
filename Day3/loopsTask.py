#generate a list of even numbers from 1-20
#print out the square of the even numbers
#put everything into a new list called squares

numbers = list(range(2,21,2))
print(numbers)
num = []

#for n in numbers:
    #num.append(n)
    #print (n**2)

# [<result> for <iterator> in <list>]
loop = [n**2 for n in numbers]
print (loop)