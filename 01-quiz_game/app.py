print("Welcome to my computer quiz!")

playing = input("Do you want to play Yes (y|Y), No (n|N)? ")

if playing.lower() != "yes" and playing.lower() != "y":
    quit()

print("Ok! let's Play! :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What Does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")

percent = (score/4) * 100
print(f"You got {percent}%")
