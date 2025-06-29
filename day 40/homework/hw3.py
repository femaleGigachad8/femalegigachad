# 3) გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს პირიქით.

# Input: "helloWorld" -> Output: "Hello world"

user_input = input("Please enter a sentance: ")
result = ""

for char in user_input:
    if char.isupper():
        result += " "+char.lower()
    else: 
        result += char 

result = result.capitalize()
print(result) 