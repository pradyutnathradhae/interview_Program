'''
https://leetcode.com/problems/encrypt-and-decrypt-strings/
You are given a character array keys containing unique characters and a string array values containing strings of length 2. You are also given another string array dictionary that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a 0-indexed string.

A string is encrypted with the following process:

For each character c in the string, we find the index i satisfying keys[i] == c in keys.
Replace c with values[i] in the string.
A string is decrypted with the following process:

For each substring s of length 2 occurring at an even index in the string, we find an i such that values[i] == s. If there are multiple valid i, we choose any one of them. This means a string could have multiple possible strings it can decrypt to.
Replace s with keys[i] in the string.
Implement the Encrypter class:

Encrypter(char[] keys, String[] values, String[] dictionary) Initializes the Encrypter class with keys, values, and dictionary.
String encrypt(String word1) Encrypts word1 with the encryption process described above and returns the encrypted string.
int decrypt(String word2) Returns the number of possible strings word2 could decrypt to that also appear in dictionary.
 

Example 1:

Input
["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
Output
[null, "eizfeiam", 2]

Explanation
Encrypter encrypter = new Encrypter([['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]);
encrypter.encrypt("abcd"); // return "eizfeiam". 
                           // 'a' maps to "ei", 'b' maps to "zf", 'c' maps to "ei", and 'd' maps to "am".
encrypter.decrypt("eizfeiam"); // return 2. 
                              // "ei" can map to 'a' or 'c', "zf" maps to 'b', and "am" maps to 'd'. 
                              // Thus, the possible strings after decryption are "abad", "cbad", "abcd", and "cbcd". 
                              // 2 of those strings, "abad" and "abcd", appear in dictionary, so the answer is 2.
 

Constraints:

1 <= keys.length == values.length <= 26
values[i].length == 2
1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
All keys[i] and dictionary[i] are unique.
1 <= word1.length <= 2000
1 <= word2.length <= 200
All word1[i] appear in keys.
word2.length is even.
keys, values[i], dictionary[i], word1, and word2 only contain lowercase English letters.
At most 200 calls will be made to encrypt and decrypt in total.
'''

class Encrypter():

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.keys = keys
        self.values = values
        self.dictionary = dictionary
        self.encrypt_dict = {}
        self.decrypt_dict = {}
        self.count = 0
        for i in range(len(keys)):
            self.encrypt_dict[keys[i]] = values[i]
            if values[i] in self.decrypt_dict:
                self.decrypt_dict[values[i]].append(keys[i])
            else:
                self.decrypt_dict[values[i]] = [keys[i]]
        

        

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        rval = ""
        for i in word1:
            rval += self.encrypt_dict[i]
        return rval

    def combinations_check(self,l,st,ind,len):
        if ind == len:
            # print(st)
            if st in self.dictionary:
                # print(st)
                self.count += 1
            return
        temp = st
        for j in l[ind]:
            st += j
            self.combinations_check(l,st,ind+1,len)
            st = temp
        # for j in l[ind]:
        #     st += j
        #     self.combinations_check(l,st,ind+1,len)
    

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        self.count = 0
        l = []
        for i in range(0,len(word2),2):
            temp = word2[i:i+2]
            if temp not in self.decrypt_dict:
                return 0
            l.append(self.decrypt_dict[temp])
        self.combinations_check(l,"",0,len(l))
        return self.count
        # l = []
        # possible = []
        # temp = 0
        # for i in range(0,len(word2),2):
        #     l.append(self.decrypt_dict[word2[i:i+2]])
        #     possible.append(set())
        # for i in self.dictionary:
        #     for j in range(len(l)):
        #         possible[j].add(i[j])
        # for i in range(len(l)):
        #     for j in l[i]:
        #         if j in possible[i]:
        #             temp += 1
             

        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

if __name__ == '__main__':
    keys, values, dictionary = ['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]
    obj = Encrypter(keys, values, dictionary)
    print(obj.decrypt_dict)
    # print(obj.encrypt("abcd"))
    print(obj.decrypt("eizfeiam"))
    # print(obj.decrypt("aa"))
    # print(obj.decrypt("aaaa"))
    # print(obj.decrypt("aaaaaaaa"))
    # print(obj.decrypt("aaaaaaaaaaaaaa"))
    # print(obj.decrypt("aefagafvabfgshdthn"))