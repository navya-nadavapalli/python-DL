 #if statement
#if condition:
#statements

num=8
if num>0:
    print("positive number")

#if-else statement
# if condition:
# statements
# #else:
# #statements
num=-15
if num>0:
    print("Positive number")
else:
    print("negative number")

#vote app
age = 22
if age>=18:
    print("you can vote")
else:
    print("you cannot vote")   

#vote app in dynamic
#apply type casting
age = int(input("Enter you Age:"))
if age>=18:
    print("you can vote")
else:
    print("you cannot vote")  

#ternary operator
#value_if_true if condition else value_if_false
age = int(input("Enter you Age:"))
vote_status = "you can vote" if age>=18 else "you cannot vote"
print(vote_status)

#elif ladde
#if condition:
# statements
#elif condition:
#statements
#elif condition:
#statements
#elif condition:
#statements
#elif condition:
#statements

#else:
#statements

#calculate student marks using elif statement
marks = int(input("Enter your marks:"))
if marks>=90:
    print("A")
elif marks>=75:
    print("B") 
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
else:
    print("FAIL")              

#vote app with nationality
age=int(input("Enter Your Age"))
nationality = input("Enter Your Nationality")
if age>=18 and nationality == "indian":
    print("You can Vote")
else:
    print("You cannot vote")
