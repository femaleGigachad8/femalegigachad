# 4) შექმენით ხარიელი სია სადაც მომხმარებელს 5-ჯერ შემოატანინენებთ რიცხვს, შემდეგ კი დაამატებთ მას სიის ბოლოში append() ფუნქციით.

list = []
gc = 0
while gc < 5:
    ui = int(input("PLease enter a number: "))
    gc+=1
    list.append(ui) 
print (list)
