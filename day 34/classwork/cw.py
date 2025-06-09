# 1) შექმენით 5 ელემენტიანი სია. გადაუარეთ მას for ციკლით და დაბეჭდეთ მისი თითოეული ელემენტი

list = [0, 1, 2, 3, 4]

for i in list:
    print(i)

# 2) შექმენით ცვლადი სადაც შეინახავთ ნებისმიერ წინადადებას.
# გადაუარეთ for ციკლით მას და დაბეჭდეთ წინადადების თითოეული სიმბოლო
    
sentance = "I am a carspotter"

for u in sentance:
    print (u)

# 3) პირველ დავალებაში შექმნილ სიას გადაუარეთ while ციკლის გამოყენებით.(მინიშნება: დაგჭირდებათ ცვლადის შექმნა,
# რომელსაც გაზრდით ყოველი იტერაციისას და გამოიყენებთ სიის ინდექსებზე წვდომის მისაღებად)

i = 0  #unda shevqmnat cvladi romelsac aqvs indeqsis mnishvneloba
while i < len(list): #len gvichvenebs siis zomas da sanam len metia indexze mashin 
    #daiprinteba i-s indexi romlis mnishvnelobac aqvs
    print(list[i])
    i += 1 #i-s daemateba 1 
    