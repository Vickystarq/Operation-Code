# Customer Variability
Num_1 = float(input("Enter a value for Num_1:"))
Num_2 = float(input("Enter a value for Num_2:"))
print("Num_1 is:", Num_1)
print("Num_2 is:", Num_2)
#Operational Code
Result= Num_1 + Num_2  # Addition
print("Additon Result is:", Result)
Result= Num_1 - Num_2
print("Subtraction Result is:", Result)
Result= Num_1 * Num_2
print("Multiplication Result is:", Result)
Result= Num_2 / Num_1
print("Division Result is:", Result)
Result= Num_2 // Num_1
print("Quotient Result is:", Result)
Result= Num_2 % Num_1
print("Modulo Result is:", Result)
Result= Num_2 ** Num_1
print("Power Result is:", Result)
# Comparison Operation 
Result = Num_1 > Num_2
print("Result is", Result)
Result = Num_1 < Num_2
print("Result is", Result)
Result = Num_1 == Num_2
print("Result is", Result)
Result = Num_1 != Num_2
print("Result is", Result)
#Logical Reasoning Operation 
Num_3 = float(input("Enter a value for Num_3:"))
if (Num_3 > Num_1) and (Num_3> Num_2):  # Condition 1
    print("Num_3 is the largest:", Num_3)
else :
    print("One Value is greater than :", Num_3)
Num_3 = float(input("Enter a value for Num_3:"))
if (Num_3 < Num_1) and (Num_3 < Num_2):
   print("Num_3 is the smallest:", Num_3)
else :
    print("The other Values are greater than :", Num_3) 
Num_3 = float(input("Enter a value for Num_3:"))
if  Num_3 > Num_1 and Num_3 > Num_2:
    print("Num_3 is the largest")
else:
    print("Num_3 is in within the range of value")
#shorthand Operator 
Num1 = float(input("Enter a value for Num1:"))
Num2 = float(input("Enter a value for Num2:"))
Result = Num1 + Num2
Result += 10
print("My updated value is:", Result)
#End Code
