a=int(input("enter the first no :"))
b=int(input("enter the second no :"))

print("operations: +,-,*,/")
select=input("select operations :")
if select == "+":
    print(a, "+", b, "=", a+b)
elif select == "-":
    print(a, "-", b, "=", a-b)
elif select == "*":
    print(a, "*", b, "=", a*b)
else:
    print(a, "/", b, "=", a/b)
