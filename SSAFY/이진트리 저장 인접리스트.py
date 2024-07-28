arr = [1,2,1,3,2,4,3,5,3,6]
# 인접리스트 = 각자가 갈수있는 경로만 저장, 갈수 없는 경로까지 저장하는 인접행렬에 비해 메모리적으로 효율적
# 이진트리 만들기
nodes = [[] for i in range(0,14)]
for i in range(0,len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i+1]
    nodes[parentNode].append(childNode)
    # nodes[childNode].append(parentNode) # 양방향 저장, 트리에서는 잘 쓰이지 않는다
# for i in range(len(nodes)):
#     print(nodes[i])

# 자식이 더이상 없다는걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None:
        return

    print(nodeNumber, end= ' ')
    preorder(nodes[nodeNumber][0])
    preorder(nodes[nodeNumber][1])

preorder(1)