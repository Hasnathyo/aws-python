

# cities = {"Manchester": "England" " 500,000",
#             "Cardiff": "Wales" " 340,000",
#             "Valencia": "Spain" " 790,000"}


# for city,description in cities.items():
#     print(city,description)

cities = {"Manchester" : {"Info" : {"Size" : "500,000",
                                    "Country" : "England"}},
            "Cardiff" : {"Info" : {"Size" : "340,000",
                                    "Country" : "Wales"}},
            "Valencia" : {"Info" : {"Size" : "790,000",
                                    "Country" : "Spain"}}}
for city in cities.keys():
    print(city)
    print(cities[city]["Info"]["Size"])
    print(cities[city]["Info"]["Country"])