#list methods

#append 
l = [1,4,3,2]
l.append(6)
print(l)

l.insert(4,5) # (index,value)
print(l)

l.remove(2) #removes the first occurance of the 2
print(l)

l.extend({12,14,15});

l1 = [16,17]
l.extend(l1)
print(l);

l.pop() # removes the last element
l.pop(0) # removes the first element
del l[5] # removes the 6th element
print(l)

# l.clear() - to empty the list 

l.sort();
print(l)
l.sort(reverse=True)
print(l)

l2 = l.copy();
print(l2)

l1 = l1 + l2; # joining two lists
print(l1)
