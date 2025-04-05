# 4) შექმენით ცვლადი, სადაც შეინახავთ თქვენს სახელს.
# მომხმარებელს შემოატანინეთ პაროლი და თუ ის უდრის "1234"-ს დაბეჭდეთ
# "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect"

name = "tekla"
user_input = input ("please enter your password: ")
if user_input == "1234":
    print ("Password is correct")
else:
    print ("Password is incorrect")
