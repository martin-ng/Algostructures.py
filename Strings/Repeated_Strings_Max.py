
def max_repeated_chars(string, max):
    if len(string) == 0 or max == 0:
        return

    new_str = ''
    n = len(string)
    i = 0
    j = 0
    curr = string[i]

    while i < n:
        if string[i] == curr:
            if j < max:
                new_str += curr
                j += 1
            i += 1
        else:
            curr = string[i]
            j = 0

    return new_str

# Alternative solution


def max_repeated_chars(string, max):
    if len(string) == 0 or max == 0:
        return

    new_str = ''
    last_seen = None
    last_seen_count = None

    for char in string:
        if char != last_seen:
            last_seen = char
            last_seen_count = 1
        else:
            last_seen_count += 1
        if last_seen_count <= max:
            new_str += char

    return new_str


print(max_repeated_chars('aaaabbbbccccdd', 1))
print(max_repeated_chars('aaabbbcccccddddd', 3))
print(max_repeated_chars('mmmaaaaarrtttin', 1))
