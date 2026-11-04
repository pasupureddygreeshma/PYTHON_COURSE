#TUPLES IN PYTHON
#1.Creating a Tuple
t=(10,20,30,40)
print(t)

#Accessing Tuple Elements
print("First Element:",t[0])
print("Second Element:",t[-1])

#3.Tuple Index Method
print("index of 20:",t.index(20))

#4.Tuple Count Method
print("Count of 10:",t.count(10))

#5.Tuple Slicing
print("Slicing:",t[0:2])

#6.Reversing a Tuple
print("Reversed tuple:",t[::-1])

#7.Tuple Concatenation
this=("apple","banana","cherry")
that=(1,2,3)
they= this+that
print("Concatendated tuple:",they)

#8.Tuple Repetition
a=(1,2,3)
b=a*2
print("Repeated tuple:",b)

#9.For loop in Tuples
l=(1,2,3,4)
for i in range(len(l)):
    print(l[i])

#10.White Loop in Tuples
l=(1,2,3,4)
i=0
while i<len(l):
    print(l[i])
    i+=1

#11.Tuple Length
t=(10,20,30,40)
print(len(t))

#12.Converting Tuple into List
t=(10,20,30)
a=list(t)

#13.Tuple Immutability
t=(10,20,30)
print(t)

