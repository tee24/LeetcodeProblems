class Solution:
	def dfs(self, board,i,j, pos, word):
		if pos == len(word):
			return True #word found
		if not (0<=i<len(board)) or not (0<=j<len(board[0])):
			return
		if board[i][j] != word[pos]:
			return
		temp = board[i][j]
		board[i][j] = '*'
		if self.dfs(board,i+1,j,pos+1, word) or self.dfs(board,i-1,j,pos+1, word) or self.dfs(board,i,j+1,pos+1, word) or self.dfs(board,i,j-1,pos+1, word):
			return True
		board[i][j] = temp #backtrack
		return False
	
	def exist(self, board: List[List[str]], word: str) -> bool:
		if not board or not word:
			return None
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					if self.dfs(board,i,j,0,word):
						return True
		return False
