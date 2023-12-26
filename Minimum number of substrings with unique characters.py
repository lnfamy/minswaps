"""
https://www.geeksforgeeks.org/find-minimum-number-of-substrings-with-unique-characters/
"""
def solution(s):
    last_seen = [-1] * 26
    start = 0
    ans = 1

    for i in range(len(s)):
        # if the last time we saw this character was after the start of this current substring, we need to start a
        # new substring. that means we have one more substring, therefore we increment the answer by 1 and set the
        # start index of the current substring to the current index i.
        if last_seen[ord(s[i]) - ord('a')] >= start:
            ans += 1
            start = i
        # set the last seen position of this character to its index in the string
        last_seen[ord(s[i]) - ord('a')] = i

    return ans
