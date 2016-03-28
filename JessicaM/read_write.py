#!/usr/bin/python

#f = open("scores.txt", "a")

with open("scores.txt", "a") as f_a:
    while True:
        partic = raw_input("participants Name: > " )
        if partic == "quit":
            print("Quitting....GoodBye")
            break

        scor = raw_input("participants Score: > ")
            
        f_a.write(partic + "," + scor + "\n")

with open("scores.txt", "r") as f:
    #content = f.read()
    #content = f.readlines()
    content = f.read().splitlines()

scoreboard ={}

for lines in content:
    participants = lines.strip().split(",")
    participant = participants[0]
    score = participants[1]

    scoreboard[participant] = score

print(scoreboard)
