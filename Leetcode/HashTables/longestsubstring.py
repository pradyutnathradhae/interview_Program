'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


def longestsubstring(s):
    dic = {}
    max_length = first_index = current_max = 0
    for index,i in enumerate(s):
        max_length = max(max_length,current_max)
        if i in dic.keys() and dic[i] >= first_index:
            current_max  = index - dic[i]
            first_index = dic[i] + 1
        else:
            current_max += 1
        dic[i] = index
    
    return max(max_length,current_max)

if __name__ == '__main__':
    s = input("Enter the string:")
    print(longestsubstring(s))