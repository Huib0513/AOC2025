#!python3
import os
import datetime

# Test input
input = ["3-5",
"10-14",
"16-20",
"12-18",
"",
"1",
"5",
"8",
"11",
"17",
"32"]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    result = 0
    fresh_stuff = []
    part2 = False
    for line in input:
        if len(line) == 0:
            part2 = True
            continue
        if not part2:
            fresh_stuff.append((int(line.split('-')[0]),int(line.split('-')[1])+1))
        else:
            for r in fresh_stuff:
                if ((int(line) > r[0]) & (int(line) < r[1])):
                    result += 1
                    break

    print("Deel 1: " + str(result))

def solve2():
    result = -1
 
    print("Deel 2: " + str(result))

starttime = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-starttime)

starttime = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-starttime)

