print("Welcome to my tennis quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play.")
score = 0

answer = input("What does Ad stand for? ")
if answer.lower() == "advantage":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does WC stand for? ")
if answer.lower() == "wild card":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does bagel stand for? ")
if answer.lower() == "zero" or answer.lower() == "love":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GOAT stand for? ")
if answer.lower() == "greatest of all time":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")