print("Welcome to my computer quiz!")

playing = input("Do you want to play Yes (y|Y), No (n|N)? ")

if playing.upper() != "YES" and playing.upper() != "Y":
    quit()

print("Ok! let's Play!")

answer = input("What does CPU stand for? ")

if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")