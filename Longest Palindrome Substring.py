def longest_palindrome_subsequence(s):
    
    def helper(s,l,r):
        while l >= 0 and r <= len(s)-1 and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

    ans = ''
    for i in range(len(s)):
        even = helper(s,i,i)
        odd = helper(s,i,i+1)
        ans = max(ans, odd, even, key=len)
    return ans

print(longest_palindrome_subsequence('sar'))