# 2) შექმენით 5 ელემენტიანი სიტყვების სია. მომხმარებელს შემოატანინეთ სიტყვა და რიცხვი(ეს იქნება პოზიცია სადაც დაამატებთ შემოტანილ სიტყვას). დაბეჭდეთ განახლებული სია.
word = ["apple", "car", "book", "computer", "phone"]

sityva  = input("enter a word:")
num = int(input("enter a num: "))

word.insert(num, sityva)
print(word)
