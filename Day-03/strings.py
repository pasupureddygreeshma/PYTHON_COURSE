str1="Hello, World!"
print(str1)
lower_str=str1.lower()#lowercase
print(lower_str)
upper_str=str1.upper()#uppercase
print(upper_str)
capitalize_str=str1.capitalize()#capitalize
print(capitalize_str)

#checking methods
print(str1.islower()) 
print(str1.isupper())
print(str1.istitle()) 
print(str1.isalpha())
print("1,2,3,4,5".isdigit())
print("khghkyuiojkp222$12s12374".isalpha())
print(str1.rstrip())
print(str1.lstrip())
print(str1.split())

#Counting methods
str2="Hello, World! Hello, Python!"
print(str2.count("Hello"))
print(str2.count("World"))
words=str2.split()
print(len(words))
print(type(words))
combined_str=" ".join(words)
str2="she as an interview"
print(str2.split())
print(len(str2))

