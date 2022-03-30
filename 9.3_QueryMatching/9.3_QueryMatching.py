'''
lab 9.3
Function name : QueryMatching(q, t, n, k)
Input :  q = query (length = p) = CGTTCAGGGGA
         t = text (length = m)  = TATTCGTACATAGGATTTCA
         n = n-letter substring of q
         k = allow mismatch
Output : i = starting position 
Time complexity : O(nm)???
Usage : python ./9.3_QueryMatching.py
Author : Pornsawan Cholsaktrakool 29/3/65
'''
# list index: start from 0
# creat list of all possible substring length n from DNA


class DnsObj:
    def __init__(self, start_q,  start_t, sub_str, mismatch_acception):
        self.__start_q = start_q
        self.__start_t = start_t
        self.__sub_str = sub_str
        self.__mismatch_acception = mismatch_acception

    @property
    def start_q(self):
        return self.__start_q

    @property
    def start_t(self):
        return self.__start_t

    @property
    def sub_str(self):
        return self.__sub_str

    @property
    def mismatch_acception(self):
        return self.__mismatch_acception

    #start_q_p = property(_start_q)

    def __creatWordList(self, DNA, substring_length):
        w = []
        for i in range(len(DNA)-substring_length+1):  # loop all possible start position
            w.append(DNA[i:i+substring_length])       # append substring
        return w

    # list index start from 0

    def QueryMatching(self):
        start_q = []
        start_t = []
        sub_str = []
        # ['CGTTCA', 'GTTCAG', 'TTCAGG', 'TCAGGG', 'CAGGGG', 'AGGGGA']
        substring_q = self.__creatWordList(self.__start_q, self.__sub_str)
        # ['TATTCG', 'ATTCGT', 'TTCGTA', 'TCGTAC', 'CGTACA', 'GTACAT', 'TACATA', 'ACATAG', 'CATAGG', 'ATAGGA', 'TAGGAT', 'AGGATT', 'GGATTT', 'GATTTC', 'ATTTCA']
        substring_t = self.__creatWordList(self.__start_t, self.__sub_str)
        for i in substring_q:
            for j in substring_t:
                dist_ct = 0
                # x = 0 1 2 3 4 5, n = substring length
                for x in range(self.__sub_str):
                    if i[x] != j[x]:    # i='CGTTCA';  j='TATTCG'
                        dist_ct += 1
                if dist_ct <= self.__mismatch_acception:
                    start_q.append(substring_q.index(i))
                    start_t.append(substring_t.index(j))
                    sub_str.append(i)
        return (start_q, start_t, sub_str)

    # position start from 1 for

    def Print(self):
        all_value = self.QueryMatching()
        q = all_value[0]
        t = self.__start_t
        n = all_value[1]
        k = all_value[2]
        for i in range(len(q)):
            # start position เริ่มจาก 1 เพื่อให้ผู้ใช้เข้าใจง่าย
            print('\nFound at', (q[i])+1,
                  'in q and at', (n[i])+1, 'in t.')
            #sub_str = q[q[i]:(q[i])+n]
            print(t)
            print(' '*(n[i]-1), k[i])
        return


# ============================================================
# region Parameter
dna1 = 'CGTTCAGGGGA'
dna2 = 'TATTCGTACATAGGATTTCA'
sub_str_length = 6
mismatch_acception = 2
# endregion

dns_obj = DnsObj('CGTTCAGGGGA', 'TATTCGTACATAGGATTTCA', 6, 2)
test2 = dns_obj.QueryMatching()
dns_obj.Print()
