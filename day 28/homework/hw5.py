# 5) მომხმარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ეს რიცხვი მარტივი(მარტივი არის რიცხვი, რომელიც მხოლოდ 1-ზე და საკუთარ თავზე იყოფა). შემდეგ კი დაბეჭდეთ "This is prime number" თუ რიცხვი მარტივია, სხვა შემთხვევაში "This isn't prime number"

number = int(input("Please enter a number: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print("This is a prime number")
else:
    print("This isn't a prime number")