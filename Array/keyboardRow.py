# https://leetcode.com/problems/keyboard-row/

def findWords(words):

    key_rows = [set('qwertyuiop'), set("asdfghjkl"), set('zxcvbnm')]

    res = []

    for key_row in key_rows:
        for word in words:
            word_set = word.lower()
            for c in word_set:
                if c not in key_row:
                    break
            else:
                res.append(word)

    return res
