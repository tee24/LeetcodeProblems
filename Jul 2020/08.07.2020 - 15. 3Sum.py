def three_sum(nums):
    ans = set()

    p = []
    n = []
    z = []

    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    set_p = set(p)
    set_n = set(n)

    if len(z) > 2:
        ans.add((0,0,0))

    if z:
        for num in set_p:
            if -num in set_n:
                ans.add((-num,0,num))

    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if -(p[i]+p[j]) in set_n:
                x = (-(p[i]+p[j]), p[i], p[j])
                x = tuple(sorted(x))
                ans.add(x)

    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if -(n[i]+n[j]) in set_p:
                x = (-(n[i]+n[j]), n[i], n[j])
                x = tuple(sorted(x))
                ans.add(x)

    return [list(x) for x in ans]

print(three_sum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))



x = (1,4,3)
y = sorted(x)