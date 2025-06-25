

#TypeError,Type Checking and type conversion
num_char = len(input('What is your name '))
#new_num_char = str(num_char)----> conversion of int to string
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")
#type()------->to find data types
print(type(num_char))

a = (123)
print(type(a))
a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+ str(100))