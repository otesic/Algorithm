<details>
<summary>DFS 선행</summary>

  <div markdown="1">

# 대표적인 그래프 탐색 알고리즘으로써 DFS / BFS가있다.

먼저 DFS알아보기전에 알아야할 스택, 큐가 있다.

### 스택 큐

스택은 = 선입후출 , 큐는 = 선입선출이다.

```
  stack = []

  stack.append(1)
  stack.append(2)
  stack.append(5)
  stack.pop()
  stack.append(9)
  print(stack[::-1]) #최상단 원소부터 출력
  print(stack)
  [9, 2, 1]
  [1, 2, 9]

  from collections import deque

  queue = deque()

  queue.append(1)
  queue.append(2)
  queue.append(3)
  queue.append(4)
  queue.popleft()

  print(queue) #먼저 들어온 순서
  queue.reverse()
  print(queue) #나중에 들어온 순서

  [2, 3, 4]
  [4, 3, 2]
```

### 재귀함수

```
  # 재귀함수로 팩토리얼 구현하기
  def for_fac(n):
      result = 1
      for i in range(1, n+1):
          result *= i
      return result

  def recur_fac(n):
      if n <= 1:
          return 1
      return n * recur_fac(n-1)

  print(for_fac(8))
  print(recur_fac(8))
```

### 유클리드 호제법

두자연수 A,B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 할때
A, B의 최대공약수는 B와 R의 최대공약수와 같다.

```
  # a > b
  def gcd(a,b):
      if a%b==0:
          return b
      return gcd(b,(a%b))

  print(gcd(192,162))
```

</div>
</details>
