print("-"*50,"Welcome!","-"*50)
score= int(input("Enter your score: "))
if score <=100 and score>=70:
    print("Your grade is A")
elif score <=69 and score>=60:
    print("Your grade is B")
elif score<=59 and score>=50:
    print("Your grade is C")
elif score<=49 and score>=45:
    print("Your grade is D")
elif score<=44 and score>=40:
    print("Your grade is E")
elif score<=39 and score>=0:
    print("Your grade is F")
else:
    print("Invalid score, please enter a valid score!")