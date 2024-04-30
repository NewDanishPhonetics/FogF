import re

output = open("output.txt", "w", encoding="utf8")
input = open("danpass_ffmap.csv", "r", encoding="utf8")
lines = input.readlines()

nål = "t>0" #definer hvad der skal findes. Man kan bruge RE

for høstak in lines:
    kolonne = line.split(';')
    ord = kolonne[1]
    bred = kolonne[2]
    snæver = kolonne[3]
    map = kolonne[4]
    if nål in høstak:
        print(ord, snæver)
        output.write(ord + " " + snæver + "\n")

output.close()
input.close()
