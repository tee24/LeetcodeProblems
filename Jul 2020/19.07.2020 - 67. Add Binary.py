def binary_add(a,b):
    a = list(a)
    b = list(b)
    carry = 0
    answer = []

    while a or b or carry:
        if a:
            carry+=int(a.pop())
        if b:
            carry+=int(b.pop())

        answer.append(str(carry%2))

        carry//=2

    return ''.join(answer)[::-1]

#Space, Time: O(K), K=max(m,n)