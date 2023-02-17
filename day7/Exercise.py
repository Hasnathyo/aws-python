#Create a class for students of GenUni
#should have attributes for first and last name of students
#the third attribute should be for email which is concatenating...
#first_name.last name@genuni.co.uk
#Print the students first name, last name and email

#create a method that generates the student's ID by conncatenating the 
#students first and last names with their birth months as a parameter
#when you call the method

class Students():
    def __init__(self,first_name,last_name,birth_month):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name + "@genuni.co.uk"
        self.student_id = first_name + last_name + birth_month

    def favourite_quote(self,quote):
        return f"{self.first_name}'s favourite quote is {quote}"

student1 = Students("Hasnath","Khan","07")
student2 = Students("Emad","Saeed","12")

print(student1.student_id)
print(student2.student_id)