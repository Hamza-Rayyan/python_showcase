# so we define exception to handle the errors 

try:
    age = int(input('Age: ')) 
    print(age)
    income = 20000
    risk = income / age
    print(risk)
except ValueError:
    print("please enter only intergers")
except ZeroDivisionError:
    print("invalid values")
    

    