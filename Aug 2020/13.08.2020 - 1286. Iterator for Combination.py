class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
    	self.characters = list(characters)
    	self.combinationLength = combinationLength
    	self.combos = [[]]

    	for i in self.characters:
    		self.combos+=[[i]+x for x in self.combos]
    	self.combos = [''.join(x[::-1]) for x in self.combos if len(x)==combinationLength]
    	self.combos = sorted(self.combos)[::-1]
        
    def next(self) -> str:
    	return self.combos.pop()
        

    def hasNext(self) -> bool:
    	return True if self.combos else False


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.combos = self.combinations(self.characters, self.combinationLength)
        self.index = len(self.combos) - 1
        
        
    def next(self) -> str:
        self.index-=1
        temp = self.combos.pop()
        ans = ''
        for i,j in enumerate(temp):
            if j == '1':
                ans+=self.characters[i]
        return ans

    def hasNext(self) -> bool:
        return self.index >= 0

    def combinations(self, chars, comb):
        res = []

        for i in range(int('1'*len(chars),2)+1):
            if bin(i)[2:].count('1') == comb:
                res.append(bin(i)[2:].zfill(len(chars)))
        return res

        
      

