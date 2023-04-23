# 이진트리 탐색 이전

이진 탐색을 알기 위해서는 순차탐색에 대해서 알아야한다.
범위가 큰 상황에서의 이진탐색을 가정하는 경우가 많음 (2,000만 이상 or 1,000만 이상)

## 순차탐색

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 시간 복잡도는 O(N)

```
    def soultion(n, target, array):
    for i in range(n):
        if array[i] == target:

            #현재위치 반환
            return i + 1
    -

    find_data = input().split()
    n = int(find_data[0])
    target = find_data[1]
    array = input().split()

    print(solution(n, target, array))
```

### 이진탐색

- 배열이 정렬되어 있어야만 사용할 수 있는 알고리즘
- 찾으려는 데이터에서 시작점, 끝점 , 중간점을 체크한 뒤 찾으려는 데이터와 중간점의 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법
- 시간복잡도 O(logN)
- 구현의 방법은 재귀함수, 반복문

```
# 재귀함수
def solution(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2

	if array[mid] == target:
		return mid
	elif array[mid] > target:
		# 중간값보다 찾는 데이터가 작을 경우 왼쪽 탐색
		return solution(array, target, start, mid - 1)
	else:
		# 중간값보다 찾는 데이터가 클 경우 오른쪽 탐색
		return solution(array, target, start, mid + 1)
	return None

# 반복문
def solution(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			# 중간값보다 찾는 데이터가 작을 경우 왼쪽 탐색
			end = mid - 1
		else:
			# 중간값보다 찾는 데이터가 클 경우 오른쪽 탐색
			start = mid + 1
	return None
-

    n, target = list(map(int, input().split()))
    array = list(map(int, input().split))

    result = solution(array, target, 0 , n-1)

    if result == None:
        print("찾으려는 값 없습니다.")
    else:
        print(result+1)
```

### 트리 자료구조

- 트리는 부모 노드와 자식 노드로 구성
- 최상단 노드 = 루트 노드
- 최하단 노드 = 단말 노드
- 트리 일부를 떼어내도 트리 구조 = 서브트리
- 계층적이고 정렬된 자료를 다루기 용이

### 이진 탐색 트리

- 부모 노드보다 왼쪽 자식 노드가 작다
- 부모 노드보다 오른쪽 자식 노드가 크다
- sys.stdin.readline().rstrip() 으로 빠르게 입력 받아서 이용한다.

</div>
</details>
