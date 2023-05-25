'''
lab 9.2
Function name : ApproximatePatternMatching(p, t, k)
Input :  p = pattern (length = n) = CGTTCAGGGGA
         t = text (length = m)  = TATTCGTACATAGGATTTCA
         k = allow mismatch
Output : i = starting position 
Time complexity : O(nm)
Usage : python ./9.2_ApproximatePatternMatching.py
Author : Pornsawan Cholsaktrakool 29/3/65
'''
# start position in this function use Python list index: start from 0
def ApproximatePatternMatching(p, t, k):
    n = len(p)
    m = len(t)
    start_position = []
    for i in range(m-n+1):  # loop all possible start position
        word = t[i:i+n]     # word of each start position
        dist_ct = 0
        for j in range(n):
                if word[j] != p[j]: # Humming distance
                    dist_ct += 1
        if dist_ct <= k:            # get starting position of word ที่ mismatch <= k 
            start_position.append(i)
    # print(start_position)    
    return start_position # position start from 0

# start position start from 1 not 0
def Print(p, t, k, start_position):
    s = []
    for x in start_position:
        s.append(int(x)+1)   # get start position start from 1
    print('Start position of approximate pattern matching which allow',k,'mismatch\n',\
        'Found at position',s,'\n')
    for y in s:
        print(t,'\n',' '*(y-3),p)
    return
   
##==============================================
#p = 'CGTTCAGGGGA'; t = 'TATTCGTACATAGGATTTCA'; k=3
p = 'CGTACAT'; t = 'TATTCGTACATAGGCGTTCAGGGGAATTTCACGTACATCGTACAT'; k=1
start_position = ApproximatePatternMatching(p, t, k)
Print(p, t, k, start_position)