# 4) შექმენით პროგრამა, სადაც მომხმარებელი გამოიცნობს ჩაფიქრებულ რიცხვს 1-დან 10-ის ჩათვლით.
# დაგჭირდებათ ცვლადი, სადაც შეინახავთ ნებისმიერ რიცხვს 1-დან 10-მდე(ეს იქნება ჩაფიქრებული რიცხვი).
# while loop-ის გამოყენებით მომხმარებელს იქამდე შემოატანინეთ რიცხვი სანამ არ გამოიცნობს. მომხმარებელს 
# ექნება 3 ცდა ჩაფიქრებული რიცხვის გამოსაცნობად. ყოველი არასწორი რიცხვის შეყვანისას დაბეჭდეთ "Wrong number"
# და აცნობეთ მომხმარებელს რამდენი ცდა დარჩა. თუ გამოიცნო, გათიშეთ while ციკლი და დაბეჭდეთ You win,
#  ხოლო თუ ცდები ამოეწურა ასევე გათიშეთ while ციკლი და დაბეჭდეთ "You lose"

secret_number = 7
attempts = 3
while attempts > 0 :
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == secret_number:
        print ("You win")
        break
    else:
        attempts -= 1 
        if attempts > 0:
             print("Wrong number. Attempts left:", attempts) 
        else:
            print("You lose")







