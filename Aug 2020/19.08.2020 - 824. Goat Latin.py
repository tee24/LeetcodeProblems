class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = set(['a','e','i','o','u', 'A','E','I','O','U'])

        sentence = S.split()

        for num, word in enumerate(sentence):
            temp = word
            if word[0] not in vowels:
                temp=temp[1:]+temp[0]
            temp+='ma'
            temp+=('a'*(num+1))
            sentence[num] = temp
        return ' '.join(sentence)

