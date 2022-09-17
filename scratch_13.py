print("enter a and b")
a=int(input())
b=int(input())
no=15
print("Player 1:\n")
print("PLEASE GUESS NUMBER")
guessno=int(input())
if guessno<a|guessno>b:
    exit()
i=0

while(no!=guessno):
    if no<guessno:
        print(f"The guessno={guessno} is greater than no={no} ")

    elif(no>guessno):
        print(f"The guessno={guessno} is lesser than no={no} ")
    else:
        print(f"Guess number {guessno} is not in range")
        exit()
    guessno=int(input("PLEASE GUESS NEXT NUMBER"))
    i=i+1
print("You have guessed the correct no")
print(f"The number of trials taken by Player 1 is {i}")
print("Player 2:\n")
print("PLEASE GUESS NUMBER")
guessno1=int(input())
if guessno1<a|guessno1>b:
    exit()
j=0

while(no!=guessno1):
    if no<guessno1:
        print(f"The guessno={guessno1} is greater than no={no} ")

    elif(no>guessno1):
        print(f"The guessno={guessno1} is lesser than no={no} ")
    else:
        print(f"Guess number {guessno1} is not in range")
        exit()
    guessno1=int(input("PLEASE GUESS NEXT NUMBER"))
    j=j+1
print("You have guessed the correct no")
print(f"The number of trials taken by Player 2 is {j}")
if i==j:
    print("The match is tied")
elif(i<j):
    print("Player 1 has won")
else:
    print("Player 2 has won")

