# 1) მომხმარებელს შემოატანინეთ წინადადება და შეინახეთ ის ცვლადში. თქვენი დავალებაა ეს შემოტანილი წინადადება გადაიყვანოთ camelCase-ში.
# (ამ დავალების შესასრულებლად არ უნდა გამოიყენოთ .title ფუნქცია)



ui = input ("Please enter a sentance: ")
result = ""
is_space = False 

for i in ui.lower():
    if i == " ":
        is_space = True
    elif is_space:
        result  += i.upper ( )
        is_space = False
    else:
        result += i
print(result)


