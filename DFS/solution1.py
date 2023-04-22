n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def DFS(x,y):
    # 0보다 작거나 n,m보다 클수없음 
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] ==0:
        # 방문한 노드를 1로 초기화
        graph[x][y] =1
        # 상하좌우 재귀적으로 확인
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        # 현재위치에서 DFS수행
        if DFS(i,j) == True:
            result += 1
print(result)