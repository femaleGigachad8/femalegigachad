# 1) მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ თუ ის ნაკლებია 18-ზე მაშინ შეამოწმეთ თუ ასაკი ნაკლებია 14-ზე დაუბეჭდეთ Discount 20%, სხვა შემთხვევაში Discount 10%.
# თუ პირველი if-ი არასწორია დაბეჭდეთ No discount

# გამოიყენეთ ჩაშენებული if


age = int(input("Please enter your age: "))

while age < 18:
    if age < 14:
        if age >= 14:
            print ("No discount")
    else:
        print ("Discount 10%")
        