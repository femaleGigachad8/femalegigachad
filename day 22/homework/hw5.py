#5) მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)
num = int(input("Please enter your number: ")) 
for i in range (1, num+1):
    if num % i == 0:
        print (i)
        