# 3) მომხმარებელს შემოატანინეთ 5 რიცხვი. თქვენი დავალებაა დაითვალოთ აქედან დადებითი და უარყოფითი რიცხვები. საბოლოოდ დაბეჭდეთ შემდეგი ფორმატით:
# "Positive numbers count: {count}"
# "Negative numbers count: {count}"

positive = 0
negative = 0
i = 0

while i < 5:
    i += 1
    number = int(input ("შეიყვანე რიცხვი: "))

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1



print(f"Positive numbers count: {positive}")
print(f"Negative numbers count: {negative}")
