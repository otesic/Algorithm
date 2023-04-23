n, target = map(int, input().split())
h_list = list(map(int,input().split()))

def solution(h_list,target , start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    return binary(h_list,target , mid)

def binary(h_list,target , cutting_size):
    cuted_list = []
    for i in h_list:
        if i < cutting_size:
            cuted_list.append(0)
        else:
            cuted_list.append(i-(cutting_size))
    result = sum(cuted_list)
    if result == target:
        return cutting_size
    elif result > target:
        return binary(h_list,target,cutting_size+1)
    else:
        return binary(h_list,target,cutting_size-1)

print(solution(h_list, target , cutting_size))