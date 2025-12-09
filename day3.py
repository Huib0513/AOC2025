#!python3
import os
import datetime

# Test input
input = ["987654321111111",
"811111111111119",
"234234234234278",
"818181911112111"]

# input complete lines
#input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').read().splitlines()

def solve1():
    result = 0

    for bank in input:
        max1 = indexmax1 = max2 = indexmax2 = 0
        for index in range(len(bank)-1):
            if (int(bank[index]) > max1): 
                max1 = int(bank[index])
                indexmax1 = index
        for index in range(indexmax1+1, len(bank)):
            if (int(bank[index]) > max2): 
                indexmax2 = index
                max2 = int(bank[index])
        print(bank + ': ' + str((max1*10)+max2))
        result += ((max1*10)+max2)
    
    print("Deel 1: " + str(result))

def find_highest(bank):
    max = int(bank[0])
    maxindex = 0
    for i in range(len(bank)):
        if (int(bank[i]) > max):
            maxindex = i
            max = int(bank[i])
    return max, maxindex


def solve2():
    result = -1
    length = 2
    start = 0
    digit = 0
    for bank in input:
        resultstring = ''
        for l in range(length,0,-1):
            digit, start = find_highest(bank[start:len(bank)-start-l])
            resultstring += str(digit)
            start += 1
        print(bank, resultstring)
 
    print("Deel 2: " + str(result))

starttime = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-starttime)

starttime = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-starttime)

