def ugly_num(n):
    pointers = [0,0,0]
    ans = [1]
    while len(ans) < n:
        while 2*ans[pointers[0]] <= ans[-1]:
            pointers[0]+=1
        while 3*ans[pointers[1]] <= ans[-1]:
            pointers[1]+=1
        while 5*ans[pointers[2]] <= ans[-1]:
            pointers[2]+=1
        ans.append(min(2*ans[pointers[0]], 3*ans[pointers[1]], 5*ans[pointers[2]]))

    return ans[-1]

# Space & Time: O(n)
