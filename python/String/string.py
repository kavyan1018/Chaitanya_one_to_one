# # single line comment
# """
#     multi line comments 
# """


# # printf -> print
# # "" -> '' "" """mulitne"""


# print("Hello World !")
# print('Hello World !')


# # variables 

# # int char

# a = 'hello !'

# print(a)



# # """ """ -> paragraph type 

# a = """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam possimus, voluptatem obcaecati veniam similique eligendi rem deserunt quaerat doloremque molestias sequi modi ab saepe! Nisi similique sequi hic eveniet odio."""
    
# print(a)



# Slicing  -> cut the String 
b = "Hello, World!"

# print(b[2:5])
# print(b[5:7])
# print(b[:7])       Slice from start
# print(b[2:])       # Slice from end


# Negative indexing 

# print(b[-5:-2]) 
# print(b[-15:-4]) 




# Upper case
print(b.upper())

a = " HII , tHIS IS MY fIRsT pYTHON sessION "
# Lower Case
print(a.lower())


# Remove Whitespace  
print(a.strip())

# replace
print(b.replace("H", "J"))

# Split 
b = "Hello, World!"

print(b.split(","))
print(b.split(" "))
print(b.split("W"))


# String Concatenation
a = "Hello"
b = "World !"

c = a + b

# Without space
print(c)

# With space
c = a + " " + b 
print(c)


# String Formate

age = 22
txt = f"My Name is Kavya, I am {age} Year old"

print(txt)

price = 56
prt = f"This price is {price:.2f} dollars"

print(prt)


teext = f"This price is {20 * 59} dollars"

print(teext)