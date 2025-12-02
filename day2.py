#!python3
import os
import datetime

# Test input
input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

# input complete lines
input = open('input_'+os.path.basename(__file__).split(".")[0]+'.txt').readline()

def solve1():
    ranges = input.split(',')
    result = 0

    for r in ranges:
        lo, hi = r.split('-')
        #print(lo,hi)
        index = int(lo)
        while (index < int(hi)+1):
            # Make sure only values with even lengths are considered
            if (len(str(index)) % 2 != 0):
                index = 10 ** len(str(index))

                continue

            # Verify validity
            indexasstring = str(index)
            if (indexasstring[len(indexasstring)//2:] == indexasstring[:len(indexasstring)//2]): 
                print('Got one: ' + indexasstring)
                result += index

            index += 1


    print("Deel 1: " + str(result))

def solve2():
    ranges = input.split(',')
    result = 0

    for r in ranges:
        lo, hi = r.split('-')
        #print(lo,hi)
        index = int(lo)
        while (index < int(hi)+1):
            # Make sure only values with even lengths are considered
            if (len(str(index)) % 2 != 0):
                index = 10 ** len(str(index))

                continue

            # Verify validity
            indexasstring = str(index)
            if (indexasstring[len(indexasstring)//2:] == indexasstring[:len(indexasstring)//2]): 
                print('Got one: ' + indexasstring)
                result += index

            index += 1

    print("Deel 2: " + str('No'))

start = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-start)

start = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-start)

