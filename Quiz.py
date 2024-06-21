print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play 😄")
score = 0

answer = input("What is a computer? ")
if answer.lower() == ('device'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What are the main components of a computer system? ")
if answer.lower() == ('hardware'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is an operating system? ")
if answer.lower() == ('software'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is the function of cpu? ")
if answer.lower() == ('processing'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is the difference between RAM and ROM? ")
if answer.lower() == ('volatility'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " marks out of 5")