print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play 😄")
score = 0

answer = input("What is phone? ")
if answer.lower() == ('a rectangular device'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is pc? ")
if answer.lower() == ('personal computer'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is laptop? ")
if answer.lower() == ('computer alternative'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is water? ")
if answer.lower() == ('liquid'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is human? ")
if answer.lower() == ('trash'):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " marks out of 5")