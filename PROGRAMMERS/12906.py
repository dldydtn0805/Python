def solution(arr):
    stack = []
    for ele in arr:
        if stack:
            if stack[-1] != ele:
                stack.append(ele)
        else:
            stack.append(ele)
    return stack
