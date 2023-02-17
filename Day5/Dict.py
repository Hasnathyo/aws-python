#Dictionary

#indents are only there to make it look cleaner 
student = {"name":"Ibrahim",
            "location":"Manchester",
            "food":("pasta, chicken"),
            "height": 185, 
            "favourite_colour":["blue","green", {"favourite_shade":"navy"}],
            "address":{"street":"123 Generation Street",
            "post_code":"GH2 345",
            "city":"Manchester"}}

address = student["address"]
#changing things in a dictionary
student["location"] = "London"
student["address"]["city"] = "London"
student["favourite_colour"][2]["favourite_shade"] = "teal"
#cant edit a tuple so change the whole thing
student["food"] = ("cheese","burger")


#print(student.keys()) #only prints out the keys
#print(student.items()) #only prints out the items
#print(student.values()) #only prints out the values

dict_keys = student.keys()
dict_val = student.values()
dict_items = student.items()

for keys,values in dict_items:
    print(keys,"<<item",values,"<<value")