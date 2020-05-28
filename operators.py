# for logical operators there are and , or , not
num1 = 5
num2 = 6
#print true or false if num1 greater than num2
print(num1 > num2)
#print true or false if num1 lower than num2
print(num1 < num2)
#print true or false if num1 equal num2
print(num1 == num2)
#print true or false if num1 NOT equal num2
print(num1 != num2)
#print true or false if num1 geater than or equal num2
print(num1 >= num2)
#print true or false if num1 lower than or equal num2
print(num1 <= num2)

#logical operators and , or , not
#print(True and True) # True
#print(True and False) # False
#print(False and False) # False
a,b = 22,23
print(a == a and b == b)
print(a == a and b < a)
print(a>b and b<a) # a greater than b && b less than a

#print(True or True) # True
#print(True or False) # True
#print(False or False) # False
print(a == a or b == b)
print(a == a or b < a)
print(a>b or b<a) # a greater than b && b less than a

#print(not True) # False
#print(not False) # True
print(not (a != 5))
print(not (a == 5))

print(True and True) # True