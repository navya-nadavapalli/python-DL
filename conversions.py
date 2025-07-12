#type conversions
a = 100 #int
b = 3.4 #float
c = a+b # python will convert to float automatically
print(c)
print(type(c)) 

#Type Casting - No data loss
x = 100 #int
y = float(x) # y should be float
print(x)
print(y)
print(type(y))

#Type Casting -data loss
l = 3.14
m = int(l) # l should be int
print(l)
print(m)
print(type(m)) 

#numeric to text
z=10 #int
num_text = str(z)
print(type(num_text))