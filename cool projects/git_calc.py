name_1= input("Enter your name: ")
Zodiac_1= input("Enter your zodiac sign: ")
print(name_1, Zodiac_1)
name_2= input("Enter your person's name: ")
Zodiac_2= input("Enter your person's zodiac sign: ")
print(name_2, Zodiac_2)
score_1=0
for char in (name_1+Zodiac_1):
    score_1=score_1+ ord(char)
score_2=0
for char in (name_2+Zodiac_2):
    score_2=score_2+ ord(char)
love = ((score_1 + score_2) % 100)+1
print(f"\n{name_1} and {name_2} are {love}% compatible!")

if love >= 80:
    print("A perfect match! 💕")
elif love >= 60:
    print("Great potential! 😊")
elif love >= 40:
    print("Could work with effort! 🤔")
else:
    print("Maybe just friends! 😅")