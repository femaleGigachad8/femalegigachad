#5) მომხმარებელს შემოატანინეთ რიცხვი. შეამოწმეთ, თუ შემოტანილი რიცხვი არის ლუწი დაბეჭდეთ 
#"The numbers is even", სხვა შემთხვევაში დაბეჭდეთ "The number is odd"

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")

