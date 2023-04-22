### DFS(깊이 우선 탐색)

깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다

- 인접 행렬 표현
  루트 노드 = 0
  좌측하단 노드 = 1 / 비용 7
  우측하단 노드 = 2 / 비용 5
  |     | 0   | 1   | 2   |
  | --- | --- | --- | --- |
  | 0   | 0   | 7   | 5   |
  | 1   | 7   | 0   | INF |
  | 2   | 5   | INF | 0   |
- 인접 그래프 표현
  ```python
  INF = 9999999
  graph = [
      [0,7,5],
      [7,0,INF],
      [5,INF,0]
  ]
  print(graph)
  ```
- 인접리스트 표현 방식 예
  ```python
  # 행이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3)]

  # 0번 노드에 연결된 정보 저장 (노드, cost)
  graph[0].append((1,7))
  graph[0].append((2,5))

  # 1번 노드에 연결된 정보 저장
  graph[1].append((0,7))

  # 2번 노드에 연결된 정보 저장
  graph[2].append((0,5))

  print(graph)
  ```

DFS 탐색의 예제 / stack 활용

```python
def DFS(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end="")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited =[False] * 9
print(visited)
DFS(graph,1,visited)
```
