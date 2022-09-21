
person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person) #prints out the dictionary

print((person['children'])) 

print(person['children'][1]) #prints out betty

#prints out name of cat
print(person['pets']['cat']) #can't do [3] for cats b/c u need to give it a key b/c pets is a dictionary so u need to say 'cat'

#for loop to print out all children
for child in person['children']:
    print(child)

#for loop tp print out names of dogs and cat
for p in person['pets']:
    print(person['pets'][p])





