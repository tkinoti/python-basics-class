#structures - variables that hold multiple variables eg list, tuple and dictionary

#list - has square brackets []

person_l =["John", "Doe", 30, 65.54, "Mombasa", True]

print(person_l[0])

print(person_l[3])

print(person_l[1:5])

print(person_l[0:5])

print(person_l[2:4])

print(person_l[-4:-2])

person_l.append("employed")

person_l.remove(65.54)

person_l.pop(0)

print(person_l)



#tuple - has normal brackets () is immutable hence cannot change its contents. uses smaller space (days, months...)
person_t =("John", "Doe", 30, 65.54, "Mombasa", True)

print(person_t[0])

print(person_t[3])

print(person_t[1:5])

print(person_t[0:5])

print(person_t[2:4])

print(person_t[-4:-2])

# person_t[2]=31 , testing tuple immutability
# print(person_t)

#dictionaries - holds variables in key:value pairs uses curly braces

person_d = {"firstname" : "John", "surname" : "Doe", "weight": 65.57, "location": "mombasa", "activeuser": True}

print(person_d)

print(person_d["surname"])

print(person_d["surname"],person_d["location"])

#assignment
tasklist=[23,"jane",["lesson 23",560,{"currency": "kes"}],987,(76,"john")]

print(type(tasklist))

print(tasklist[2][2]["currency"])

print(tasklist[2][1])

print(len(tasklist))

print(tasklist)

