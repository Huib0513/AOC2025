#!python3
import os
import datetime
from collections import defaultdict
from re import finditer

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
    patterns = defaultdict(int)

    for r in ranges:
        lo, hi = r.split('-')

        maxlen = len(hi)//2
        # Loop over all values in the range
        for value in range(int(lo),int(hi)+1):
            foundone = False
            id = str(value)
            # Loop over alle possible pattern lengths: max half of the length of the value
            for patternlength in range(1,maxlen+1):
                startpos = 0
                endpos = startpos+patternlength
                while (id[startpos:endpos] == id[endpos:endpos+patternlength]):
                    if ((endpos+patternlength) < len(id)):
                        startpos = endpos
                        endpos += patternlength
                    else:
                        #print('Got one: ' + id + ' (' + id[startpos:endpos] + ')')
                        foundone = True
                        result += value
                        break
                if (foundone == True): break

##### Algorithm to collect all patterns occurring more than once
#                patterns.clear()
#                for start in range(len(str(value))-patternlength+1):
#                    pattern = str(value)[start:start+patternlength]
#                    # Patterns do not start with a zero
#                    if pattern[0] != '0':
#                        patterns[pattern] += 1
#                # Check only patterns that occur more than once
#                repeats = [key for key in patterns.keys() if patterns[key]>1]
#
#                #Check where in the string a pattern occurs
# #               for c in tocheck:
# #                   positions = [match.start() for match in finditer(c, str(value))]
#                    # If the difference between two positions is the length of the pattern, we have a match
#                if (len(repeats) > 0):
#                    print(value, repeats)
 
    print("Deel 2: " + str(result))

starttime = datetime.datetime.now()
solve1()
print("Tijd voor oplossing 1: ", datetime.datetime.now()-starttime)

starttime = datetime.datetime.now()
solve2()
print("Tijd voor oplossing 2: ", datetime.datetime.now()-starttime)

