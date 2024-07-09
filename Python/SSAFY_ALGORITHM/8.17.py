"""

def enQ(data):
    global rear
    if rear==Qsize-1:
        print('Q is Full') #가득 차면
    else:
        rear += 1
        Q[rear] = data

def deQ(): #선형 큐에 한해서 인덱스 증가하는 방식으로 구현
    global front
    if front == rear: # 비어있으면
        print('큐가 비어있음')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3
Q = [0]*3
rear = -1
front = -1
enQ(1)
enQ(2)
rear += 1 #enQ(3)
Q[rear] = 3

while front != rear: # 큐가 비어있지 않으면
    front += 1
    print(Q[front])

기본적인 Queue
"""

"""
날먹 Queue
Q = []
Q.append(1) # enqueue(1)
Q.append(2)
Q.append(3)

print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))
"""

"""
원형 큐

def enq(data):
    global rear
    if (rear+1)%cQsize == front:
        print('cQ is Full')
    else:
        rear = (rear+1)%cQsize
        cQ[rear] = data

def deq():
    global front
    front = (front+1)%cQsize
    return cQ[front]

cQsize = 4
cQ = [0]*cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
print(deq())
print(deq())
enq(4)
>1
2

"""
"""

def enq(data):
    global rear
    global front
    if (rear+1)%cQsize==front:
        front = (front+1)%cQsize

    rear = (rear+1)%cQsize
    cQ[rear] = data

def deq():
    global front
    front = (front+1)%cQsize
    return cQ[front]

cQsize = 4
cQ = [0]*cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
print(deq())
print(deq())
print(deq())
print(deq())
"""

from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

print(q.popleft())
print(q.popleft())
print(q.popleft())