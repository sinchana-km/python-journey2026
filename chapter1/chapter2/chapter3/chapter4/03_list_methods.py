mylist=[1, 8, 72, 21, 15]
print(mylist)
mylist.sort() #sorts the original list
mylist.reverse() #reverse the original list
mylist.append(9) #add 9 at the end of the original list
mylist.insert(2, 9) #insert 9 at index 2
mylist.pop() #removes an item from the end of the list
mylist.pop(2) #removes an item from the given index from the list
mylist.remove(21) #removes the first occurence of a given item from the list
print(mylist)