#1.ARITHMETIC OPERATORS:==+,-,*,/,%,**,//
a = 10
b = 20
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus
print(a**b) #exponentiation
print(a//b) #floor division

#2. RELATIONAL OR COMPARISON OPERATORS:==>,<,>=<=,==,!=
a=10
b=20
print(a>b) #greater than
print(a<b)  # less than
print(a>=b) #greater than or equal to
print(a<=b)  #less than or equal to
print(a==b)  #equal to
print(a!=b)  #not equal to

#3.LOGICAL OPERATORS:==and,or,not
a=10
b=20
print(a>5 and b>15) #and
print(a>5 or b>15) #or
print(not(a>5 and b>15)) #not

#4.ASSIGNMENT OPERATORS:===,+=,-=,*=,/=,%=,//=,**=
a=10
b=20
a+=b #a=a+b
print(a)
a-=b   #a=a-b
print(a) 
a*=b  #a=a*b
print(a)
a/=b  #a=a/b
print(a)
a%=b  #a=a%b
print(a)
a//=b #a=a//b
print(a)
a**=b   #a=a**b
print(a)

#5.BITWISE OPERATORS:==&,!,^,~,<<,>>
a=10
b=20
print(a&b) #bitwise and
print(a|b) #bitwise or
print(a^b) #bitwise xor
print(~a)   #bitwise not or complement
print(a<<2) #left shift
print(a>>2) #right shift

#6.MEMBERSHIP OPERATORS
a=[10,20,30,40,50]
print(10 in a)  #True
print(60 in a)  #False
print(60 not in a)#True
s="hello"
print("H" in s)

#7.IDENTITY OPERATORS:==is,is not
a=10
b=10
print(a is b) #True
print(a is not b) #False
a=[10,20,30]
b=[10,20,30]
print(a is b)
print(a is not b)


