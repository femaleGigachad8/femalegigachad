# 7) შემქნით ცარიელი სია, სადაც 3-ჯერ input-ის სახით მომხმარებელს შეაყვანინებთ სამი სტუდენტის სახელს და დაამატებთ სიაში append() ფუნქციით. შემდეგ კი ჩასვით "Teacher" სიის თავში, წაშალეთ ბოლო სტუდენტი და დაბეჭდეთ სიის სიგრძე, ასვეე საბოლოო სია.

list = [ ]

i = 0 
while i < 3:
    ui = input("Name and surname: ")
    list.append(ui)
    i+=1

list.insert(0, "Teacher")
list.pop(3)
print ("lenght of the list = ", len(list), "and the list is", list )
