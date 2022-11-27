# Given a string s consisting of small English letters, find and return the first instance
# of a non-repeating character in it. If there is no such character, return '_'.

def solution(s):

    for i in range(0, len(s)):
        key = s[i]

        if key not in s[i+1:] and key not in s[:i]:
            return key

    return '_'
