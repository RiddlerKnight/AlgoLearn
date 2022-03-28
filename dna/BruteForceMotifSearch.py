'''
Algorithms : BruteForce?
Function name :
Input : Enter Seq 1:atcgtt
        Enter Seq 2:ctggga
        Enter Seq 3:acgtgg 
        t = amount of sequence
        l = length of motif
        n = number of NT each sequence
Output :    ATGG

Time complexity is ...
Usage : python ./BruteForceMotifSearch.py
Author : Pornsawan Cholsaktrakool 9/2/2565 1.34 pm

'''

import itertools
from Bio.Seq import Seq
from Bio import motifs


# get input from user
def EnterSequence (t):
    DNA = ["atcgtt".upper(), "ctggga".upper(), "acgtgg".upper() ]
    # for i in range(t): 
    #     a = input("Enter Seq {0}:".format(i+1))
    #     b = a.upper()
    #     DNA.append(list(b)) # [['A', 'T', 'C', 'G', 'T', 'T'], ['C', 'T', 'G', 'G', 'G', 'A'], ['A', 'C', 'G', 'T', 'G', 'G']]   
    return DNA


# get all possible sequence of spcific length(l) from all posible start position 
def CutSeq (DNA,n,l):
    all_cut_seq =[]
    for i in DNA:   # ['A', 'T', 'C', 'G', 'T', 'T']
        cut_seq = []
        for j in range(n-l+1): # possible start position (6-4+1)
            cut_seq.append(''.join(i[j:j+l]))  #  joined 'ATCG'
        all_cut_seq.append(cut_seq)   
    return (all_cut_seq)  


# get all combination of alignment
def Alignment (align):
    x = []
    for temp in itertools.product(*align):
        x.append(temp)
    return x

# profile and scoring to find best motif   
def Profile_and_Score(align):
    bestScore = 0
    all_score = []
    for x in align:
        instance = []
        for i in x:
            instance.append(Seq(i))

        m = motifs.create(instance)
        all_score.append(m)

    # หา max col และรวมเป็น score
    score_list = []
    for profile in all_score:
        cols = []
        for row in profile.counts:
            if len(cols) != len(profile.counts[row]):
                cols = [0] * len(profile.counts[row])
            for col_xi in range(len(cols)):
                if cols[col_xi] < profile.counts[row, col_xi]:
                    cols[col_xi] = profile.counts[row, col_xi]

        score = sum(cols)
        score_list.append([profile, score])

    # หา max score
    max_score_profile = None
    for l in score_list:
        if max_score_profile == None or l[1] > max_score_profile[1]:
            max_score_profile = l

    print("Max score = {0}, with consensus = {1}".format(max_score_profile[1],max_score_profile[0].consensus))


    # for x in align:   # ('ATCG', 'CTGG', 'ACGT')
    #     y = []
    #     for z in x:   # 'ATCG'
    #         y.append(Seq(z))        # get default input for Bio.Seq
    #     profile =  motifs.create(y) # get profile
    #     f = profile.counts          # get frequency_position_matrix
    #                             #         0      1      2      3
    #                             # A:   2.00   0.00   0.00   0.00
    #                             # C:   1.00   1.00   1.00   0.00
    #                             # G:   0.00   0.00   2.00   2.00
    #                             # T:   0.00   2.00   0.00   1.00
     
    #     score = 0    
    #     for i in range(len(profile)): # 0 1 2 3 
    #         c = max(f['A',i],f['C',i],f['G',i],f['T',i])  # max score of each position
    #         score += c
    #     if score > bestScore:
    #         bestScore = score
    #         bestProfile=profile
    #     bestMotif = bestProfile.consensus    
    # # print(bestScore) 
    # # print(bestProfile)
    # return bestMotif


def BruteForceMotifSearch():
    n = 6
    t = 3
    l = 4
    return Profile_and_Score((Alignment ((CutSeq (EnterSequence (t),n,l)))))

print(BruteForceMotifSearch())

'''
Seq1 = "atcgtt"
Seq2 = "ctggga"
Seq3 = "acgtgg"

'''