python_dictionary={
    "bug":"an error in the program that prevents the program running as expected.",
    "function":"A piece of code that you can call over again and again.",
}

# Retrieving items from dictionary.
print(python_dictionary["function"])

# Adding new items to the dictionary.
python_dictionary["loop"]="The action of doing something over and again."
print(python_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# python_dictionary = {}
# print(python_dictionary)

# Edit an item in a dictionary
python_dictionary["bug"]="A moth in computer."
print(python_dictionary)

# Loop through a dictionary
for thing in python_dictionary:
    print(thing)
    print(python_dictionary[thing])

# Nesting
nest={
    "key":["list",],
    "key2":{"Dictionary",},
}
capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

# Nesting a list in a dictionary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log_dictionary={
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5},
}

# Nesting a dictionary in a List
travel_log_list=[
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["total_visits"]=times_visited
    new_country["cities_visited"]=cities_visited
    travel_log_list.append(new_country)

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log_list )