# 1) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში

# 2) იგივე სახელი დაბეჭდეთ lowercase-ში

# 3) იგივე სახელი დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი, ხოლო დანარჩენი lowercase-ში

name = input("Please enter your name: ")

print (name.upper()) 
print (name.lower())
print (name.capitalize())


# 4) შექმენით ცვლადი, სადაც შეინახავთ ნებისმიერ სიტყვას. მომხმარებელს შემოატანინეთ სიმბოლო, რომლის ინდექსიც უნდა იპოვოთ სთრინგში და დაუბეჭდოთ.

# თუ მომხმარებელმა ჩაწერა ისეთი სიმბოლო, რომელიც არ არის სიტყვაში. დაუბეჭდეთ რომ "This symbol is not in word"



word = "Datodzia"
symbol = input("enter a symbol to find its index in the word: ")
index = word.find(symbol)


if index != -1:
    print(symbol, "-", index)
else:
    print("This symbol is not in word")
    
