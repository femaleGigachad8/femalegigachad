# 1) მომხმარებელს შემოატანინეთ წინადადება, დაითვალეთ მასში space-ების რაოდენობა და დაბეჭდეთ.
user_input = input("Please enter a sentance: ")
spaces = 0
for i in user_input:
    if i == " ":
        spaces += 1
    else:
        continue
print (spaces)