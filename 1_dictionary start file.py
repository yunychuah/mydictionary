import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook)) #type allows you to know what type of object u r dealing w 

phone = phonebook['Chris']

print(phone)

print(len(phonebook)) #will show 3 if there are 3 elements in the phonebook

mydictionary = dict(m=8, n=9) #dict funciton, m=8 is a key value pair, when you print it out u see that values are m and n and are strings and keys are 8 and 9 and integers

print(mydictionary)

mydict = {} #creates an empty dictionary and u can keep adding to it 

print(mydict)

print()
print('*****  end section 1 ********')
print()



print()
print('*****  start section 2 - search dictionary ********')
print()


name = 'Chris'

if name in phonebook: 
    print(phonebook[name]) 
else:
    print(name, 'not found') #if you can't find the name in phonebook 


print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()


print(phonebook)
phonebook['Chris'] = '555-0123' #b/c chris exists in dictionary, so it will update from 1111 to 0123
phonebook['Joe'] = '555-4444' #Joe can't be found in dictionary so will add entire key value pair to dictionary



print()
print('*****  end section 3 ********')
print()



print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


del phonebook['Chris']
print(phonebook)



print()
print('*****  end section 4 ********')
print()



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook: #key is not a reserved word u can change key to k and as long as u change the other 2 keys below to k it will still produce results
    print(key) #defalut option ot iterate through dictionary is to iterate through keys so if u want to iterate vlaues u hv to specifically call it 
    print(phonebook[key])#prints out corresponding values(phone numbers) to katie joanne and joe 


for value in phonebook.values(): #.values b/c u want it to cycle through all the values to find the phone number
    print(value)


for k,v in phonebook.items(): #reminder that k and v are just variable names and u can name these whatever 
    print('key:',k, ' value: ', v)


for tuple in phonebook.items(): #for if you did not split it up 
    print(tuple) #if method returns a tuple u can split it up by giving it multiple variables, know its a tuple b/c of the parentheses which means these are immutable objects(Can't change them)
                    #in dictionaries keys are mutable but values are immutable 

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print() #clear method clears out all the elements 

phone = phonebook.get('Chris', 'key not found') #warning this is case sensitive so no chris only Chris uppercase
print(phone)

phonebook.clear()
print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print() #allows u to remove key value pair from your dictionary 

remove = phonebook.pop('Chris' , 'key not found')

print(remove)

print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

print(phonebook)
a = phonebook.popitem()

print(a)
print(phonebook)



print()
print('*****  end section 8 ********')
print()


''''''
print()
print('*****  start section 9 - using random and converting to list ********')
print() #use random aspect of a list 
#random.choice will pick a random element in your list

list_of_keys = list(phonebook) #creates list w phonebook elements
print(list_of_keys)
random_key = random.choice(list_of_keys) #choose random element in that list
print(random_key)
random_value = phonebook[random_key]
print(random_value)
 
#alternate way(you can also just do this for efficiency)
random_value = phonebook[random.choice(list(phonebook))]
print(random_value)


print()
print('*****  end section 9 ********')
print()

