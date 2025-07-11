# 2) დაწერე ფუნქცია, რომელიც ბეჭდავს "Hello, world!"

def hi():
    print("Hello, world!")
hi()




# 3) დაწერე ფუნქცია, რომელიც იღებს სახელს და ბეჭდავს "Hello, [სახელი]!"

def greet(name):
    print("Hello", name + "!")
greet("tekla")




# 4) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს

def sum_of_2 (a, b):
    print (a+b)
sum_of_2(2, 5)




# 5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია

def even_or_odd ():
    ui = int(input("Enter a number: "))
    if ui % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

even_or_odd()




# 6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს

def sashualo(list):
    sum = 0
    count = 0

    for num in list: 
        sum += num 
        count+=1
    print(sum/count)
sashualo([5, 5, 4, 6])




# 7) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს ამ სტრიქონის სიგრძეს

def len_of_text (text):
    print(len(text))
len_of_text("ear")




# 8) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში

def rev_list(list):
    print (list[::-1])
rev_list([1, 2, 3, 4, 5])




# 9) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მას დიდ ასოებად გადაყვანილს

def upper_string(text):
    text = text.upper()
    print(text)
upper_string("i hate niggers")




# 10) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უმეტესს

def more(a, b):
    if a > b:
        print (a)
    else:
        print(b)
more(9, 6)




# 11) დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს True თუ ის უარყოფითია, False თუ არა

def negative(num):
    if num < 0:
        print(True)
    else:
        print(False)
negative(-1)




# 12) დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. 
# გამოიყენე ციკლი და 'len()' შედარებისთვის

def longest(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)
longest(["hidroeleqtrosadguri", "vashli", "programireba"])                 




# 13) დაწერე ფუნქცია, რომელიც იღებს რიცხვს 'n' და აბრუნებს სიას 1-დან 'n'-ის ჩათვლით ყველა ლუწი რიცხვით. გამოიყენე for ციკლი და if-else

def luwi(n):
    for i in range(1, n):
        if i % 2 == 0:
            print(i)
luwi(10)




# 14) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else

def xmovnebi(text):
    count = 0
    for letter in text:
        if letter in "aeiou":
            count += 1
    print(count)
xmovnebi("tekla luka davit shavidze ana")