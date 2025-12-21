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
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

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
    fresh_stuff = {}

    for line in input:
        if len(line) == 0:
            break
        fresh_stuff[line.split('-')[0]] = (int(line.split('-')[0]),int(line.split('-')[1])+1)
    
    startjes = sorted([int(f) for f in fresh_stuff.keys()])
    print(startjes)
    for i in range(len(startjes)):
        print(startjes[i])
        # if i is not the last item: 
        #   if the next start is larger than the current end: count all numbers in the range
        #   else if the next stop is larger than the current stop: count all number from the current start to the next start
        #   else ignore the smaller next range

        # Take the start
        # until the next start is smaller than the current end
        # if the next end is smaller than the current end: ignore range
        # if the next end is larger than the current end: start working with that end


 
    print("Deel 2: " + str(result))

starttime = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-starttime)

starttime = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-starttime)

