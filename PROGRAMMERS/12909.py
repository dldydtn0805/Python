def solution(s):
    l = 0
    r = 0
    for i in range(len(s)):
        if (s[i] == '('):
            l += 1
        else:
            if r == l:
                return False
            r += 1
    if r < l or l > r: 
        return False
    return True
