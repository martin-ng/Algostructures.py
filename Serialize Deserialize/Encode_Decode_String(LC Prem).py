# For problems where you need to decode and encode strings over a network, you need to generalize an algorithm
# where you account for all possible characters out of the 256 valid ASCII characters

# This solution marks the length of each string and appends it to a string followed by a space


class Solution:
    def encode(self, strs):
        string = ''
        for s in strs:
            string += str(len(s)) + ' ' + s
        return string

    def decode(self, s):
        if not s:
            return []
        res = []
        length = 0
        n = len(s)
        i = 0

        while i < n:
            if s[i] != ' ':
                length *= 10
                length += int(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
                res.append(s[i:i+length])
                i += length
                length = 0

        return res


new_sln = Solution()
print(new_sln.encode(['martin', 'likes', 'to', 'code']))
encoded_string = new_sln.encode(['martin', 'likes', 'to', 'code'])
print(new_sln.decode(encoded_string))
