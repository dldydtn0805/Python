def dfs(node,start):
    visited[node]=1
    value=arr[node]
    if not visited[value]:
        dfs(value,start)
    elif visited[value] and value==start:
        res.append(value)

n=int(input())
arr=[0]
res=[]
for i in range(n):
    arr.append(int(input()))

for i in range(1,n+1):
    visited=[0]*(n+1)
    dfs(i,i)

res.sort()
print(len(res))
for ans in res:
    print(ans)
