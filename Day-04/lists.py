#LISTS  IN Python
#1.Creating a list
fruits=["apple","mango","banana","grapes","orange"]
print("Fruits:",fruits)

#2.Finding the largest Number
numbers=[20,60,40,50,90]
print("Largest number:",max(numbers))

#3.Adding an Element using append()
a=[10,20,30,40]
a.append(50)
print(a)

#4.Removing an element using remove()
fruits=["apple","mango","banana","grapes","orange"]
fruits.remove("orange")
print(fruits)

#5.Reverse a list using slicing
a=[10,20,30,40]
print(a[::-1])

#6. List Concatenation
list1=[1,2,3,4]
list2=[3,4,5,6,7]
list3=list1 + list2
print(list3)

#7.List Repetition
fruits=["apple","banana","cherry"]
print(fruits*2)

#8.Adding multiple elements using extend()
a=[1,2,5,45]
a.extend([100,200,300])
print(a)

#9.Inserting an Element using pop()
a=[1,2,3,4,5]
a.insert(0,10)
print(a)

#10. Counting Elements
a=[10,20,10,30,10]
print(a.count(10))

#11.Finding the index
a=[1,2,3,4,5]
print(a.index(3))

#12.Sorting in Ascending Order
a=[2,3,5,1,7,4]
a.sort()
print(a)

#13.Sortring in Descending Order
a=[2,3,5,1,7,4]
a.sort(reverse=True)
print(a)

#14.Built in Functions
a=[20,15,18,31,14,6]
print(max(a))
print(min(a))
print(len(a))
print(sum(a))

#15.Copying a List
days=["sunday","monday","tuesday"]
new_days=days.copy()
print(new_days)

#16.Creating a List
a=[1,2,3,4]
a.clear()
print(a)



 





