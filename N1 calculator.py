x = float(input("შეიყვანეთ პირველი რიცხვი: "))

z = input("აირჩიეთ ოპერატორი: +, -, *, /, **: ")

y = float(input("შეიყვანეთ მეორე რიცხვი: "))


if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "/":
    if y != 0:
        print(x / y)
    else:
        print("0-ზე გაყოფა არ შეიძლება")
elif z == "**":
    print(x ** y)
else:
    print("შეყვანილი ოპერატორი არასწორია")






