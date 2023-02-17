people = {"Frank": "5",
            "Andy": "10",
            "Josh": "2",
            "Ronnie": "32",
            "Jordan": 8}

dict_items = people.items()

for keys,values in dict_items:
    print(keys,"'s favourite number is",values)