

def string_compression(string):

    n = len(string)
    read = 0
    write = 0

    while read < n:
        curr = string[read]
        count = 0
        while read < len(string) and string[read] == curr:
            read += 1
            count += 1
        string[write] = curr
        write += 1
        if count > 1:
            for c in str(count):
                string[write] = c
                write += 1

    return write


# string = ["a", "a", "b", "b", "c", "c", "c"]
# string = ["a", "a", "a", "a", "b", "c", "d", "d", "d", "e"]
string = ["m", "m", "a", "r", "r", "t", "i", "n", "n"]

print(string_compression(string))
