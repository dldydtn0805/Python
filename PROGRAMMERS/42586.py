import math 
def solution(progresses, speeds):
    stack = []
    queue = []
    N = len(progresses)
    answer = []
    for i in range(N):
        queue.append(math.ceil((100-progresses[i])/speeds[i]))
    
    for element in queue:
        if stack:
            if stack[-1] < element:
                stack.append(element)
                answer.append(1)
            else:
                answer[-1] += 1 
                
        else:
            stack.append(element)
            answer.append(1)
    return answer
