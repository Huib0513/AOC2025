#!python3
import os
import datetime

# Test input
input = ["L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"]

# input integers separated by commas
#input= [int(i) for i in open("input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().split(",")]

# input integers on complete lines
#input = [int(i) for i in open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    pos = 50
    zeros = 0
    for (d,i) in [(l[:1], int(l[1:])) for l in input]:
        pos += i if d == 'R' else -i
        if (pos > 99): pos = pos - 100
        if (pos < 0): pos = 100 + pos
        if (pos == 0): zeros += 1
        #print(i if d == 'R' else -i, pos)
    print("Deel 1: " + str(zeros))

def solve2():
    print("Deel 2: No")

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)
