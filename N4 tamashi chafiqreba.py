import random

cop_number = random.randint(1, 100)

steps = 0

while True:

    user_number = input("Guess the number: ")

    if user_number == "E" or user_number == "exit":
        print("Bye Bye")
        break

    elif not user_number.isdigit():  # იმ შემთვევაში თუ user_number-ში შეტანილი რიცხვი იქნება სიტყვა ან ასო(ნებისმიერი სტრინგი) გარდა "E" და "exit"
        # მაშინ გამოგვიტანს შემდეგ პრინტს და მოგვთხოვს რიცხვის შეტეანას
        print("Please input any digit!")
        continue  # continue ასეთ შემთხვევაში პროცესს აგზავნის თავში და ციკლი იყება სულ თავიდან ("Guess the number: ")-დან
        # სანამ არ შევიყვანთ რიცხვს მანამდე იტრიალებს ციკლი და გამოვა input("Guess the number: ") ოპერაცია


    user_number = int(user_number)  # ამ ხერხით user_number-ში შეგვიძლია შევიტანოთ როგორც რიცხვი, ასევე სტრინგი

    steps += 1

    if user_number == cop_number:
        print("Congratulations! You guess the number!")
        print(f"You found the number in {steps} steps")
        break
    elif user_number < cop_number:
        print("Your number is lower")
    else:
        print("Your number is higher")

