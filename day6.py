#!python3
import os
import datetime

# Test input
input = ["123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "]

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    result = 0
    matrix = [[x.strip() for x in row.split(' ') if x.strip()] for row in input]
    # Transpose matrix using zip
    #print(list(zip(*matrix)))
    for problem in list(zip(*matrix)):
        problemresult = 0 if problem[-1] == '+' else 1
        for p in problem[:-1]:
            if problem[-1] == '+':
                problemresult += int(p)
            else:
                problemresult *= int(p)

        result += problemresult
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

