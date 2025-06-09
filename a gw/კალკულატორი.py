print("აირჩიეთ ოპერაცია:")
print("1. მიმატება")
print("2. გამოკლება")
print("3. გამრავლება")
print("4. გაყოფა")

choice = input("აირჩიეთ ერთ-ერთი (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("მოხდა შეცდომა!გაყოფა ნულზე!") 
        else: 
            print(num1, "/", num2, "=", num1 / num2)
else:
    print("შეყვანა მოხდა არასწორად") 