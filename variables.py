#strings - alpha numeric and special
#integers - numbers without decimals
#float -  number with few decimal places(eg currency)
#double - number with a large number of decimal places (eg pi)
#boolean - holds true or false

firstname = "Tom"
secondname = "Kinoti"

print(firstname +" "+ secondname)

print(firstname, secondname)

x="45"
y="70"
z=45
print(type(x))

print(type(z))

#type casting
print(type(str(z)))

#string operations
print(firstname.upper())
print(firstname.lower())
print(firstname.title())

print(secondname.count("i")) #case sensitive

print(secondname.upper().count("I"))

print(secondname.upper())

print(secondname.count("I"))

print(type("John Doe".split(" ")))

print(secondname[0])
print(secondname[-1])
print(secondname[-5])


print(secondname[0:3])# the first is where you begin and the other is where you end plus one
print(secondname[3:])
print(secondname[3:6])

#integers
print(98+87+65+78+90)

print((98+87+65+78+90)/5)

sum= 98+87+65+78+90

avg=sum/5

print(avg)

rem=7%2 #modulus - returns the reminder of a division
print(rem)
print(type(rem))

fl1=3.45
print(type(fl1))

bo = 4 > 7

print(bo)

print(type(bo))

dec1=3.45877894
print(int(dec1))

dec2 = round(dec1,2)
print(dec2)

