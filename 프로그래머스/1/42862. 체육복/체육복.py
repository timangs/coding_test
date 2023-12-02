def solution(n, lost, reserve):
    physical_list = [1 for x in range(n)]
    for i in lost:
        physical_list[i-1] -= 1
    for j in reserve:
        physical_list[j-1] += 1
    print(physical_list)
    for k,h in enumerate(physical_list):
        if h == 2:
            if physical_list[k-1] == 0 and k-1 >= 0:
                physical_list[k-1] += 1
                physical_list[k] -= 1
                print(physical_list)
        if physical_list[k] == 2:
            if k != n-1:
                if physical_list[k+1] == 0:
                    physical_list[k+1] += 1
                    physical_list[k] -= 1
                    print(physical_list)

    answer = n - physical_list.count(0)

    return answer
