class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        buff_word1 = {}
        buff_word2 = {}

        for ch in word1:
            if ch not in buff_word1:
                buff_word1[ch] = 1
            else:
                buff_word1[ch] += 1

        for ch in word2:
            if ch not in buff_word2:
                buff_word2[ch] = 1 
            else:
                buff_word2[ch] += 1 

        sorted_word1 = sorted(buff_word1.items(), key = lambda x: x[1])
        sorted_word2 = sorted(buff_word2.items(), key = lambda x: x[1])

        for i in range(len(sorted_word1)):
            w1, w2 = sorted_word1[i][1], sorted_word2[i][1]
            if w1 != w2 or (sorted_word1[i][0] not in buff_word2):
                return False

        return True
        

    