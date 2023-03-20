# Creating a dictionary called people.
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}

# Finding the max value in the dictionary and then finding the key associated with that value.
max_value = max(people.values())
max_key = max({k for k,v in people.items() if v == max_value})
print(max_key,max_value)

# solution 2
kv = ({k:v for k,v in people.items() if v == max(people.values())})
print(kv)

# Creating a new dictionary called people_x2. It is taking the values from the people dictionary and
# multiplying them by 2.
people_x2 = {k:v*2 for k,v in people.items()}
print(people_x2)

# Print enumerate key in people dict
list_people = list(enumerate(people))
print(list_people)

# Create dict from list
people_dict = dict(list_people)
people_dict1 = {k : v for k, v in list_people}
print(people_dict)
print(people_dict1)





