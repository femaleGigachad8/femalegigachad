# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა 1 რიცხვი. თქვენი დავალებაა შეამოწმოთ ამ რიცხვის ლუწობა. 
# თუ იგი ლუწია, დაბეჭდეთ "რიცხვი ლუწია" სხვა შემთხვევაში "რიცხვი კენტია"

def even_or_odd ():
    ui = int(input("Enter a number: "))
    if ui % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

even_or_odd()