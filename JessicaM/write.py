#!/usr/bin/python

f = open("scores.txt", "a")

while True:

    participant = raw_input("participant  ")

    if participant == "quit":
        print("Quitting....GoodBye")
        break

    scores = raw_input("Score for " + participant + " >")
    f.write(participant + "," + scores + "\n")

f.close()

f_read = open("scores.txt", "r")

participants = {}
entry =[]

for line in f_read:
    entry = line.strip().split(",")
    participant = entry[0]
    score = entry[1]

    print(participant + "=>" + score)
    participants[participant] = score

f_read.close()

print(participants)
