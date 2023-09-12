programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary
#print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary[
    "Loop"] = "The action of doing something again and over again."
#print(programming_dictionary)

#Create an empty dictionary.
empty_dicrtionary = {}

# empty_dicrtionary[1] = "Putting the first item in this dictionary."
# print(empty_dicrtionary)

# #Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary.
programming_dictionary["Bug"] = "The moth in your computer."
#print(programming_dictionary)

#lOOP through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#Nested List in a Dictionary
travel_list_dic = {
    "France": ["Paris", "Lille", "Dijan"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
#Nested Dictionary in a Dictionary
travel_dic_dic = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijan"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 6
    }
}
#print(travel_dic_dic)

#Nested Dictionary in a List
travel_log = [{
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijan"],
    "total_visits": 12
}, {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 6
}]
print(travel_log[1])