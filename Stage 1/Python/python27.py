car = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
thisdict = dict(name = "John", age = 36, country = "Norway")

x=car.keys()
y=car.values()
print(x)
print(y)

car["color"] = "red"

print(x)

z = car.items()
print(z)

if "brand" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

car["year"] = 2018

car.pop("color")
print(car)
car.popitem()
print(car)

"""
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
"""
#using loops in dic
for x in car:
  print(x)

for x in car:
  print(car[x])


for x, y in car.items():
  print(x, y)

for x in car.keys():
  print(x)

for x in car.values():
  print(x)


#copy dict
mydict = car.copy()
print(mydict)

#nested dict 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
