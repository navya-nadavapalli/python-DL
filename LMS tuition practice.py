 #covering all concepts of variables ,data types,operators,conditionals,Type casting.
print("-----LMS FEE DISCOUNT CALCULATION------")
#get user input
student_name = input("Enter Name:")
student_grade = int(input("Enter Grade(1-12)"))
tuition_fee = float(input("Enter Tuition Fee"))

is_Academic_topper_input = input("Academic Topper ?(yes/no)")
is_Academic_topper = is_Academic_topper_input =="yes"

#initial Discount set
discount = 0.0

#input validation
if 1<= student_grade <=12:
    #process discount for calculation
    print(f"processing discount for{student_name}")

    #primary discount for 9-12
    if student_grade >= 9 and student_grade <= 12:
        if is_Academic_topper:
            discount = 0.20
            print("Academic Topper Dicount  Applied")
        else:
            discount = 0.10
            print("Primary Discount Applied") 

    elif student_grade >=6 and student_grade<= 8:
        discount =0.05
        print("Middle School Discount Applied")
    else:
        dicount = 0.0
        print("No Discount Applicable for this grades")

    #using match-case
    match student_grade:
        case 10:
            discount += 0.03
        case 12:
            discount += 0.05
        case _:
            discount += 0.0

    discount_amount = tuition_fee * discount
    discount_fee = tuition_fee - discount_amount 

    print("print(-----LMS FEE DISCOUNT CALCULATION------)")
    print(f"Processing discount for {student_name} ")
    print(f"Student Name{student_name}")
    print(f"Student Grade{student_grade}")
    print(f"Academic Topper status {is_Academic_topper}")
    print(f"Base Tuition Fee{tuition_fee}")
    print(f"Amount Discount{discount_amount}")
    print(f"Final TUition FEE{discount_fee}")

else :   
    print(f"Invalid Grade!, please enter in between 1-12")
