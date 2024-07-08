print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
option =int( input("Choose an operator"))
result =0
if(option ==1):
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1 + num2
elif(option ==2):
 num1 = int(input("Enter first number:"))
 num2 = int(input("Enter second number:"))
 result = num1 - num2
elif(option ==3):
 num1 = int(input("Enter first number:"))
 num2 = int(input("Enter second number:"))
 result = num1 * num2
elif(option ==4):
 num1 = int(input("Enter first number:"))
 num2 = int(input("Enter second number:"))
 result = num1 / num2


else:
    print("Invalid option")

print("The result of the opertaion is{}".format(result))