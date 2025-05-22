# 4) მომხმარებელს შემოატანინეთ 3 რიცხვი და დაითვალეთ რამდენი მათგანია 10-ზე მეტი. თუ ყველა შემოტანილი რიცხვი ათზე მეტია, დაბეჭდეთ "All the numbers that are larger than ten.", სხვა შემთხვევაში დაბეჭდეთ "Some numbers that are less than or equal to ten."

count = 0
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))

if num1 > 10:
    count += 1
if num2 > 10:
    count += 1
if num3 > 10:
    count += 1

if count == 3:
    print("All the numbers that are larger than ten.")
else:
    print("Some numbers that are less than or equal to ten.")
