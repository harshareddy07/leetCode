class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        count = 0   
        
        for i in range(len(word)):
            vowels_count = {}
            for j in range(i,len(word)):
                if word[j] not in vowels:
                    break

                vowels_count[word[j]] = vowels_count.get(word[j],0) + 1
                if len(vowels_count) == 5:
                    count += 1

        return count
                