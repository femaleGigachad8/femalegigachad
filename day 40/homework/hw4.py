# 4) ასევე დაწერეთ პროგრამა, რომელიც შემოტანილ წინადადებას გადაიყვანს snake_case-ში.
user_input = input(("Please enter a sentance: "))
sentace = ""

for i in user_input:
    if i != " ":
        sentace += i 
    else:
        sentace += "_"
print (sentace)
