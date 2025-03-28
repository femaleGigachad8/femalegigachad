# 3) შექმენით რეგისტრაცია/ავტორიზაციის სიმულაცია:
# მომხმარებელს შემოატანინეთ ემაილი, პაროლი და შეინახეთ ისინი ცვლადებში.
# ისევ შემოატანინეთ ემაილი და პაროლი(ეს იქნება ავტორიზაცია) 
# და თუ შემოტანილი მნიშვნელობები დაემთხვევა
# რეგისტრაციისას შეყვანლის, 
# დაბეჭდეთ True, სხვა შემთხვევაში False.


email = input ("Please enter your email: ")
password = input ("Please enter your password: ")

email2 = input ("Please enter your email: ")
password2 = input ("Please enter your password: ")

print (email == email2 and password == password2)
