def solution(arr):
    answer = []
    stack = 10
    for i in arr:
        if stack != i:
            answer.append(i)
            stack=i
        else:
            continue
    return answer