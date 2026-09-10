#tuples - duplicates are allowed, ordered, immutable

t1 = ("apple", "orange", "kiwi","pineapple","mango")

t2 = () #empty tuple

print(t1[0])
print(t1[1])
print(t1[:3])
print(t1[1:4])

#changing the value of a tuple 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


for i in range(len(t1)):
    print(f"{i+1} is {t1[i]}")
