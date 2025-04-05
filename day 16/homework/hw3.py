# 3) კომენტარებით ახსენით რა არის Control Flow(ივარჯიშეთ if/else-ბზე და გააკეთეთ მინიმუმ 3 მაგალითი)


# Control Flow არის პროგრამაში ინსტრუქციების შესრულების თანმიმდევრობა. 
# Sequence - კომპიუტერი ზემოდან ქვემოთ კითხულობს კოდს
# Selection - პროგრამა ირჩევს, თუ რა უნდა შესრულდეს პირობის მიხედვით მაგ: if ან else

username = input ("What's your username?")
if username == "asuto.ronaldo7":
    print ("welcome back, KAORI")
else: 
    print ("incorrect username")


weather = input ("როგორი ამინდია?:")
if weather == "მზიანი":
    print ("დღეს შეგიძლია მეგობრებთან ერთად გახვიდე")
else: 
    print ("დღეს ამინდი ცუდია, სახლში დარჩი")

math_problem = input ("what's 1+19?: ")
if math_problem == "20":
    print ("Correct!")
else: 
    print ("oops, incorrect please try again.")

