"""
Question:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
# code

def check_valid_anagrams(s,t):
    if len(s) != len(t):
        return False
    countT, countS = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countT:
        if countT[c] != countS.get(c, 0):
            return False
    return True

if __name__ == '__main__':
    string1 = "anagram"
    string2 = "nagaram"
    print(check_valid_anagrams(string1, string2))