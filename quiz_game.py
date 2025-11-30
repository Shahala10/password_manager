print("WELCOME TO OUR COMPUTER QUIZ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Bye")
    quit()

print("Okay! Let's play: ")
score = 0

answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=10
else:
    print("Incorrect!")



answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score +=10
else:
    print("Incorrect!")


answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score +=10
else:
    print("Incorrect!")


answer = input("What does ROM stands for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score +=10
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score +=10
else:
    print("Incorrect!")
    
print("You got " + str(score) + " question correct!")
print("You got " + str((score/4)*100) + "%.")