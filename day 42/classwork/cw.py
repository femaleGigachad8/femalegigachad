# 1) შექმენით ფუნქცია სახელად even_or_odd,
# რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაბეჭდავს ლუწია თუ კენტია ის


def even_or_odd ():
    ui = int(input("Enter a number: "))
    if ui % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

even_or_odd()

# 2) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს 5 სახელს.
#  შექმნის მისგან სახელების სიას და დაბეჭდავს მას. 


def names ():
    name = []
    for i in range(5):
        ui = input("Enter a name: ")
        
        name.append(ui)
        
    print (name) 

names()



# 3) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა რიცხვს.

def between(num):
    
    for i in range (1,num):
        print (i)
between(10)

# 4) შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს, და დაბეჭდავს რიგით მე-5 ლუწ რიცხვს შემოტანილი რიცხვის შემდეგ.

def evennum(n):
    current = n
    for i in range(5):
        current += 1
        while current % 2 != 0:
            current += 1
    print(current)

evennum(13)



